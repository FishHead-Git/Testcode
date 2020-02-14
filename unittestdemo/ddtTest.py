import unittest
from ddt import ddt, data, unpack, file_data


@ddt
class DdtTestCase(unittest.TestCase):

    @unpack
    @data(
        {'word': 'A', 'word2': "B", "word3": "C"},
        {'word': 'D', 'word2': "E", "word3": "F"},
        {'word': 'G', 'word2': "H", "word3": "I"}
    )
    def test_tcfunc(self, word, word2, word3):
        print(word, word2, word3, type(word))


if __name__ == '__main__':
    unittest.main(verbosity=2)
