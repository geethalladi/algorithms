"""
Graph Protocol
"""

from typing import Collection, Protocol, Sequence, runtime_checkable

from algo.graphs.edge import EdgeInput, Edge
from algo.graphs.vertex import Vertex

__all__ = ['IGraph']


@runtime_checkable
class IGraph(Protocol):
    """
    Graph Protocol
    """

    name: str
    directed: bool = False
    num_vertices: int = 0
    num_connect_components: int = 0

    def get_vertices(self) -> Collection[str]:
        """
        Return all the vertices of this graph
        """
        ...

    def get_vertex(self, key: str) -> Vertex:
        """
        Return the vertex for this key
        """
        ...

    def edges(self) -> Collection[Edge]:
        """
        Return all the edges in this graph
        """
        ...

    def add_vertex(self, key: str) -> Vertex:
        """
        Add vertex to this graph
        """
        ...

    def add_edge_str(self, source: str, dest: str,
                     weight: int):
        """
        Add this edge to the graph
        """
        ...

    def add_edge(self, source: Vertex, dest: Vertex,
                 weight: int):
        """
        Add this edge to the graph
        """
        ...

    def to_dot(self):
        """
        Convert the graph to dot representation
        """
        ...

    def clear(self):
        """
        Clear the state of the graph's vertices
        """
        ...

    def view(self, pause: bool):
        """
        Visualize this graph
        """
        ...

    def transpose(self) -> 'IGraph':
        """
        Transpose this graph and returns a new instance
        """
        ...

    def __iter__(self):
        """
        Iterable for IGraph
        """
        ...

    @classmethod
    def _create(cls, name: str, directed: bool) -> 'IGraph':
        """
        Create a single graph
        """
        ...

    @classmethod
    def build(cls, name: str, edges: Sequence[EdgeInput], directed: bool) -> 'IGraph':
        """
        Build a graph from the edges
        """
        ...
