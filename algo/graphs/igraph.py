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
    num_vertices: int
    num_connect_components: int

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

    def clear(self):
        """
        Clear the state of the graph's vertices
        """
        ...

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

    def stop_and_view(self):
        """
        Visualize this graph and stop execution
        """
        ...

    def dfs(self, start: str):
        """
        Do a depth first traversal of the graph
        from the given start node
        """
        ...

    def bfs(self, start: str):
        """
        Do a breadth first search based traversal
        from the given start node
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
