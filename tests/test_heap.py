# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from algo.heap import sort, Heap


class TestHeap:
    """
    A Test Suite for heap
    """

    def test_empty(self):
        assert sort([]) == []

    def test_single(self):
        assert sort([1]) == [1]

    def test_already_sorted(self):
        assert sort([1, 2]) == [1, 2]

    def test_reverse_sorted(self):
        assert sort([2, 1]) == [1, 2]

    def test_sort_2(self):
        assert sort([1, 2, 3, 4, -1, -2, -3, -4, 0]
                    ) == [-4, -3, -2, -1, 0, 1, 2, 3, 4]

    def test_heap(self):
        h = Heap()
        h.insert(1)
        h.insert(2)
        h.insert(3)
        h.insert(4)
        h.insert(-1)
        h.insert(-2)
        h.insert(-3)
        h.insert(-4)
        # h.visualize()
