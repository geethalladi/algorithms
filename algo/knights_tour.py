"""
Generate a knight's tour for the given n x n chess board
"""
import logging as log

from typing import NamedTuple, List, Sequence, Set, Tuple

from algo.graphs.edge import Edge
from algo.graphs.graph import Graph
from algo.graphs.igraph import IGraph


class Position(NamedTuple):
    """
    Abstract Type for Position
    """
    x: int
    y: int

    def __repr__(self):
        return str(self)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def displace(self, other: 'Position'):
        """
        Returns a new displaced Position
        """
        return Position(self.x + other.x,
                        self.y + other.y)

    def within_grid(self, top_right: 'Position',
                    bottom_left: 'Position' = None):
        """
        Check if this position occurs within the specified grid
        """
        if not bottom_left:
            # Use origin if bottom_left is not specified
            bottom_left = Position(0, 0)

        return (bottom_left.x <= self.x <= top_right.x) and (
            bottom_left.y <= self.y <= top_right.y)


# declaring a type for neighbour
Neighbour = Tuple[Position, Position]


def knights_tour(size: int) -> Sequence[Position]:
    """
    Generate the knights tour for the n x n
    chess board, starting at (0,0)
    """
    assert (size > 0), "Invalid size given"

    log.info('Generating knights tour of size, %s', size)
    graph: IGraph = __create_knights_tour_graph(size)
    graph.view()
    return __generate_a_tour(graph)


def __create_knights_tour_graph(size: int) -> IGraph:
    """
    Generate a graph for the knight's tour of the given
    dimension. The Graph should have n * n nodes. Every
    valid knight's move from a position (x, y) should be
    connected via an edge
    """
    log.info('Creating KT Graph of size %s', size)

    neighbours: Set[Neighbour] = set()
    for i in range(0, size):
        for j in range(0, size):
            neighbours.update(__create_edges_for(Position(i, j), size))

    edges: List[Edge] = [Edge(str(p1), str(p2)) for (p1, p2) in neighbours]

    log.info('Created edge set of size %s', len(neighbours))
    log.info('Edge list %s', edges)
    return Graph.build('Knights Tour {}'.format(size),
                       edges,
                       directed=False)


def __create_edges_for(pos: Position, size: int) -> Set[Neighbour]:
    log.info('Creating neighbours for %s inside board of size %s', pos, size)
    possiblities = {
        (-2, -1), (-2, 1),
        (2, -1), (2, 1),
        (-1, -2), (-1, 2),
        (1, -2), (1, 2)
    }
    grid: Position = Position(size - 1, size - 1)

    result: Set[Neighbour] = set()
    for p in possiblities:
        other = pos.displace(Position(*p))
        if not other.within_grid(grid):
            # Leave it if it falls outside
            continue
        # if pos > other:
        #     # Always the left end of the edge
        #     # should be greater, to avoid
        #     # duplicate edges
        #     other, pos = pos, other

        result.add((pos, other))

    log.info('Result is %s', result)
    return result


def __generate_a_tour(graph: IGraph) -> Sequence[Position]:
    """
    Given a graph with knight's positions as neighbour,
    generate a possible tour starting at (0,0)
    """
    log.info('Generating a tour from %s', graph.name)
    return []
