"""
Graph ADT
"""
import logging as log

from typing import Dict

# TODO: This should be a sibling package
from algo.graphs.vertex import Vertex


class Graph:
    """
    An abstract data type for representing Graphs.
    This implementation uses the adjacency list representation.
    """

    vertices: Dict[str, Vertex]
    num_vertices: int

    def __init__(self):
        """
        Create a graph instance based on adjacency list
        """
        self.vertices = {}
        self.num_vertices = 0

    def add_vertex(self, key: str) -> Vertex:
        """
        Add the given vertex to the Graph
        """
        assert len(key) > 0, "Invalid Vertex Key"
        assert key not in self.vertices, "Duplicate Vertex Key found"
        log.debug('Add vertex %s', key)
        self.num_vertices += 1
        result: Vertex = Vertex(key)
        self.vertices[key] = result
        return result

    def view(self):
        """
        Graphically represent the graph
        """
        # TODO: Update the implementation
        return None
