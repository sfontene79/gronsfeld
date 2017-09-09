import unittest
from gronsfeld import textutils

class TestTextUtils(unittest.TestCase):

    def test_rotatePositive(self):
        self.assertEqual(textutils.rotate('a', 1), 'b')

    def test_rotateNegative(self):
        self.assertEqual(textutils.rotate('b', -1), 'a')

    def test_rotatePositiveLimit(self):
        self.assertEqual(textutils.rotate('y', 3), 'b')

    def test_rotateNegativeLimit(self):
        self.assertEqual(textutils.rotate('b', -3), 'y')

    def test_score_nomatch(self):
        self.assertEqual(0, textutils.score('abcdefgn', ['un']))
         
    def test_score_shortmatch(self):
        self.assertEqual(1, textutils.score('abudefgn', ['un']))
         
    def test_score_shortmatch_multiplematches(self):
        self.assertEqual(2, textutils.score('abudeugn', ['un']))
         
    def test_score_longmatch(self):
        self.assertEqual(15, textutils.score('abctroisdefg', ['trois']))
         
    def test_score_longmatch_multiplematches(self):
        self.assertEqual(30, textutils.score('abctroisdeftroisgs', ['trois']))
         
    def test_score_singlematch_multiplewords(self):
        self.assertEqual(18, textutils.score('abctroisdefungs', ['trois', 'un']))
         
if __name__ == '__main__':
    unittest.main()