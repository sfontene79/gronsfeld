import unittest
from gronsfeld import gronsfeld
from gronsfeld import GronsfeldKey

class TestGronsfeld(unittest.TestCase):

    def test_decipher(self):
        key = GronsfeldKey('123')
        self.assertEqual('aaa', gronsfeld.decipher('bcd', key))

    def test_decipher_long(self):
        key = GronsfeldKey('123')
        self.assertEqual('aaabbbcc', gronsfeld.decipher('bcdcdede', key))


if __name__ == "__main__":
    unittest.main()