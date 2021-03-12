"""
Vertex abstract data type
"""

import logging as log

from typing import Dict, Collection

log.basicConfig(level=log.INFO)


def non_empty_colletion(lst):
    """
    Assert if the collection is empty
    """
    assert len(lst) > 0, "Collection is empty"


def positive_number(num):
    """
    Assert if the number is positive
    """
    assert num > 0, "Number is expected to be positive"


class Vertex:
    """
    Vertex using adjacency list representation
    """
    id: str
    connected_to: Dict['Vertex', int]

    def __init__(self, key: str):
        """
        Initialize the Vertex instance
        """
        # removing isinstance as the type check is
        # done already by the linter
        assert (len(key) > 0), "Invalid Vertex Key"
        self.id = key
        self.connected_to = {}

    def get_id(self) -> str:
        """
        Return the identifier of this vertex
        """
        return self.id

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
        assert (weight > 0), "Invalid edge weight"
        self.connected_to[other] = weight
        if not directed:
            # if undirected, add the other edge as well
            other.add_edge(self, weight, True)

    def __str__(self) -> str:
        """
        Return the string representation
        """
        return "{} -> {}".format(
            self.id,
            str([x.id for x in self.get_connections()]))
