import yaml
from pathlib import Path
import re
from cldfviz.text import render, MD_LINK_PATTERN
from pycldf import Dataset
import pandas as pd
import pandoc
from clldutils import jsonlib

CONTENT = "content"
TEMP = "var"
TABLES = "tables"

structure = yaml.load(open("structure.yaml"), Loader=yaml.SafeLoader)
tables = jsonlib.load("tables/table_metadata.json")

tasks = ["structure", "github", "preview", "latex"]

if "structure" in tasks:
    print("Checking files...")
    
    def enumerate_children(child_id, child_data, depths, level, tuples):
        depths[level] += 1
        tuples.append((child_id, "".join([str(x) for x in depths.values()])))
        if "children" in child_data:
            for cchild_id, cchild_data in child_data["children"].items():
                tuples = enumerate_children(
                    cchild_id, cchild_data, depths, level + 1, tuples
                )
        return tuples
    
    
    depths = {0: 0, 1: 0, 2: 0, 3: 0}
    tuples = []
    for child_id, child_data in structure["document"]["children"].items():
        # depths[0] += 1
        tuples = enumerate_children(child_id, child_data, depths, 0, tuples)
    
    num_pre = re.compile("[\d]+\ ")
    
    content_files = {}
    tent = Path(CONTENT)
    for file in tent.iterdir():
        if ".md" not in file.name:
            continue
        name = re.sub(num_pre, "", file.stem)
        content_files[name] = file
    
    var_files = {}
    var = Path(TEMP)
    for file in var.iterdir():
        if ".md" not in file.name:
            continue
        name = re.sub(num_pre, "", file.stem)
        var_files[name] = file
    
    for section, number in tuples:
        fname = f"{number} {section}.md"
        new_path = Path(CONTENT, fname)
        if section in content_files:
            if section in var_files:
                print(f"CONFLICT: {section}. Resolve manually.")
            else:
                if content_files[section] != new_path:
                    print(f"'{section}': {content_files[section]} > {new_path}")
                    print("GOOD")
                    content_files[section].rename(new_path)
                del content_files[section]
        elif section in var_files:
            if var_files[section] != new_path:
                print(f"'{section}': {var_files[section]} > {new_path}")
                var_files[section].rename(new_path)
            del var_files[section]
        else:
            print(f"'{section}': creating {new_path}")
            new_path.touch()
    
    for id, file in content_files.items():
        new_path = Path(TEMP, file.name)
        print(f"Unlisted: {file} > {new_path}")
        file.rename(new_path)

compiled = []
for file in tent.iterdir():
    if ".md" not in file.name:
        continue
    content = open(file).read()
    compiled.append(content)
compiled = "\n".join(compiled)

with open("combined_raw.md", "w") as outfile:
    outfile.write(compiled)

def insert_tables(md, latex=False):
    current = 0
    for m in MD_LINK_PATTERN.finditer(md):
        yield md[current : m.start()]
        current = m.end()
        key = m.group("label")
        url = m.group("url")
        if key == "table":
            print(tables[url])
            table = pd.read_csv(Path(TABLES, f"{url}.csv"), keep_default_na=False)
            if latex:
                table_str = f"""\\begin{{table}}
\\caption{{{tables[url]['caption']}}}
\\label{{{url}}}
\\centering
{table.to_latex(index=False)}
\\end{{table}}
"""
                yield table_str
            else:
                yield table.to_markdown(index=False)
        else:
            yield md[m.start() : m.end()]
    yield md[current:]


def iter_md(md, latex=False):
    current = 0
    for m in MD_LINK_PATTERN.finditer(md):
        yield md[current : m.start()]
        current = m.end()
        key = m.group("label")
        url = m.group("url")
        if key == "src":
            if not latex:
                yield f"[{url}](sources.bib?with_internal_ref_link&ref&year_brackets=round#cldf:{url})"
            else:
                yield f"""[References](Source?with_anchor#cldf:{url}"""
        elif key == "psrc":
            if not latex:
                yield f"[{url}](sources.bib?with_internal_ref_link&ref&year_brackets=round#cldf:{url})"
            else:
                yield f"""[References](Source?parencites=True#cldf:{url})"""
        elif key == "form":
            yield f"[{url}](FormTable#cldf:{url})"
        elif key == "meaning":
            yield f"[Concept {url}](FormTable?parameterReference={url}#cldf:__all__)"
        elif key == "ex":
            yield f"[Example {url}](ExampleTable#cldf:{url})"
        elif key == "mp":
            yield f"[Morpheme {url}](MorphsetTable#cldf:{url})"
        elif key == "m":
            yield f"[Morph {url}](MorphTable#cldf:{url})"
        elif key == "refs":
            if latex:
                yield """[References](Source?with_anchor#cldf:__all__)"""
            else:
                yield """# References
[References](Source?with_anchor#cldf:__all__)"""
        elif key == "label":
            if latex:
                yield f"""{{#{url}}}"""
            else:
                yield f"""<a name="{url}"></a>"""
        else:
            yield md[m.start() : m.end()]
    yield md[current:]


def preprocess(md):
    md = "".join(insert_tables(md))
    with open("combined_tables.md", "w") as outfile:
        outfile.write(md)
    md = "".join(iter_md(md))
    return md

def preprocess_latex(md):
    md = "".join(insert_tables(md, latex=True))
    md = "".join(iter_md(md, latex=True))
    return md

preprocessed = preprocess(compiled)
old_preprocessed = open("combined_preprocessed.md", "r").read()
if preprocessed != old_preprocessed or 1 ==1:
    with open("combined_preprocessed.md", "w") as outfile:
        outfile.write(preprocessed)

    ds = Dataset.from_metadata("../yaw_cldf/cldf/metadata.json")
    if "github" in tasks:
        output = render(preprocessed, ds, template_dir="github_templates")
        with open("README.md", "w") as f:
            f.write(output)
    if "preview" in tasks:
        output = render(preprocessed, ds, template_dir="plain_templates")
        with open("preview.md", "w") as f:
            f.write(output)
        print(output)
    if "latex" in tasks:
        tmpl = open("latex_version/tmpl.tex", "r").read()
        output = render(preprocess_latex(compiled), ds, template_dir="latex_templates")
        doc = pandoc.read(output)
        with open("latex_version/main.tex", "w") as f:
            f.write(tmpl + "\n\n" + pandoc.write(doc, format="latex") + "\n\n\\end{document}")