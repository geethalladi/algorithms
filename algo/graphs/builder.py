"""
Mixin for building graphs.
Follows the builder pattern.
"""
import logging as log

from typing import List, Sequence, Set, Type

from algo.graphs.edge import EdgeInput
from algo.graphs.igraph import IGraph

__all__ = ['GraphBuilderMixin']


class GraphBuilderMixin:  # pylint: disable=too-few-public-methods
    """
    Graph Builder Mixin
    """

    @classmethod
    def __vertices(cls, edges: Sequence[EdgeInput]) -> Set[str]:
        """
        Return the unique set of vertices from the edge list
        """
        result: Set[str] = set()
        for e in edges:
            result.add(e.source.capitalize())
            result.add(e.dest.capitalize())
        return result

    @classmethod
    def build(cls: Type[IGraph], name: str, lst: Sequence[EdgeInput], directed=False) -> IGraph:
        """
        Build a graph instance
        """
        assert len(lst) > 0, "Empty Edge list"

        result: IGraph = cls._create(name, directed)
        edges: List[EdgeInput] = EdgeInput.make(lst)
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
