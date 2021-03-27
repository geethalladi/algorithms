"""
Graph Algorithm Implementations
"""
import logging as log

from algo.graphs.igraph import IGraph
from algo.graphs.state import State
from algo.graphs.traversal import depth_first_search as dfs
from algo.graphs.traversal_helper import TraversalHelper
from algo.graphs.vertex import Vertex, EdgeContainer

__all__ = ['has_cycle']


class CycleError(ValueError):
    """
    Custom error for cycles
    """


def has_cycle(graph: IGraph) -> bool:
    """
    Check if the graph has a cycle
    """
    graph.set_helper(TraversalHelper(process_edge=raise_back_edge))
    try:
        dfs(graph)
    except CycleError as exp:
        log.info('Cycle found: %s', exp)
        return True
    finally:
        # clear the helper
        graph.set_helper(TraversalHelper())
    return False


def raise_back_edge(source: Vertex, dest: Vertex, edge: EdgeContainer):
    """
    Check if the edge is a back edge
    """
    log.debug('Checking back edge in %s, %s, %s', source, dest, edge)
    if is_back_edge(source, dest):
        msg = 'Backend edge exists between {} and {}'.format(source, dest)
        raise CycleError(msg)


def is_back_edge(_: Vertex, dest: Vertex) -> bool:
    """
    Check if the given edge is a backedge
    """
    return dest.get_state() == State.DISCOVERED
