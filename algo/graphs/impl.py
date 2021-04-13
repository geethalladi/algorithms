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

__all__ = ['has_cycle', 'is_bipartite']


class CycleError(ValueError):
    """
    Custom error for cycles
    """


class BipartiteError(ValueError):
    """
    Custom error for bipartite graphs
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
    return dest.state == State.DISCOVERED


def color_vertex(source: Vertex, dest: Vertex, edge: Edge):
    """
    Color the new vertex
    """
    # # this should be a new edge, seen for the first time
    # assert edge.state == State.UNDISCOVERED, f'{edge.state} is not UNDISCOVERED'

    if source.color is None:
        source.color = 'blue'

    if source.color == dest.color:
        msg = 'Neighbours with same color found {} and {}'.format(source, dest)
        raise BipartiteError(msg)

    dest.color = complement(source.color)
    return


def complement(color: str) -> str:
    """
    Return the complement of this color
    """
    assert color in ['blue', 'brown']

    if color == 'blue':
        return 'brown'
    return 'blue'


def is_bipartite(graph: IGraph, source: str = None) -> bool:
    """
    Returns true if the given graph is bipartite, if all
    the vertices can be colored with only two colors
    """
    try:
        # do a depth first forest search with the given hooks
        dfs(graph, source, Hooks(process_edge=color_vertex))
        return True
    except BipartiteError as exp:
        log.info('Not Bipartite: %s', exp)
        return False
