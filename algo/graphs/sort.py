"""
Module to sort inside Graph
"""
import logging as log
from typing import Sequence

from algo.graphs.igraph import IGraph
from algo.graphs.state import State
from algo.graphs.traversal import depth_first_search as dfs
from algo.graphs.traversal_helper import TraversalHelper
from algo.graphs.vertex import Vertex, EdgeContainer

__all__ = ['topological_sort']


def topological_sort(graph: IGraph) -> Sequence[Vertex]:
    """
    Topological sorting of the graph
    """

    def check_cycle(source: Vertex, dest: Vertex, edge: EdgeContainer):
        log.info('Checking cycles in %s, %s, %s', source, dest, edge)
        if dest.get_state() == State.DISCOVERED:
            msg = 'Cycle exists between {} and {}'.format(source, dest)
            raise Exception(msg)

    graph.set_helper(TraversalHelper(process_edge=check_cycle))
    # do a Depth First Search (Forest style)
    dfs(graph)
    return sorted(graph, key=lambda v: v.finish, reverse=True)
