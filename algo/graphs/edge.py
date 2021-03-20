"""
Edge ADT
"""

from typing import NamedTuple, Tuple, Optional, Iterable


class Edge(NamedTuple):
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
            return Edge(tup[0], tup[1], tup[2])
        return Edge(source=tup[0], dest=tup[1], weight=1)

    @classmethod
    def make(cls, iterable: Iterable['Edge']):
        """
        Writing make specifically for edges
        """
        return [cls.__make_edge(e) for e in iterable]
