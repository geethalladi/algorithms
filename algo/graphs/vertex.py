"""
Vertex abstract data type
"""

import logging as log

from typing import Dict, Collection

from algo.graphs.edge import Edge
from algo.graphs.state import State
from algo.utils.contracts import postcondition

# log.basicConfig(level=log.INFO)

__all__ = ['Vertex']


class Vertex:
    """
    Vertex using adjacency list representation
    """
    id: str
    state: State
    distance: int
    parent: 'Vertex'
    discovery: int
    finish: int
    connected_to: Dict['Vertex', Edge]

    def __init__(self, key: str):
        """
        Initialize the Vertex instance
        """
        # removing isinstance as the type check is
        # done already by the linter
        assert (len(key) > 0), "Invalid Vertex Key"
        log.debug('Creating vertex with key %s', key)
        self.id = key
        self.connected_to = {}
        self.clear()

    def clear(self):
        """
        Clear the state of this vertex
        """
        log.debug('Clearing the state of vertex %s', self.id)
        self.state = State.UNDISCOVERED
        self.distance = 0
        self.parent = None
        # Setting the discovery / finish time to 0
        self.discovery = 0
        self.finish = 0
        # clear the contents of the edge
        for e in self.edges():
            e.clear()

    @postcondition(lambda result: len(result) >= 0)
    def neighbours(self) -> Collection['Vertex']:
        """
        Get all the connected vertices
        """
        return self.connected_to.keys()

    def edges(self) -> Collection[Edge]:
        """
        Get all the edges starting from this vertex
        """
        return self.connected_to.values()

    def edge(self, other: 'Vertex') -> Edge:
        """
        Return the edge instance associated with the given vertex
        """
        return self.connected_to[other]

    def weight(self, other: 'Vertex') -> int:
        """
        Return edge weight between this and the other vertex
        """
        return self.edge(other).weight

    def add_edge(self, other: 'Vertex', weight: int = 1,
                 directed: bool = False):
        """
        Add an edge between this and the given vertex
        """
        assert weight > 0, "Invalid edge weight"

        if not self.__should_add_edge(other, weight):
            return

        log.debug('Adding edge between %s and %s with weight %d, %s',
                  self.id, other.id, weight, directed)

        edge: Edge = Edge(self.id, other.id, weight, directed)
        self.connected_to[other] = edge

        # if undirected, use the same edge container
        if not directed:
            # the other is also an instance of vertex
            # and this is fine
            # pylint: disable=protected-access
            other.__add_edge(self, edge, directed)

    def __add_edge(self, other: 'Vertex', edge: Edge, directed: bool):
        """
        Private function for adding Edge
        """
        assert not directed, 'Adding edge container instance for a directed graph'

        if not self.__should_add_edge(other, edge.weight):
            return

        # Sharing the same edge instance in case of
        # an undirected graph
        self.connected_to[other] = edge

    def __should_add_edge(self, other: 'Vertex', weight: int = 1):
        """
        Should this edge be added
        """
        if other not in self.connected_to:
            # edge does not exist
            return True

        # If it's already connected
        existing = (self.id, other.id, self.connected_to[other])
        given = (self.id, other.id, weight)

        # ASSUMPTION: Graph is either directed or undirected
        # and not a mixed bag and safely ignoring the other half
        if self.connected_to[other].weight == weight:
            log.debug('Ignoring redundant edge %s', existing)
            return False

        # If contradicting raise AssertionError
        msg = 'Conflicting Edge {} exists against {}'.format(existing, given)
        raise AssertionError(msg)

    def is_processed(self):
        """
        Has the vertex been processed already
        """
        return self.state == State.PROCESSED

    def set_parent(self, parent: 'Vertex', edge: Edge):
        """
        Set the parent and the distance
        """
        assert edge, 'Edge Reference is missing while setting parent'

        self.parent = parent
        self.distance = parent.distance + edge.weight

    def __str__(self) -> str:
        """
        Return the string representation
        """
        if self.discovery == 0 and self.finish == 0:
            return self.id

        return '{} ({}, {})'.format(self.id,
                                    self.discovery,
                                    self.finish)
