"""
Graph Algorithm Implementations
"""
import logging as log

from algo.graphs.edge import Edge
from algo.graphs.igraph import IGraph
from algo.graphs.state import State
from algo.graphs.traversal import depth_first_search as dfs
from algo.graphs.traversal import Hooks
from algo.graphs.vertex import Vertex

__all__ = ['has_cycle']


class CycleError(ValueError):
    """
    Custom error for cycles
    """


def has_cycle(graph: IGraph) -> bool:
    """
    Check if the graph has a cycle
    """
    try:
        # do a depth first forest search with the given hooks
        dfs(graph, None, Hooks(process_edge=raise_back_edge))
        return False
    except CycleError as exp:
        log.info('Cycle found: %s', exp)
        return True


def raise_back_edge(source: Vertex, dest: Vertex, edge: Edge):
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
