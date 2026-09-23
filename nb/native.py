"""Platform parser bindings."""
import ctypes
import pathlib

_LIB = pathlib.Path(__file__).parent / "_nbprofile.so"

def load():
    lib = ctypes.CDLL(str(_LIB))
    lib.nb_profile_parse.argtypes = [ctypes.c_char_p]
    lib.nb_profile_parse.restype = ctypes.c_int
    return lib
