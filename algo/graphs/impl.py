"""
Graph Algorithm Implementations
"""
import logging as log

from algo.graphs.edge import Edge, EdgeType
from algo.graphs.igraph import IGraph
from algo.graphs.traversal import depth_first_search as dfs, classify_edge
from algo.graphs.traversal import Hooks
from algo.graphs.vertex import Vertex

__all__ = ['has_cycle', 'is_bipartite', 'edge_classifier']


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
    def raise_back_edge(source: Vertex, dest: Vertex, _: Edge):
        if classify_edge(source, dest) == EdgeType.BACK:
            msg = f'Backend edge exists between {source} and {dest}'
            raise CycleError(msg)

    try:
        # do a depth first forest search with the given hooks
        dfs(graph, None, Hooks(process_edge=raise_back_edge))
        return False
    except CycleError as exp:
        log.info('Cycle found: %s', exp)
        return True


def is_bipartite(graph: IGraph, source: str = None) -> bool:
    """
    Returns true if the given graph is bipartite, if all
    the vertices can be colored with only two colors
    """
    complement = {'blue': 'brown', 'brown': 'blue'}

    def color(source: Vertex, dest: Vertex, _: Edge):
        if source.color is None:
            source.color = 'blue'
        if source.color == dest.color:
            msg = f'Neighbours with same color found {source} and {dest}'
            raise BipartiteError(msg)
        dest.color = complement[source.color]

    try:
        # do a depth first forest search with the given hooks
        dfs(graph, source, Hooks(process_edge=color))
        return True
    except BipartiteError as exp:
        log.info('Not Bipartite: %s', exp)
        return False


def edge_classifier(graph: IGraph, start: str = None):
    """
    Classify all the edges in the given graph
    """

    def classifier(source: Vertex, dest: Vertex, edge: Edge):
        assert edge.type == EdgeType.UNKNOWN, f'Edge Type for {edge} is already known'

        result: EdgeType = classify_edge(source, dest)
        log.info('Edge %s is of type %s', edge, result)
        edge.type = result

    # Do the depth first search
    dfs(graph, start, hooks=Hooks(process_edge=classifier))
