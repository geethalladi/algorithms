# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from typing import List

from algo.word_ladder import find_shortest_path, bucket, to_buckets


class TestWordLadder:
    """
    A Test Suite for WordLadder
    """

    words: List[str]

    def setup_method(self):
        self.words = ['fail', 'fall', 'pall', 'pole', 'poll',
                      'foil', 'foul', 'fool', 'cool', 'pool',
                      'pope', 'pale', 'sale', 'sage', 'page']

    def test_one(self):
        assert find_shortest_path(
            self.words, 'fool', 'sage') == ['Fool', 'Pool', 'Poll',
                                            'Pall', 'Pale', 'Sale', 'Sage']

    def test_bucket(self):
        assert bucket('FOOL') == ['_OOL', 'F_OL', 'FO_L', 'FOO_']
        assert bucket('F') == ['_']
        assert bucket('FO') == ['_O', 'F_']

    def test_words_to_bucket(self):
        assert to_buckets(['FOOL']) == {
            '_OOL': ['FOOL'], 'F_OL': ['FOOL'],
            'FO_L': ['FOOL'], 'FOO_': ['FOOL']
        }
        assert to_buckets(['FOOL', 'ABCD']) == {
            '_OOL': ['FOOL'], 'F_OL': ['FOOL'], 'FO_L': ['FOOL'], 'FOO_': ['FOOL'],
            'ABC_': ['ABCD'], 'AB_D': ['ABCD'], 'A_CD': ['ABCD'], '_BCD': ['ABCD']
        }
        assert to_buckets(['FOOL', 'POOL']) == {
            '_OOL': ['FOOL', 'POOL'], 'F_OL': ['FOOL'],
            'FO_L': ['FOOL'], 'FOO_': ['FOOL'],
            'POO_': ['POOL'], 'PO_L': ['POOL'], 'P_OL': ['POOL']
        }
