"""
Generate a knight's tour for the given n x n chess board
"""
import logging as log

from typing import NamedTuple, List, Sequence, Tuple

from algo.graphs.edge import Edge
from algo.graphs.graph import Graph
from algo.graphs.igraph import IGraph
from algo.graphs.vertex import Vertex, State


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


def is_neighbour(pos1: Position, pos2: Position) -> bool:
    """
    Check if the two given positions are neighbouring
    """
    dx: int = abs(pos1.x - pos1.y)
    dy: int = abs(pos1.y - pos2.y)

    return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)


def knights_tour(size: int) -> Sequence[str]:
    """
    Generate the knights tour for the n x n
    chess board, starting at (0,0)
    """
    assert (size > 0), "Invalid size given"

    log.info('Generating knights tour of size, %s', size)
    graph: IGraph = __create_knights_tour_graph(size)
    vertices: Sequence[Vertex] = __generate_a_tour(graph, size)
    return [v.id for v in vertices]


def __create_knights_tour_graph(size: int) -> IGraph:
    """
    Generate a graph for the knight's tour of the given
    dimension. The Graph should have n * n nodes. Every
    valid knight's move from a position (x, y) should be
    connected via an edge
    """
    log.info('Creating KT Graph of size %s', size)

    neighbours: List[Neighbour] = []
    for i in range(0, size):
        for j in range(0, size):
            neighbours.extend(__get_neighbours(Position(i, j), size))

    edges: List[Edge] = [Edge(str(p1), str(p2)) for (p1, p2) in neighbours]

    log.info('Created edge set of size %s', len(edges))
    log.debug('Edge list %s', edges)
    return Graph.build('Knights_Tour_{}'.format(size), edges, directed=False)


def __get_neighbours(pos: Position, size: int) -> List[Neighbour]:
    """
    Get the valid neighbours for the given position
    """

    log.debug('Creating neighbours for %s inside board of size %s', pos, size)
    possiblities = {(-2, -1), (-2, 1), (2, -1), (2, 1),
                    (-1, -2), (-1, 2), (1, -2), (1, 2)}
    grid: Position = Position(size - 1, size - 1)

    result: List[Neighbour] = []
    for p in possiblities:
        other = pos.displace(Position(*p))
        # Leave it if it falls outside
        if other.within_grid(grid):
            result.append((pos, other))

    log.debug('Result is %s', result)
    return result


def __start_position(size: int) -> Position:
    return Position(0, 0)


def __generate_a_tour(graph: IGraph, size: int) -> List[Vertex]:
    """
    Given a graph with knight's positions as neighbour,
    generate a possible tour starting at (0,0)
    """
    log.info('Generating a tour from %s', graph.name)
    graph.clear()
    start: Vertex = graph.get_vertex(str(__start_position(size)))
    return KT(graph, size * size).tour(start)


class KT:
    graph: IGraph
    size: int
    path: List[Vertex]
    completed: int
    view_count: int

    def __init__(self, graph: IGraph, size: int):
        self.graph = graph
        self.size = size
        self.clear()

    def clear(self):
        self.path = []
        self.completed = 0
        self.view_count = 0

    def push_to_path(self, v: Vertex):
        """
        Add it to the top of the Stack
        """
        v.set_state(State.PROCESSED)
        self.path.append(v)
        self.completed = len(self.path)

    def pop_from_path(self):
        """
        Pop the vertex at the top of the Stack
        """
        v: Vertex = self.path.pop()
        self.completed = len(self.path)
        v.set_state(State.UNDISCOVERED)

    def is_tour_complete(self):
        """
        Predicate to check if the tour is already complete
        """
        return self.completed == self.size

    def tour(self, start: Vertex) -> List[Vertex]:
        """
        Generate a tour of all the vertices
        """
        status: bool = self.__tour(start, self.size)
        if not status:
            raise Exception('No Tour of size %s found'.format(self.size))
        assert (
            len(self.path) == self.size), "Invalid tour size %s".format(self.path)
        return self.path

    def __tour(self, start: Vertex, left: int) -> bool:
        """
        Generate a tour from the given start vertex
        """
        # log.info('KT from %s of size %s', start.id, size)

        assert self.completed + left == self.size

        if self.is_tour_complete():
            # Already complete
            log.info('Size is done. Path is %s', self.path)
            return self.path

        self.push_to_path(start)

        if (self.completed % 5 == 0) and (self.completed > self.view_count):
            self.graph.stop_and_view()
            self.view_count = self.completed

        i, status, nbr = 0, False, list(start.get_connections())
        while i < len(nbr) and (not status):
            succ = nbr[i]
            # A new node available. Try to find a tour from that node
            if succ.get_state() == State.UNDISCOVERED:
                log.info('Trying %s %s', succ.id, succ.state)
                status = self.__tour(succ, left - 1)
            i = i + 1

        if not status:
            self.pop_from_path()

        return status
