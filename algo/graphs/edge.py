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
