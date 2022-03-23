# -*- coding: utf-8 -*-
"""Notebook-check script."""
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from art import tprint

NOTEBOOKS_LIST = [
    "ArtList",
    "DecorList",
    "FontList"]

EXTENSION = ".ipynb"

if __name__ == "__main__":
    tprint("ART", "bulbhead")
    tprint("Notebook Check", "bulbhead")
    print("Processing ...")
    for index, notebook in enumerate(NOTEBOOKS_LIST):
        ep = ExecutePreprocessor(timeout=6000, kernel_name='python3')
        path = os.path.join("", notebook)
        with open(path + EXTENSION, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
            ep.preprocess(nb, {'metadata': {'path': ''}})
        with open(path + EXTENSION, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print("{0}.{1} [OK]".format(str(index + 1), notebook))
