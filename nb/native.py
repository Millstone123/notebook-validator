"""Notebook profile parser bindings."""
from nb_profiles_native import nb_profile_parse


def parse(path):
    return nb_profile_parse(str(path).encode())
