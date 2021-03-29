"""
Module for implementing min and max heap data structures
"""

import logging as log

from typing import Generic, List, TypeVar, Protocol

from algo.graphs.edge import EdgeInput
from algo.graphs.graph import Graph

__all__ = ['sort', 'Heap']


CT = TypeVar('CT', bound='Comparable')


class Comparable(Protocol):  # pylint: disable=too-few-public-methods
    """
    Protocol for Comparable
    """

    def __lt__(self: CT, other: CT) -> bool:
        """
        Return true, if self < other
        """
        ...


class Heap(Generic[CT]):
    """
    Heap as a data structure
    """

    # entries for storing the elements
    # using 1-based index
    entries: List[CT]
    size: int

    def __init__(self, reverse: bool = False):
        self.entries = []
        self.size = 0
        self.reverse = reverse

    def insert(self, element: CT):
        """
        Insert the element into the heap
        """
        if self.size == 0:
            # TODO: remove this dirty hack
            # Insert twice for the first element
            # to simulate 1 based index
            self.entries.append(element)

        # ensure the tree order is maintained
        self.entries.append(element)
        self.size += 1
        log.debug('Inserting element %s at %s', element, self.size)

        # ensure the heap order is maintained
        self._bubble_up(self.size)

    def get(self) -> CT:
        """
        Get the dominant element
        """
        assert not self.empty(), 'Empty Heap'
        log.debug('Get element from heap of size %s', self.size)

        self._swap(1, self.size)
        result: CT = self.entries.pop(self.size)
        self.size -= 1

        # maintain the heap property
        if not self.empty():
            self._bubble_down(1)

        return result

    def _bubble_up(self, pos: int):
        """
        Bubble up till it reaches its equilibrium
        based on the dominance relation
        """
        if pos == 1:
            log.debug('Reached the top after bubbling up')
            return
        parent = self._parent(pos)
        if self._is_dominant(pos, parent):
            # If more dominant than the parent
            self._swap(pos, parent)
            # tail call recursion
            self._bubble_up(parent)

    def _bubble_down(self, pos: int):
        log.debug('Bubbling down from index %s', pos)
        d: int = self._find_dominant(pos)
        if d == pos:
            # pos is dominant when compared to its children
            # stoping bubbling down
            log.debug('Stopping bubbling down at %s', pos)
            return

        # Swap with the dominant child
        # and continue bubbling down
        self._swap(d, pos)
        self._bubble_down(d)

    def _find_dominant(self, pos: int):
        """
        Find dominant between element at 'pos' and its children
        """
        assert self._valid(pos), 'Index {} is not inside heap'.format(
            pos)

        result: int = pos
        for child in [self._left(pos), self._right(pos)]:
            if self._valid(child) and self._is_dominant(child, result):
                result = child

        return result

    def _is_dominant(self, i, j) -> bool:
        """
        Returns true if index 'i' is more dominant
        than index 'j'
        """
        assert self._valid(i), 'Index {} is not within heap'.format(i)
        assert self._valid(j), 'Index {} is not within heap'.format(j)

        return self._is_dominant_value(self.entries[i], self.entries[j])

    # pylint: disable=invalid-name
    def _is_dominant_value(self, x: CT, y: CT) -> bool:
        """
        Check if value 'x' dominates value 'y'
        """
        if self.reverse:
            # check the other direction (max heap)
            return x > y
        # min heap
        return x < y

    def _swap(self, i, j):
        """
        Swap the value at both the indices
        """
        assert self._valid(i), 'Index {} is not within heap'.format(i)
        assert self._valid(j), 'Index {} is not within heap'.format(j)

        self.entries[i], self.entries[j] = self.entries[j], self.entries[i]

    def _valid(self, i):
        """
        Check if the index is valid
        """
        return 1 <= i <= self.size

    def empty(self) -> bool:
        """
        Check if the heap is empty
        """
        return self.size <= 0

    def visualize(self):
        """
        Visualize the heap
        """
        if self.empty():
            log.debug('Empty heap nothing to visualize')
            return

        def add_edge(parent, child, edges):
            if not self._valid(child):
                return
            e: EdgeInput = (
                '{}({})'.format(self.entries[parent], parent),
                '{}({})'.format(self.entries[child], child)
            )
            edges.append(e)

        edges: List[EdgeInput] = []
        # TODO: can be pruned to self.size // 2.
        for i in range(1, self.size):
            left, right = self._left(i), self._right(i)
            add_edge(i, left, edges)
            add_edge(i, right, edges)

        g = Graph.build('heap', edges, directed=False)
        g.view(pause=True)

    @classmethod
    def _parent(cls, pos: int) -> int:
        # floor(n, 2)
        return pos // 2

    @classmethod
    def _left(cls, pos: int) -> int:
        return pos * 2

    @classmethod
    def _right(cls, pos: int) -> int:
        return (2 * pos) + 1


def sort(values: List[int], reverse: bool = False) -> List[int]:
    """
    Sort the list using heap data structure
    """
    h = Heap[int](reverse)
    for v in values:
        h.insert(v)

    result = []
    while not h.empty():
        result.append(h.get())

    return result
