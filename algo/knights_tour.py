"""
Generate a knight's tour for the given n x n chess board
"""
import logging as log

from typing import NamedTuple, Sequence, Set

from algo.graphs.edge import Edge
from algo.graphs.graph import Graph
from algo.graphs.igraph import IGraph


class Position(NamedTuple):
    """
    Abstract Type for Position
    """
    x: int
    y: int

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)


def knights_tour(size: int) -> Sequence[Position]:
    """
    Generate the knights tour for the n x n
    chess board, starting at (0,0)
    """
    log.info('Generating knights tour of size, %s', size)
    graph: IGraph = __create_knights_tour_graph(size)
    return __generate_a_tour(graph)


def __create_knights_tour_graph(size: int) -> IGraph:
    """
    Generate a graph for the knight's tour of the given
    dimension. The Graph should have n * n nodes. Every
    valid knight's move from a position (x, y) should be
    connected via an edge
    """
    edges: Set[Edge] = set()
    for i in range(0, size):
        for j in range(0, size):
            edges.update(__create_edges_for(Position(i, j), size))

    return Graph.build('Knights Tour {}'.format(size),
                       edges,
                       directed=False)


def __create_edges_for(pos: Position, size: int) -> Set[Edge]:
    log.info('Creating neighbours for %s inside board of size %s', pos, size)
    return set()


def __generate_a_tour(graph: IGraph) -> Sequence[Position]:
    """
    Given a graph with knight's positions as neighbour,
    generate a possible tour starting at (0,0)
    """
    log.info('Generating a tour from %s', graph.name)
    return []
