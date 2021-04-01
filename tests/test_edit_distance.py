# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from algo.edit_distance import edit_distance as ed


class TestEditDistance:
    """
    A Test Suite for edit_distance
    """

    def test_same(self):
        assert ed('hello', 'hello') == (0, '')

    def test_insert(self):
        assert ed('ello', 'hello') == (1, 'Immmm')
