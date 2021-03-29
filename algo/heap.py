"""
Module for implementing min and max heap data structures
"""

import logging as log
import sys

from typing import List

from algo.graphs.edge import EdgeInput
from algo.graphs.graph import Graph

__all__ = ['sort', 'Heap']


class Heap:
    """
    Heap as a data structure
    """

    # entries for storing the elements
    # using 1-based index
    entries: List[int]
    length: int

    def __init__(self, reverse: bool = False):
        self.entries = [sys.maxsize]
        self.length = 0
        self.reverse = reverse

    def insert(self, element: int):
        """
        Insert the element into the heap
        """
        self.length += 1
        # ensure the tree order is maintained
        self.entries.append(element)
        log.info('Inserting element %s at %s', element, self.length)

        # ensure the heap order is maintained
        self._bubble_up(self.length)

    def get(self) -> int:
        """
        Get the dominant element
        """
        assert not self.empty(), 'Empty Heap'
        log.info('Get element from heap of size %s', self.length)

        result: int = self.entries[1]
        replacement: int = self.entries.pop(self.length)
        self.length -= 1

        if self.empty():
            # no need to bubble down
            return result

        # maintains the tree order
        self.entries[1] = replacement
        # maintain the heap property
        self._bubble_down(1)
        return result

    def _bubble_up(self, index: int):
        """
        Bubble up till it reaches its equilibrium
        based on the dominance relation
        """
        if index == 1:
            log.info('Reached the top after bubbling up')
            return
        parent = self._parent(index)
        if self._is_dominant(index, parent):
            # If more dominant than the parent
            self._swap(index, parent)
            # tail call recursion
            self._bubble_up(parent)

    def _bubble_down(self, index: int):
        log.info('Bubbling down from index %s', index)
        left = self._left(index)
        right = self._right(index)

        # if (left > self.length) and (right > self.length):
        #     # leaf node
        #
        #     return

        d: int = self._find_dominant(index, left, right)
        if d == index:
            # d is dominant when compared to its children
            # stoping bubbling down
            log.info('Stopping bubbling down at %s', index)
            return

        # Swap with the dominant child
        # and continue bubbling down
        self._swap(d, index)
        self._bubble_down(d)

    def _find_dominant(self, index, left, right):
        assert 1 <= index <= self.length, 'Index {} is not inside heap'.format(
            index)

        # For leaf node, return the index
        if (not self._valid_index(left)) and (not self._valid_index(right)):
            return index

        # checking the dominance with left child
        result: int = index
        if self._is_dominant(left, index):
            result = left

        # no right child then return the result
        if (right > self.length):
            return result

        # both the child exists
        # and the right dominates
        if self._is_dominant(right, result):
            result = right

        return result

    def _is_dominant(self, i, j) -> bool:
        """
        Returns true if index 'i' is more dominant
        than index 'j'
        """
        assert self._valid_index(i), 'Index {} is not within heap'.format(i)
        assert self._valid_index(j), 'Index {} is not within heap'.format(j)

        return self._is_dominant_value(self.entries[i], self.entries[j])

    # pylint: disable=invalid-name
    def _is_dominant_value(self, x: int, y: int) -> bool:
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
        assert self._valid_index(i), 'Index {} is not within heap'.format(i)
        assert self._valid_index(j), 'Index {} is not within heap'.format(j)

        self.entries[i], self.entries[j] = self.entries[j], self.entries[i]

    def _valid_index(self, i):
        """
        Check if the index is valid
        """
        return 1 <= i <= self.length

    def empty(self) -> bool:
        """
        Check if the heap is empty
        """
        return self.length <= 0

    def visualize(self):
        """
        Visualize the heap
        """
        if self.empty():
            log.info('Empty heap nothing to visualize')
            return

        def add_edge(parent, child, edges):
            if not self._valid_index(child):
                return
            e: EdgeInput = (
                '{}({})'.format(self.entries[parent], parent),
                '{}({})'.format(self.entries[child], child)
            )
            edges.append(e)

        edges: List[EdgeInput] = []
        # TODO: can be pruned to self.length // 2.
        for i in range(1, self.length):
            left, right = self._left(i), self._right(i)
            add_edge(i, left, edges)
            add_edge(i, right, edges)

        g = Graph.build('heap', edges, directed=False)
        g.view(pause=True)

    @classmethod
    def _parent(cls, index: int) -> int:
        # floor(n, 2)
        return index // 2

    @classmethod
    def _left(cls, index: int) -> int:
        return index * 2

    @classmethod
    def _right(cls, index: int) -> int:
        return (2 * index) + 1


def sort(values: List[int], reverse: bool = False) -> List[int]:
    """
    Sort the list using heap data structure
    """
    h = Heap(reverse)
    for v in values:
        h.insert(v)

    result = []
    while not h.empty():
        result.append(h.get())

    return result
