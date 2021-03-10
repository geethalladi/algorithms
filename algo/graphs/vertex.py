"""
Vertex abstract data type
"""

from typing import Dict, List

import logging as log
log.basicConfig(level=log.INFO)


class Vertex:
    """
    Vertex using adjacency list representation
    """
    id: str
    connected_to: Dict[str, int]

    # TODO: How to qualify self here
    def __init__(self, key: str):
        """
        Initialize the Vertex instance
        """
        self.id = key
        self.connected_to = {}

    def get_id(self) -> str:
        """
        Return the identifier of this vertex
        """
        return self.id

    def get_connections(self) -> List[str]:
        """
        Get all the connected vertices
        """
        return self.connected_to.keys()

    def get_weight(self, other: str) -> int:
        """
        Return edge weight between this and the other vertex
        """
        return self.connected_to[other]

    def add_edge(self, other: 'Vertex', weight: int = 1,
                 directed: bool = False):
        """
        Add an edge between this and the given vertex
        """
        self.connected_to[other.get_id()] = weight
        if not directed:
            # if undirected, add the other edge as well
            other.add_edge(self, weight, True)
