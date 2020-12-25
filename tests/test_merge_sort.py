# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from algo.merge_sort import sort


class TestMergeSort:
    def test_empty(self):
        assert sort([]) == []

    def test_none(self):
        assert sort(None) == []

    def test_single(self):
        assert sort([1]) == [1]

    def test_sorted(self):
        assert sort([1, 2, 3, 4]) == [1, 2, 3, 4]

    def test_unsorted(self):
        assert sort([1, 4, 3, 2, 0, -1]) == [-1, 0, 1, 2, 3, 4]

    def test_reverse_sorted(self):
        assert sort([4, 3, 2, 1, 0]) == [0, 1, 2, 3, 4]
