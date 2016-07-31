# testing passing char** to a c function
from ctypes import *

native_lib = CDLL("../build/output/libctypes_test_lib.dylib")

list_type = c_char_p * 3
props = list_type()
props[0]=c_char_p("ctype item 1")
props[1]=c_char_p("ctype item 2")
props[2]=c_char_p()
print type(props)
native_lib.pass_array(props)
