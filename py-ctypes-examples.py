import unittest
from sys import platform as _platform
from ctypes import *


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        if (_platform == "darwin"):
            self.native_lib = CDLL("build/output/libctypes_test_lib.dylib")
        else:
            raise Exception("platform not supported yet")

    def test_in_array_char_p(self):
        list_type = c_char_p * 3
        props = list_type()
        props[0] = c_char_p("ctype item 1")
        props[1] = c_char_p("ctype item 2")
        props[2] = c_char_p()
        self.native_lib.pass_array(props)

    def test_in_out_char_buffer(self):
        buffer = create_string_buffer(8)
        self.native_lib.populate_string(buffer, 8)
        self.assertTrue(buffer.value=="Hello")

    def test_w_char_p(self):
        str_p = c_char_p()
        str = "Hello"
        str_p.value = str
        str = "Hello World"
        self.assertFalse(str_p.value == str) # should not be equal, strings are immutable
        str_p.value=str
        self.assertTrue(str_p.value == str)  # should not be equal, strings are immutable
        str_p.value="Hi there"
        self.assertFalse("Hi there" == str)  # should not be equal, strings are immutable
        # what about
        print "value of str_p is", str_p
        print "value of str_p.value is", str_p.value
        # what about null pointer
        p = c_char_p()
        print p

    def test_string_buffer(self):
        p = create_string_buffer(3)  # create a 3 byte buffer, initialized to NUL bytes
        print(sizeof(p), repr(p.raw))
        self.assertTrue(sizeof(p)==3)
        p = create_string_buffer("Hello")  # create a buffer containing a NUL terminated string
        print(sizeof(p), repr(p.raw))
        self.assertTrue(sizeof(p) == 6)
        b'Hello\x00'
        p = create_string_buffer("Hello", 10)  # create a 10 byte buffer
        print(sizeof(p), repr(p.raw))
        self.assertTrue(sizeof(p) == 10)
        p.value = "Hi"
        print(sizeof(p), repr(p.raw))
        self.assertTrue(sizeof(p) == 10)

    def test_libc(self):
        libc = cdll.LoadLibrary("/usr/lib/libSystem.dylib")
        printf = libc.printf
        printf(b"Hello, %s\n", b"World!")
        timestamp = libc.time(None)
        print type(timestamp)

if __name__ == '__main__':
    unittest.main()