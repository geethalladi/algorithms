"""
Priority Queue Implementation
"""

import logging as log

from dataclasses import dataclass
from typing import Dict, Generic, List, Optional, Tuple, TypeVar

from algo.graphs.edge import EdgeInput
from algo.graphs.graph import Graph


__all__ = ['PriorityQueue']

T = TypeVar('T')  # pylint: disable=invalid-name


@dataclass
class Container(Generic[T]):
    """
    Creating a container class
    """
    identity: str
    priority: int
    task: Optional[T]
    position: int = -1

    def __str__(self):
        return '[{}, {}, {}, {}]'.format(self.identity,
                                         self.priority,
                                         self.position,
                                         self.task)


class PriorityQueue(Generic[T]):
    """
    Priority Queue storing elements of type  T
    """

    entries: List[Container]
    map: Dict[str, Container]
    size: int

    def __init__(self, reverse=False):
        self.entries = []
        self.size = 0
        # by default return the task
        # with the highest priority
        self.reverse = reverse
        self.map = {}

    def insert(self, identity: str, priority: int, task: Optional[T] = None):
        """
        Insert the element with the given priority
        """
        assert identity not in self.map, 'Task with id {} already exists'.format(
            identity)
        c: Container = Container(identity, priority, task)
        log.info('Inserting %s', c)
        # add it to the map
        self.map[identity] = c

        if self.size == 0:
            # dummy addition
            # done for 1 based index
            self.entries.append(c)

        # maintain the left most tree property
        self.entries.append(c)
        self.size += 1
        self._bubble_up(self.size)

    def get(self) -> Tuple[str, Optional[T]]:
        """
        Return the task with the highest priority
        """
        assert not self.empty(), 'PQ is empty'
        # self.visualize()

        self._swap(1, self.size)
        result: Container = self.entries.pop(self.size)
        self.size -= 1
        self.map.pop(result.identity)

        if self.size != 0:
            # skip empty heap
            self._bubble_down(1)

        return (result.identity, result.task)

    def update(self, identity: str, new_priority: int):
        """
        Update the priority of an existing element
        """
        assert identity in self.map, 'Entity with id {} does not exist'.format(
            identity)

        c: Container = self.map[identity]
        old, c.priority = c.priority, new_priority

        if self._is_dominant_value(new_priority, old):
            # new priority is more dominant
            self._bubble_up(c.position)
        else:
            # priority has come down
            self._bubble_down(c.position)

    def _bubble_down(self, pos: int):
        log.info('Bubbling downwards from %s', pos)
        # find the dominant among its children
        index: int = self._find_dominant(pos)

        if index == pos:
            # parent is more dominant than its children
            return
        self._swap(pos, index)
        self._bubble_down(index)

    def _find_dominant(self, pos: int):
        assert self._valid(pos), 'Invalid position {}'.format(pos)

        result: int = pos
        for child in [self._left(pos), self._right(pos)]:
            # if child exists and is dominant
            if self._valid(child) and self._is_dominant(child, result):
                result = child

        return result

    def _bubble_up(self, pos: int):
        if pos == 1:
            # done with bubbling up
            return

        log.info('Bubbling upwards from %s', pos)
        parent = self._parent(pos)
        if self._is_dominant(pos, parent):
            # if the child dominates its parent
            self._swap(pos, parent)
            self._bubble_up(parent)

    def _swap(self, i: int, j: int):
        assert self._valid(i), 'Invalid index {}'.format(i)
        assert self._valid(j), 'Invalid inddex {}'.format(j)

        self.entries[j], self.entries[i] = self.entries[i], self.entries[j]

        # Update the position
        self.entries[j].position = j
        self.entries[i].position = i

    def _is_dominant(self, i: int, j: int):
        assert self._valid(i), 'Invalid index {}'.format(i)
        assert self._valid(j), 'Invalid inddex {}'.format(j)

        x, y = self.entries[i].priority, self.entries[j].priority
        return self._is_dominant_value(x, y)

    def _is_dominant_value(self, x: int, y: int) -> bool:  # pylint: disable=invalid-name
        if self.reverse:
            # look for a lower priority
            return x < y
        # default, the one with the highest priority wins
        return x > y

    def empty(self):
        """
        Check if the PQ is empty
        """
        return self.size <= 0

    def _valid(self, pos: int):
        return 1 <= pos <= self.size

    @classmethod
    def _parent(cls, pos: int):
        return pos // 2

    @classmethod
    def _left(cls, pos: int):
        return pos * 2

    @classmethod
    def _right(cls, pos: int):
        return (pos * 2) + 1

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
        # TODO: can be pruned to self.length // 2.
        for i in range(1, self.size):
            left, right = self._left(i), self._right(i)
            add_edge(i, left, edges)
            add_edge(i, right, edges)

        g = Graph.build('heap', edges, directed=False)
        g.view(pause=True)
