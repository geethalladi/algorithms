"""
Graph Protocol
"""

from typing import Collection, Protocol, runtime_checkable
from algo.graphs.vertex import Vertex
from algo.graphs.edge import Edge


@runtime_checkable
class IGraph(Protocol):
    """
    Graph Protocol
    """

    name: str
    directed: bool

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

    def view(self):
        """
        Visualize this graph
        """
        ...

    @classmethod
    def _create(cls, name: str, directed: bool) -> 'IGraph':
        """
        Create a single graph
        """
        ...

    @classmethod
    def build(cls, name: str, edges: Collection[Edge], directed: bool) -> 'IGraph':
        """
        Build a graph from the edges
        """
        ...
