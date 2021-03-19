"""
Vertex abstract data type
"""

import logging as log

from enum import Enum, auto, unique
from typing import Dict, Collection
from algo.utils.contracts import postcondition

log.basicConfig(level=log.INFO)


@unique
class State(Enum):
    """
    Vertex State Enum
    """
    UNDISCOVERED = auto()
    DISCOVERED = auto()
    PROCESSED = auto()

    def get_color(self):
        """
        Return the color associate with the State
        """
        if self is State.PROCESSED:
            return 'red'
        if self is State.DISCOVERED:
            return 'gray'
        # default to 'black'
        return 'black'


class Vertex:
    """
    Vertex using adjacency list representation
    """
    id: str
    state: State
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
        self.state = State.UNDISCOVERED
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

    def get_color(self):
        """
        Get the color of the graph
        """
        return self.get_state().get_color()

    @postcondition(lambda x: len(x) > 0)
    def __str__(self) -> str:
        """
        Return the string representation
        """
        return "{} -> {}".format(
            self.id,
            str([x.id for x in self.get_connections()]))
