"""
Edge ADT
"""

from dataclasses import dataclass
from typing import NamedTuple, Tuple, Optional, Iterable

from algo.graphs.state import State

__all__ = ['Edge', 'EdgeInput']


# Moving away from NamedTuples as they are immutable

@dataclass
class Edge:
    """
    A Simple Container for holding edge details
    """
    # starting really simple
    # consciously avoiding direction for now
    # can be added if there is a requirement
    weight: int = 1
    state: State = State.UNDISCOVERED


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
