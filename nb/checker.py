"""Notebook metadata validation."""
import pathlib

from .native import load


def check_notebooks(path="notebooks"):
    root = pathlib.Path(path)
    if not root.exists():
        return ["missing notebook directory"]
    issues=[]
    lib=load()
    for notebook in sorted(pathlib.Path(path).glob("*.json")):
        if lib.nb_profile_parse(str(notebook).encode()) != 0:
            issues.append(notebook.name)
    return issues
