"""
Graph ADT
"""

import abc
import logging as log
import pdb

from typing import Collection, Dict, Iterable, Sequence, Set

# TODO: This should be a sibling package
from algo.graphs.builder import GraphBuilderMixin
from algo.graphs.edge import EdgeInput, Edge
from algo.graphs.igraph import IGraph
from algo.graphs.vertex import Vertex
from algo.graphs.visualizer import GraphViewMixin

from algo.utils.contracts import postcondition

__all__ = ['Graph']


class AbstractGraph(abc.ABC):
    """
    An abstract data type for representing Graphs.
    This implementation uses the adjacency list representation.
    """

    name: str
    directed: bool
    vertices: Dict[str, Vertex]
    num_vertices: int
    num_connect_components: int

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
        self.num_connect_components = 0

    @postcondition(lambda x: len(x) >= 0)
    def get_vertices(self) -> Collection[str]:
        """
        Return the collection of vertices in the given graph
        """
        return self.vertices.keys()

    def get_vertex(self, key: str) -> Vertex:
        """
        Return the vertex instance for this key
        """
        return self.vertices[key]

    def edges(self: IGraph) -> Collection[Edge]:
        """
        Return all the edges in this graph
        """
        result: Set[Edge] = set()
        for v in self:
            result.update(v.edges())

        return result

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

    def add_edge_str(self, source: str, dest: str, weight: int = 1):
        """
        Add Edge between the given vertices
        """

        assert source in self.vertices.keys(), "Source Vertex does not exist"
        assert dest in self.vertices.keys(), "Dest Vertex does not exist"

        src: Vertex = self.vertices[source]
        dst: Vertex = self.vertices[dest]
        return self.add_edge(src, dst, weight)

    def add_edge(self, source: Vertex, dest: Vertex, weight: int = 1):
        """
        Add Edge between given vertices
        """
        assert source in self.vertices.values(), "Source Vertex does not exist"
        assert dest in self.vertices.values(), "Dest Vertex does not exist"

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
            return source.weight(dest) > 0
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
                source.weight(dest) == dest.weight(source))

    def clear(self):
        """
        Clear the vertex state
        """
        log.debug('Clearing the state of graph %s', self.name)
        for v in self:
            v.clear()

    @classmethod
    def is_directed(cls, source: Vertex, dest: Vertex) -> bool:
        """
        Predicate to check if the edge between the vertices is directed
        """
        # return true if it's not undirected
        return not cls.is_undirected(source, dest)

    def __contains__(self, key: str) -> bool:
        """
        Returns true if the vertex is part of the Graph
        """
        return key in self.vertices

    def __iter__(self) -> Iterable[Vertex]:
        """
        Iterator for this instance
        """
        return iter(self.vertices.values())

    def view(self, pause: bool = False):
        """
        Visualize the graph and pause if required
        """
        self.visualize()
        if pause:
            pdb.set_trace()

    def transpose(self) -> IGraph:
        """
        Return the transpose of this graph.
        Does  not change the existing graph
        """
        assert isinstance(self, IGraph), "Instance not a graph"

        if not self.directed:
            # For an undirected graph, the
            # transpose is itself
            return self

        result: IGraph = self._create(
            'transposed {}'.format(self.name), self.directed)

        # Create vertices
        for v in self.get_vertices():
            result.add_vertex(v)

        # Create the edges
        for v in self.get_vertices():
            for e in self.get_vertex(v).edges():
                e = e.transpose()
                result.add_edge_str(e.source, e.dest, e.weight)

        return result

    @abc.abstractmethod
    def visualize(self):
        """
        Visualize this graph
        """

    @abc.abstractmethod
    def to_dot(self):
        """
        Return the Graphviz#dot representation
        """

    @classmethod
    def _create(cls, name: str, directed: bool):
        """
        Create a simple graph
        """
        # Creating a temporary method for solving typing issues
        # TODO: Later, see  if this can be fixed
        return cls(name, directed)

    @abc.abstractclassmethod
    def build(cls, name: str, edges: Sequence[EdgeInput], directed: bool) -> IGraph:
        """
        Construct a graph instance from the edges
        """

# Order of parents matter
# The first one always wins


class Graph(GraphViewMixin, GraphBuilderMixin, AbstractGraph):
    """
    A Concerte Graph Implementation
    """
