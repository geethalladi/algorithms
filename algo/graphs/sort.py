"""
Module to sort inside Graph
"""
import logging as log
from typing import Sequence

from algo.graphs.igraph import IGraph
from algo.graphs.impl import has_cycle
from algo.graphs.traversal import depth_first_search as dfs
from algo.graphs.vertex import Vertex

__all__ = ['topological_sort']


def topological_sort(graph: IGraph) -> Sequence[Vertex]:
    """
    Topological sorting of the graph
    """
    if has_cycle(graph):
        log.info('Graph %s has a cycle. TopoSort not possible', graph)
        return []
    # do a Depth First Search (Forest style)
    dfs(graph)
    return sorted(graph, key=lambda v: v.finish, reverse=True)
