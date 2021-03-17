"""
Mixin for building graphs.
Follows the builder pattern.
"""
import logging as log

from typing import Collection, Set, List, Type
from algo.graphs.edge import Edge
from algo.graphs.igraph import IGraph


# pylint: disable=too-few-public-methods
class GraphBuilderMixin:
    """
    Graph Builder Mixin
    """

    @classmethod
    def __vertices(cls, edges: Collection[Edge]) -> Set[str]:
        """
        Return the unique set of vertices from the edge list
        """
        result: Set[str] = set()
        for e in edges:
            result.add(e.source.capitalize())
            result.add(e.dest.capitalize())
        return result

    @classmethod
    def build(cls: Type[IGraph], name: str, lst: Collection[Edge], directed=False) -> IGraph:
        """
        Build a graph instance
        """
        assert len(lst) > 0, "Empty Edge list"

        # TODO: Fix lint error
        result: IGraph = cls(name, directed)
        edges: List[Edge] = Edge.make(lst)
        vertices: Set[str] = GraphBuilderMixin.__vertices(edges)

        # Add vertices
        for v in vertices:
            log.debug('Adding %s to Graph %s', v, result.name)
            result.add_vertex(v)

        # add edges
        for e in edges:
            src, dest, wg = e.source.capitalize(), e.dest.capitalize(), e.weight
            log.debug('Adding edge %s, %s with %s, %s',
                      src, dest, wg, directed)
            result.add_edge_str(src, dest, wg)
        return result
