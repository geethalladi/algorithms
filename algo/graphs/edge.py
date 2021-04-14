"""
Edge ADT
"""

from enum import Enum, auto, unique
from dataclasses import dataclass
from typing import NamedTuple, Tuple, Optional, Iterable

from algo.graphs.state import State

__all__ = ['Edge', 'EdgeInput', 'EdgeType']


# Moving away from NamedTuples as they are immutable

@unique
class EdgeType(Enum):
    """
    Edge type as an enum
    """
    UNKNOWN = auto()
    TREE = auto()
    BACK = auto()
    FORWARD = auto()
    CROSS = auto()


@dataclass
class Edge:
    """
    A Simple Container for holding edge details
    """
    # adding details for use during transpose
    # Avoiding Vertex class for now, using string id
    source: str
    dest: str
    weight: int = 1
    directed: bool = False
    state: State = State.UNDISCOVERED
    type: EdgeType = EdgeType.UNKNOWN

    def clear(self):
        """
        Clear the state of the edge
        """
        self.state = State.UNDISCOVERED
        self.type = EdgeType.UNKNOWN

    def transpose(self):
        """
        Transpose this edge
        """
        return Edge(self.dest,
                    self.source,
                    self.weight,
                    self.directed)

    def __key(self):
        """
        Unique key for this instance
        """
        x, y = self.source, self.dest
        if (not self.directed) and (self.source > self.dest):
            # for undirected use the smallest vertex at the left
            x, y = self.dest, self.source
        return (x, y, self.weight, self.directed)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Edge):
            return self.__key() == other.__key()  # pylint: disable=protected-access
        return NotImplemented

    def __str__(self):
        return f'[{self.source}, {self.dest}, {self.directed}]'


class EdgeInput(NamedTuple):
    """
    Edge as a named tuple
    """
    source: str
    dest: str
    weight: int = 1

    def __repr__(self) -> str:
        return '[{}, {}, {}]'.format(self.source,
                                     self.dest,
                                     self.weight)

    @classmethod
    def __make_edge(cls, tup: Tuple[str, str, Optional[int]]):
        """
        Make a single edge instance
        """
        if len(tup) == 3 and tup[2] is not None:
            return EdgeInput(tup[0], tup[1], tup[2])
        return EdgeInput(source=tup[0], dest=tup[1], weight=1)

    @classmethod
    def make(cls, iterable: Iterable['EdgeInput']):
        """
        Writing make specifically for edges
        """
        return [cls.__make_edge(e) for e in iterable]
