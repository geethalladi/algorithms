"""
Edge ADT
"""

from typing import NamedTuple


class Edge(NamedTuple):
    """
    Edge as a named tuple
    """
    source: str
    dest: str
    weight: int = 1

    def __repr__(self) -> str:
        return 'Edge({}, {}, {})'.format(self.source,
                                         self.dest,
                                         self.weight)

    # def __new__(cls, length, width, color="white"):
    #     return super(TemplateContainer, cls).__new__(cls, length, width, color)
