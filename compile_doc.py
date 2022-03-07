import yaml
from pathlib import Path
import re
from cldfviz.text import render, MD_LINK_PATTERN
from pycldf import Dataset
import pandas as pd

CONTENT = "content"
TEMP = "var"
TABLES = "tables"

structure = yaml.load(open("structure.yaml"), Loader=yaml.SafeLoader)

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


def iter_md(md):
    current = 0
    for m in MD_LINK_PATTERN.finditer(md):
        yield md[current : m.start()]
        current = m.end()
        key = m.group("label")
        url = m.group("url")
        if key == "src":
            yield f"[{url}](sources.bib?with_internal_ref_link&ref#cldf:{url})"
        elif key == "psrc":
            yield f"([{url}](sources.bib?with_internal_ref_link&ref#cldf:{url}))"
        elif key == "form":
            yield f"[{url}](FormTable#cldf:{url})"
        elif key == "meaning":
            yield f"[Concept {url}](FormTable?parameterReference={url}#cldf:__all__)"
        elif key == "ex":
            yield f"[Example {url}](ExampleTable#cldf:{url})"
        elif key == "table":
            table = pd.read_csv(Path(TABLES, f"{url}.csv"), keep_default_na=False)
            yield table.to_markdown(index=False)
        else:
            yield md[m.start() : m.end()]
    yield md[current:]


def preprocess(md):
    return "".join(iter_md(md))


preprocessed = preprocess(compiled)
with open("combined_preprocessed.md", "w") as outfile:
    outfile.write(preprocessed)

ds = Dataset.from_metadata("../yaw_cldf/cldf/metadata.json")
output = render(preprocessed, ds)
with open("README.md", "w") as f:
    f.write(output)
print(output)
