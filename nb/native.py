"""Platform parser bindings."""
import importlib


def load():
    return importlib.import_module("nb._nbprofile")
