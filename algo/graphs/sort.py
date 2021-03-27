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
    # TODO: has_cycle should return a boolean
    has_cycle(graph)
    # do a Depth First Search (Forest style)
    dfs(graph)
    return sorted(graph, key=lambda v: v.finish, reverse=True)


def has_cycle(graph: IGraph) -> bool:
    """
    Check if the graph has a cycle
    """
    graph.set_helper(TraversalHelper(process_edge=raise_back_edge))
    return True


def raise_back_edge(source: Vertex, dest: Vertex, edge: EdgeContainer):
    """
    Check if the edge is a back edge
    """
    log.debug('Checking back edge in %s, %s, %s', source, dest, edge)
    if is_back_edge(source, dest):
        msg = 'Backend edge exists between {} and {}'.format(source, dest)
        raise Exception(msg)


def is_back_edge(_: Vertex, dest: Vertex) -> bool:
    """
    Check if the given edge is a backedge
    """
    return dest.get_state() == State.DISCOVERED
