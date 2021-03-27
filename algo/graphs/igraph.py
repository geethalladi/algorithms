"""
Graph Protocol
"""

from typing import Collection, Protocol, runtime_checkable

from algo.graphs.edge import Edge
from algo.graphs.vertex import Vertex


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

    # TODO: not required
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

    # TODO: not required
    def view(self):
        """
        Visualize this graph
        """
        ...

    def __iter__(self):
        """
        Iterable for IGraph
        """
        ...

    # TODO: not required
    def stop_and_view(self):
        """
        Visualize this graph and stop execution
        """
        ...

    @classmethod
    def _create(cls, name: str, directed: bool) -> 'IGraph':
        """
        Create a single graph
        """
        ...

    # TODO: not required
    @classmethod
    def build(cls, name: str, edges: Collection[Edge], directed: bool) -> 'IGraph':
        """
        Build a graph from the edges
        """
        ...
