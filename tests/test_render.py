from pylingdocs.output import create_output
from pylingdocs.helpers import load_content
import pytest
from writio import load
from pycldf import Dataset
from pathlib import Path

def test_build():
    contents = load_content()
    dataset = Dataset.from_metadata("cldf/metadata.json")
    create_output(
        contents=contents,
        source_dir=".",
        output_dir="output",
        dataset=dataset,
        formats=["html"],
        structure=load("docs/structure.yaml"),
        metadata=load("metadata.yaml"),
    )
