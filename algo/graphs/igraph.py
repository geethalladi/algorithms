"""
Graph Protocol
"""

from typing import Collection, Protocol, runtime_checkable
from algo.graphs.vertex import Vertex


@runtime_checkable
class IGraph(Protocol):
    """
    Graph Protocol
    """
    directed: bool

    def get_vertices(self) -> Collection[str]:
        """
        Return all the vertices of this graph
        """
        ...

    def add_vertex(self, key: str) -> Vertex:
        """
        Add vertex to this graph
        """
        ...

    def add_edge_str(self, source: str, dest: str,
                     weight: int, directed: bool):
        """
        Add this edge to the graph
        """
        ...

    def add_edge(self, source: Vertex, dest: Vertex,
                 weight: int, directed: bool):
        """
        Add this edge to the graph
        """
        ...
