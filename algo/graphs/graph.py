"""
Graph ADT
"""

import logging as log

# TODO: This should be a sibling package
from algo.graphs.vertex import Vertex
from algo.graphs.graph_view import GraphViewMixin
from algo.graphs.graph_builder import GraphBuilderMixin
from algo.utils.contracts import postcondition

from typing import Dict, Collection, Iterable


class Graph:
    """
    An abstract data type for representing Graphs.
    This implementation uses the adjacency list representation.
    """

    name: str
    directed: bool
    vertices: Dict[str, Vertex]
    num_vertices: int

    def __init__(self, name: str, directed: bool = False):
        """
        Create a graph instance based on adjacency list
        """
        assert len(name) >= 0

        log.debug("Creating graph %s", name)
        self.name = name
        self.directed = directed
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
                     weight: int = 1, directed: bool = None):
        """
        Add Edge between the given vertices
        """

        assert source in self.vertices.keys(), "Source Vertex does not exist"
        assert dest in self.vertices.keys(), "Dest Vertex does not exist"

        if directed is None:
            directed = self.directed

        src: Vertex = self.vertices[source]
        dst: Vertex = self.vertices[dest]
        return self.add_edge(src, dst, weight, directed)

    def add_edge(self, source: Vertex, dest: Vertex,
                 weight: int = 1, directed: bool = None):
        """
        Add Edge between given vertices
        """
        assert source in self.vertices.values(), "Source Vertex does not exist"
        assert dest in self.vertices.values(), "Dest Vertex does not exist"

        if directed is None:
            directed = self.directed

        log.debug("Adding edge between %s and %s with %s, %s",
                  source, dest, weight, directed)
        return source.add_edge(dest, weight, directed)

    @classmethod
    def is_connected(cls, source: Vertex, dest: Vertex) -> bool:
        """
        Predicate to check if the two vertices are connected
        """
        assert source is not None, "Source is empty"
        assert dest is not None, "Dest is empty"
        try:
            return source.get_weight(dest) > 0
        except KeyError:
            return False

    @classmethod
    def is_undirected(cls, source: Vertex, dest: Vertex) -> bool:
        """
        Returns true if the edge is undirected
        """
        assert source is not None, "Source is empty"
        assert dest is not None, "Dest is empty"

        # source and dest should be connected from both directions
        # their weights should also match
        # return true if all the conditions are satisfied

        return (cls.is_connected(source, dest) and
                cls.is_connected(dest, source) and
                source.get_weight(dest) == dest.get_weight(source))

    @classmethod
    def is_directed(cls, source: Vertex, dest: Vertex) -> bool:
        """
        Predicate to check if the edge between the vertices is directed
        """
        # return true if it's not undirected
        return not cls.is_undirected(source, dest)

    def __iter__(self) -> Iterable[Vertex]:
        """
        Iterator for this instance
        """
        return iter(self.vertices.values())


class ConcreteGraph(Graph, GraphViewMixin, GraphBuilderMixin):
    """
    A Concerte Graph Implementation
    """
    pass
