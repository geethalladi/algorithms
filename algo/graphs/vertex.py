"""
Vertex abstract data type
"""

import logging as log

from typing import Dict, Collection, NamedTuple
from algo.graphs.state import State
from algo.utils.contracts import postcondition

log.basicConfig(level=log.INFO)


class EdgeContainer(NamedTuple):
    """
    A Simple Container for holding edge details
    """
    # starting really simple
    # consciously avoiding direction for now
    # can be added if there is a requirement
    weight: int = 1
    state: State = State.UNDISCOVERED


class Vertex:
    """
    Vertex using adjacency list representation
    """
    id: str
    state: State
    distance: int
    parent: str
    discovery: int
    finish: int
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

    def get_description(self) -> str:
        """
        Get the vertex description
        """
        if self.discovery == 0 and self.finish == 0:
            return self.id

        return '{} ({}, {})'.format(self.id,
                                    self.discovery,
                                    self.finish)

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

        if not self.__should_add_edge(other, weight):
            return

        log.debug('Adding edge between %s and %s with weight %d, %s',
                  self.get_id(), other.get_id(), weight, directed)
        self.connected_to[other] = weight
        if not directed:
            # if undirected, add the other edge as well
            other.add_edge(self, weight, True)

    def __should_add_edge(self, other: 'Vertex', weight: int = 1):
        """
        Should this edge be added
        """
        if other not in self.connected_to:
            # edge does not exist
            return True

        # If it's already connected
        existing = (self.get_id(), other.get_id(), self.connected_to[other])
        given = (self.get_id(), other.get_id(), weight)

        # ASSUMPTION: Graph is either directed or undirected
        # and not a mixed bag and safely ignoring the other half
        if self.connected_to[other] == weight:
            log.debug('Ignoring redundant edge %s', existing)
            return False

        # If contradicting raise AssertionError
        msg = 'Conflicting Edge {} exists against {}'.format(existing, given)
        raise AssertionError(msg)

    def set_state(self, state: State):
        """
        Set the vertex state
        """
        self.state = state

    def get_state(self) -> State:
        """
        Get the state of the vertex
        """
        return self.state

    def set_parent(self, parent: 'Vertex', cost: int):
        """
        Set the parent and the distance
        """
        self.parent = parent.id
        self.distance = parent.distance + cost

    def get_color(self):
        """
        Get the color of the graph
        """
        return self.get_state().get_color()

    def __repr__(self):
        """
        Representation of Vertex instance
        """
        return self.id

    def __str__(self) -> str:
        """
        Return the string representation
        """
        return self.id
