from ctypes import *
import os

sdl_lib = CDLL(os.path.abspath("../sdl-lib/cmult.so"))

print(sdl_lib.cmult(2, 2))