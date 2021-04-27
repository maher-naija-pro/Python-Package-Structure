from unittest import TestCase

import py_package

class Test(TestCase):
    def test_is_string(self):
        s = py_package.my_function()
        self.assertTrue(isinstance(s, basestring))
