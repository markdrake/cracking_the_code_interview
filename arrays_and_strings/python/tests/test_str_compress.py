__author__ = 'mark'

import unittest
from exercises import str_compress


class StrCompressTestCase(unittest.TestCase):
    def test_string_compressed(self):
        input_text = 'this is a string that requires being compressed'
        expected = 'a2c1b1e5d1g2i5h2m1o1n2q1p1s6r4u1t4'
        self.assertEqual(expected, str_compress(input_text))

    def test_string_does_not_compress_if_resulting_string_is_greater_than_original(self):
        input_text = 'abcdefg'
        expected = 'abcdefg'

        self.assertEqual(expected, str_compress(input_text))

if __name__ == '__main__':
    unittest.main()
