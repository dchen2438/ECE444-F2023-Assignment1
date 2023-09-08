import unittest
from file import utils

class test_utils(unittest.TestCase):
    def test_reversed(self):
        a = utils()
        with self.assertRaises(TypeError):
            a.reversed("123")
        with self.assertRaises(TypeError):
            a.reversed(123.123)
        self.assertEqual(a.reversed(123), 321)
    
    def test_formatter(self):
        a = utils()
        with self.assertRaises(TypeError):
            a.formatter("123")
        with self.assertRaises(TypeError):
            a.formatter(123.123)
        self.assertEqual(a.formatter(123), ('1111011', '173'))

if __name__ == '__main__':
    unittest.main()