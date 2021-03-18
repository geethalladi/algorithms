"""
Vertex abstract data type
"""

import logging as log

from typing import Dict, Collection
from algo.utils.contracts import postcondition

log.basicConfig(level=log.INFO)


class Vertex:
    """
    Vertex using adjacency list representation
    """
    id: str
    visited: bool
    connected_to: Dict['Vertex', int]

    def __init__(self, key: str):
        """
        Initialize the Vertex instance
        """
        # removing isinstance as the type check is
        # done already by the linter
        assert (len(key) > 0), "Invalid Vertex Key"
        log.debug('Creating vertex with key %s', key)
        self.id = key
        self.visited = False
        self.connected_to = {}

    def get_id(self) -> str:
        """
        Return the identifier of this vertex
        """
        return self.id

    @postcondition(lambda result: len(result) >= 0)
    def get_connections(self) -> Collection['Vertex']:
        """
        Get all the connected vertices
        """
        return self.connected_to.keys()

    def get_weight(self, other: 'Vertex') -> int:
        """
        Return edge weight between this and the other vertex
        """
        return self.connected_to[other]

    def add_edge(self, other: 'Vertex', weight: int = 1,
                 directed: bool = False):
        """
        Add an edge between this and the given vertex
        """
        assert weight > 0, "Invalid edge weight"
        assert other not in self.connected_to, "Edge already exists"

        log.debug('Adding edge between %s and %s with weight %d, %s',
                  self.get_id(), other.get_id(), weight, directed)
        self.connected_to[other] = weight
        if not directed:
            # if undirected, add the other edge as well
            other.add_edge(self, weight, True)

    def set_visited(self, flag: bool):
        """
        Set the node as visited
        """
        self.visited = flag

    def is_visited(self) -> bool:
        """
        Return True, if the node has been visited
        """
        return self.visited

    def get_color(self):
        """
        Get the color of the graph
        """
        if self.is_visited():
            return 'red'
        return 'black'

    @postcondition(lambda x: len(x) > 0)
    def __str__(self) -> str:
        """
        Return the string representation
        """
        return "{} -> {}".format(
            self.id,
            str([x.id for x in self.get_connections()]))
