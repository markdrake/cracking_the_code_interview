__author__ = 'mark'

import unittest
from exercises import str_unique_chars


class TestUniqueChars(unittest.TestCase):
    def test_string_with_unique_chars_only(self):
        input_text = 'string'
        expected = True

        self.assertEquals(expected, str_unique_chars(input_text))

    def test_string_with_repeated_chars(self):
        input_text = 'aabbcccc'
        expected = False

        self.assertEquals(
            expected,
            str_unique_chars(input_text),
            "The string contains repeated chars and unique_chars failed to detect them"
        )

if __name__ == '__main__':
    unittest.main()

