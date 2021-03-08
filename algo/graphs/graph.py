"""
Graph ADT
"""
from typing import Dict

# TODO: This should be a sibling package
from algo.graphs.vertex import Vertex


class Graph:
    """
    An abstract data type for representing Graphs.
    This implementation uses the adjacency list representation.
    """

    def __init__(self):
        """
        Create a graph instance based on adjacency list
        """
        self.vertices: Dict[id, Vertex] = {}
        self.num_vertices: int = 0

    def view(self):
        """
        Graphically represent the graph
        """
        # TODO: Update the implementation
        return None

    def add_vertex(self, key: str):
        """
        Add the given vertex to the Graph
        """
        # TODO: Adding Vertex
        return None
