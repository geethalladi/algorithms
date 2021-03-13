"""
Mixin for building graphs.
Follows the builder pattern.
"""
import logging as log

from typing import Collection, Set
from algo.graphs.edge import Edge
from algo.graphs.igraph import IGraph


class GraphBuilderMixin:
    """
    Graph Builder Mixin
    """

    @classmethod
    def get_vertices(cls, edges: Collection[Edge]) -> Set[str]:
        """
        Return the unique set of vertices from the edge list
        """
        result: Set[str] = set()
        for e in edges:
            e = Edge._make(e)
            result.add(e.source.capitalize())
            result.add(e.dest.capitalize())
        return result

    # def add_vertices(cls, g: IGraph, vertices: Set[str]):

    # def add_edges(cls, g: IGraph, edges: Collection[Edge]):
    #     """
    #     Add all edges to the graph instance
    #     """

    def build(self: IGraph, edges: Collection[Edge]):
        """
        Build a graph instance
        """
        vertices: Set[str] = GraphBuilderMixin.get_vertices(edges)
        # Add vertices
        for v in vertices:
            self.add_vertex(v)

        # add edges
        for e in edges:
            e = Edge._make(e)
            self.add_edge_str(e.source.capitalize(),
                              e.dest.capitalize(),
                              e.weight)
