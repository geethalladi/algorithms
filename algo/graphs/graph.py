"""
Graph ADT
"""

import logging as log

from typing import Dict, Collection, Iterable

# TODO: This should be a sibling package
from algo.graphs.vertex import Vertex
from algo.utils.contracts import postcondition

import graphviz


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

    def __create_dot_instance(self):
        """
        Factory method to create dot instance
        """
        if self.directed:
            log.info('Constructing a digraph instance for %s', self.name)
            return graphviz.Digraph(name=self.name, comment='Graph Visualization')

        log.info('Constructing a undirected graph instance for %s', self.name)
        return graphviz.Graph(name=self.name, comment='Graph Visualization')

    def __create_dot_representation(self):
        """
        Construct a dot representation of the entire graph
        """
        dot: graphviz.Graph = self.__create_dot_instance()
        self.__add_nodes(dot)
        self.__add_edges(dot)
        return dot

    def __add_nodes(self, dot: graphviz.Graph):
        """
        Add all the vertices to the dot representation
        """
        log.debug('Adding nodes to dot representation')
        for v in self.get_vertices():
            dot.node(v, v)

    def __should_add(self, source: Vertex, dest: Vertex):
        """
        Predicate to check if the edge needs to be added to the dot representation
        """
        if self.directed:
            # Always add if the graph is directed
            return True
        # If undirected add only once
        # add only from source to dest
        return (source.get_id() <= dest.get_id())

    def __add_edge(self, dot: graphviz.Graph, source: Vertex, dest: Vertex):
        """
        Add this edge detail to the dot representation
        """
        assert source is not None, "Source is empty"
        assert dest is not None, "Dest is empty"

        log.debug("Adding edge between %s and %s",
                  source.get_id(), dest.get_id())
        weight = source.get_weight(dest)
        dot.edge(source.get_id(), dest.get_id(), label=str(weight))

    def __add_edges_in(self, dot: graphviz.Graph, source: Vertex):
        """
        Add all the edges in the given vertex to the dot representation
        """
        log.debug('Adding edges in vertex %s', source.get_id())
        for dest in source.get_connections():
            if self.__should_add(source, dest):
                self.__add_edge(dot, source, dest)

    def __add_edges(self, dot: graphviz.Graph):
        log.debug('Adding edges to dot representation')
        for v in self.get_vertices():
            self.__add_edges_in(dot, self.vertices[v])

    def view(self):
        """
        Graphically represent the graph
        """
        dot: graphviz.Graph = self.__create_dot_representation()
        dot.save(filename='/tmp/test.gv')
        dot.view()
