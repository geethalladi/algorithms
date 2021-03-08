"""
Vertex abstract data type
"""

from typing import Dict

import logging as log
log.basicConfig(level=log.INFO)


class Vertex:
    """
    Vertex using adjacency list representation
    """
    _id: str
    _connected_to: Dict[str, int]

    # TODO: How to qualify self here
    def __init__(self, key: str):
        """
        Initialize the Vertex instance
        """
        self._id = key
        self._connected_to = {}

    def get_id(self) -> str:
        """
        Return the identifier of this vertex
        """
        return self._id

    def add_edge(self, other: 'Vertex', weight: int = 1,
                 directed: bool = False):
        """
        Add an edge between this and the given vertex
        """
        self._connected_to[other.get_id()] = weight
        if not directed:
            # if undirected, add the other edge as well
            other.add_edge(self, weight, True)
