# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from algo.longest_increasing_sequence import longest_increasing_sequence as ls


class TestLongestIncreasingSequence:
    """
    A Test Suite for longest_increasing_sequence as ls
    """

    def test_sample(self):
        assert ls([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_sample2(self):
        assert ls([1, 2, -3, 4, 5]) == [1, 2, 4, 5]

    def test_sample3(self):
        assert ls([-1, -2, -3, -4, -5]) == [-1]

    def test_sample4(self):
        # multiple possible sequence
        assert len(ls([2, 4, 3, 5, 1, 7, 6, 9, 8])) == 5
        assert ls([2, 4, 3, 5, 1, 7, 6, 9, 8]) == [2, 4, 5, 7, 9]
