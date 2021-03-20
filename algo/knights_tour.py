"""
Generate a knight's tour for the given n x n chess board
"""
import logging as log

from ast import literal_eval
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
        return '({}, {})'.format(self.x, self.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def displace(self, other: 'Position'):
        """
        Returns a new displaced Position
        """
        return Position(self.x + other.x,
                        self.y + other.y)

    def within_grid(self, top_right: 'Position',
                    bottom_left: 'Position' = None) -> bool:
        """
        Check if this position occurs within the specified grid
        """
        if not bottom_left:
            # Use origin if bottom_left is not specified
            bottom_left = Position(0, 0)

        return (bottom_left.x <= self.x <= top_right.x) and (
            bottom_left.y <= self.y <= top_right.y)

    def is_neighbour(self, pos: 'Position') -> bool:
        """
        Check if the two given positions are neighbouring
        """
        dx: int = abs(self.x - pos.x)
        dy: int = abs(self.y - pos.y)

        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)


# declaring a type for neighbour
Neighbour = Tuple[Position, Position]


def is_valid_tour(tour: Sequence[str], size: int) -> bool:
    """
    Given the board size, check if the tour is valid
    """
    assert len(tour) > 0, 'Empty Tour'

    # Check if all the nodes are covered in the tour
    if len(tour) != (size * size):
        log.info('Tour does not cover all the nodes')
        return False

    positions = [Position(*(literal_eval(v))) for v in tour]

    # Check if every position is a valid one
    top_right = Position(size - 1, size - 1)
    for pos in positions:
        if not pos.within_grid(top_right):
            log.info('Tour has an invalid position %s', pos)
            return False

    prev: Position = positions[0]
    for i in range(1, len(positions)):
        succ = positions[i]
        if not prev.is_neighbour(succ):
            log.info('%s and %s are not neighbours', prev, succ)
            return False
        prev = succ

    # When everything matches return True
    return True


def knights_tour(size: int) -> Sequence[Vertex]:
    """
    Generate the knights tour for the n x n
    chess board, starting at (0,0)
    """
    assert (size > 0), "Invalid size given"

    log.info('Generating knights tour of size, %s', size)
    graph: IGraph = __create_knights_tour_graph(size)
    return __generate_a_tour(graph, size)


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


# pylint: disable=unused-argument
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
    """
    Data type for Knight's Tour
    """
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
        """
        Clear all the internal state
        """
        self.path = []
        self.completed = 0
        self.view_count = 0

    def push_to_path(self, vertex: Vertex):
        """
        Add it to the top of the Stack
        """
        vertex.set_state(State.PROCESSED)
        self.path.append(vertex)
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
        self.__tour(start, self.size)

        if not self.is_tour_complete:
            raise Exception('No Tour of size {} found'.format(self.size))

        assert (
            len(self.path) == self.size), 'Invalid tour size {}'.format(self.path)
        return self.path

    # A variant of DFS, where a node is allowed to
    # be visited only once
    def __tour(self, start: Vertex, left: int):
        """
        Generate a tour from the given start vertex
        """
        assert self.completed + left == self.size

        log.debug('KT from %s of size %s', start.id, left)

        if self.is_tour_complete():
            return

        self.push_to_path(start)

        # # temporary code for viewing
        # if (self.completed % 5 == 0) and (self.completed > self.view_count):
        #     self.graph.stop_and_view()
        #     self.view_count = self.completed

        for succ in start.get_connections():
            # A new node available. Try to find a tour from that node
            if succ.get_state() == State.UNDISCOVERED:
                log.debug('Trying %s %s', succ.id, succ.state)
                self.__tour(succ, left - 1)
            if self.is_tour_complete():
                return

        # backtrack - no possible paths found from this node
        # reached a dead end here, backtracking is the only
        # available option
        self.pop_from_path()
        return
