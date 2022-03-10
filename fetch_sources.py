from cldfviz.text import render, MD_LINK_PATTERN
from clldutils import jsonlib
def compile_references(md):
    for m in MD_LINK_PATTERN.finditer(md):
        key = m.group("label")
        url = m.group("url")
        if key in ["src", "psrc"]:
            yield url

md = open("combined_tables.md", "r").read()
references = list(compile_references(md))
jsonlib.dump(references, "../yaw_cldf/etc/refs.json")