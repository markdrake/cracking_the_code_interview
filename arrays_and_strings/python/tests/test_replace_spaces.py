__author__ = 'mark'

import unittest
from exercises import str_replace_spaces


class TestReplaceSpaces(unittest.TestCase):
    def test_string_replace_spaces(self):
        input_text = 'Hello world!'
        expected = 'Hello%20world!'

        self.assertEquals(expected, str_replace_spaces(input_text))

if __name__ == '__main__':
    unittest.main()

