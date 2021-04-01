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
        assert ed('hello', 'hello') == (0, 'MMMMM')

    def test_substitute(self):
        assert ed('ADCD', 'ABCE') == (2, 'MSMS')

    def test_match(self):
        assert ed('ADCD', 'ABCD') == (1, 'MSMM')

    def test_insert(self):
        assert ed('hell', 'hello') == (1, 'MMMMI')

    def test_delete(self):
        assert ed('hello', 'hell') == (1, 'MMMMD')

    def test_insert_middle(self):
        assert ed('hll', 'hello') == (2, 'MIMMI')

    def test_delete_middle(self):
        assert ed('hello', 'hll') == (2, 'MDMMD')

    def test_insert_begin(self):
        assert ed('llo', 'hello') == (2, 'IIMMM')

    def test_original(self):
        assert ed('thou-shalt-not', 'you-should-not') == (5, 'DSMMMMMISMSMMMM')
