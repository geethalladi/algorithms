# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from algo.priority_queue import PriorityQueue


class TestPriorityQueue:
    """
    A Test Suite for PriorityQueue
    """

    def test_descending(self):
        pq = PriorityQueue()
        pq.insert('A', 1, None)
        pq.insert('B', 2, None)
        pq.insert('C', 3, None)

        assert pq.get() == ('C', None)
        assert pq.get() == ('B', None)
        assert pq.get() == ('A', None)

    def test_ascending(self):
        pq = PriorityQueue()
        pq.insert('A', -1, None)
        pq.insert('B', -2, None)
        pq.insert('C', -3, None)

        assert pq.get() == ('A', None)
        assert pq.get() == ('B', None)
        assert pq.get() == ('C', None)

    def test_descending_reversed(self):
        pq = PriorityQueue(reverse=True)
        pq.insert('A', 1, None)
        pq.insert('B', 2, None)
        pq.insert('C', 3, None)

        assert pq.get() == ('A', None)
        assert pq.get() == ('B', None)
        assert pq.get() == ('C', None)

        assert pq.empty()

    def test_update(self):
        pq = PriorityQueue()
        pq.insert('A', 1, None)
        pq.insert('B', 2, None)
        pq.insert('C', 3, None)
        pq.insert('D', 4, None)

        pq.update('D', 0)

        assert pq.get() == ('C', None)
        assert pq.get() == ('B', None)
        assert pq.get() == ('A', None)
        assert pq.get() == ('D', None)
