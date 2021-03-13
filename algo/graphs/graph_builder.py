"""
Mixin for building graphs.
Follows the builder pattern.
"""
import logging as log

from typing import Collection, Set, List
from algo.graphs.edge import Edge
from algo.graphs.igraph import IGraph


class GraphBuilderMixin:
    """
    Graph Builder Mixin
    """

    @classmethod
    def parse_vertices(cls, edges: Collection[Edge]) -> Set[str]:
        """
        Return the unique set of vertices from the edge list
        """
        result: Set[str] = set()
        for e in edges:
            result.add(e.source.capitalize())
            result.add(e.dest.capitalize())
        return result

    def build(self: IGraph, lst: Collection[Edge]) -> IGraph:
        """
        Build a graph instance
        """
        assert len(lst) > 0, "Empty Edge list"

        edges: List[Edge] = Edge.make(lst)
        vertices: Set[str] = GraphBuilderMixin.parse_vertices(edges)

        # Add vertices
        for v in vertices:
            log.debug('Adding %s to Graph %s', v, self.name)
            self.add_vertex(v)

        # add edges
        for e in edges:
            src, dest, wg = e.source.capitalize(), e.dest.capitalize(), e.weight
            log.debug('Adding edge %s, %s with %s, %s',
                      src, dest, wg, self.directed)
            self.add_edge_str(src, dest, wg)
        return self
