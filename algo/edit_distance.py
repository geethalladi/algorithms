"""
Implements edit_distance algorithm as described in
ADM, Skiena. Follows Dynamic Programming technique
for this implementation
"""

from dataclasses import dataclass
from typing import ClassVar, List, Optional, Tuple


@dataclass
class Cell:
    """
    Cell for storing the operation
    """
    Empty: ClassVar[Optional['Cell']] = None

    cost: int
    op: str
    parent: Optional[Tuple[int, int]] = None

    @classmethod
    def empty(cls):
        """
        defines a default empty instance
        """
        if cls.Empty:
            return cls.Empty

        cls.Empty = Cell(0, '')
        return cls.Empty


def edit_distance(source: str, dest: str) -> Tuple[int, str]:
    """
    Find the shortest number of transformations required to transform
    `source` to `dest`. The allowed transformations are [modify,
    insert, delete]. Everything has the same cost. The algorithm
    optimizes for minimising this cost. The result is a tuple,
    containing both the tuple and the transformations (encoded)
    required.

    At each pair of prefixes (i, j) the minimum cost will be the
    minimum of (modify, insert, delete). Use a table to store these
    results. Based on the previosuly computed values, compute the
    current result. Look at the recursive version (in the book) for
    more details
    """

    if source == dest:
        return (0, '')

    # for 1 based index (simplicity of accessing table)
    start, end = (' ' + source), (' ' + dest)
    rows, cols = (len(start)), (len(end))
    table: List[List[Cell]] = init_table(rows, cols)

    for i in range(0, rows):
        for j in range(0, cols):
            # match / modify cost
            match: Cell = Cell(0, 'M')

            # insert cost
            insert: Cell = Cell(1, 'I')

            # delete cost
            delete: Cell = Cell(1, 'D')

            # Update the parent
            m = minimum(match, insert, delete)
            table[i][j] = m

    path: str = find_path(table)
    return (table[len(source)][len(dest)].cost, path)


def find_path(_: List[List[Cell]]) -> str:
    """
    Find the edit path
    """
    return ''


def init_table(rows: int, cols: int) -> List[List[Cell]]:
    """
    Initialize the table
    """
    table: List[List[Cell]] = []
    for r in range(0, rows):
        table.append([])
        for _ in range(0, cols):
            table[r].append(Cell.empty())
    return table


def minimum(match: Cell, insert: Cell, delete: Cell) -> Cell:
    """
    Find the minimum among the three
    """
    result: Cell = match
    for c in [insert, delete]:
        if c.cost < result.cost:
            result = c
    return result
