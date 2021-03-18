# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from algo.graphs.word_ladder import find_shortest_path, bucket


class TestWordLadder:
    """
    A Test Suite for WordLadder
    """

    def setup_method(self):
        self.words = ['FOOL', 'POOL', 'POLL', 'POLE', 'PALE', 'SALE', 'SAGE']

    def test_one(self):
        find_shortest_path(self.words, 'fool', 'sage')

    def test_bucket(self):
        assert bucket('FOOL') == ['_OOL', 'F_OL', 'FO_L', 'FOO_']
        assert bucket('F') == ['_']
        assert bucket('FO') == ['_O', 'F_']
