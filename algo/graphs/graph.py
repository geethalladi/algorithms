"""
Graph ADT
"""
import logging as log

from typing import Dict, Collection, Iterable

# TODO: This should be a sibling package
from algo.graphs.vertex import Vertex
from algo.utils.contracts import postcondition


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

    @postcondition(lambda x: len(x) >= 0)
    def get_vertices(self) -> Collection[str]:
        """
        Return the collection of vertices in the given graph
        """
        return self.vertices.keys()

    @postcondition(lambda x: x is not None)
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

    def add_edge_str(self, source: str, dest: str,
                     weight: int = 1, directed: bool = False):
        """
        Add Edge between the given vertices
        """

        assert source in self.vertices.keys(), "Source Vertex does not exist"
        assert dest in self.vertices.keys(), "Dest Vertex does not exist"
        src: Vertex = self.vertices[source]
        dst: Vertex = self.vertices[dest]
        return self.add_edge(src, dst, weight, directed)

    def add_edge(self, source: Vertex, dest: Vertex,
                 weight: int = 1, directed: bool = False):
        """
        Add Edge between given vertices
        """
        assert source in self.vertices.values(), "Source Vertex does not exist"
        assert dest in self.vertices.values(), "Dest Vertex does not exist"

        log.debug("Adding edge between %s and %s with %s, %s",
                  source, dest, weight, directed)
        return source.add_edge(dest, weight, directed)

    def __iter__(self) -> Iterable[Vertex]:
        """
        Iterator for this instance
        """
        return iter(self.vertices.values())

    def view(self):
        """
        Graphically represent the graph
        """
        # TODO: Update the implementation
        return None
