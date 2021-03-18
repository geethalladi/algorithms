# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from algo.graphs.word_ladder import WordLadder


class TestWordLadder:
    """
    A Test Suite for WordLadder
    """

    def test_empty(self):
        wl: WordLadder = WordLadder(4, 'words.txt')
        assert wl is not None

    def test_one(self):
        wl: WordLadder = WordLadder(4)
        assert wl.solution('FOOL', 'SAGE') == ['FOOL', 'SAGE']
