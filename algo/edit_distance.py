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
    parent: Tuple[int, int] = (0, 0)

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

    table: List[List[Cell]] = __edit_distance(source, dest)

    cost: int = table[len(source)][len(dest)].cost
    path: str = find_path(table, len(source), len(dest))

    return (cost, path)


def __edit_distance(source: str, dest: str) -> List[List[Cell]]:

    # for 1 based index (simplicity of accessing table)
    start, end = (' ' + source), (' ' + dest)
    rows, cols = (len(start)), (len(end))
    table: List[List[Cell]] = init_table(rows, cols)

    # table[i][j] -> minimum difference between
    # 'i' length prefix of source to match 'j' length
    # prefix of dest. When 'i' and 'j' are equal to their
    # respective lengths, then we have the result

    # No transformation required
    table[0][0] = Cell(0, '', (-1, -1))

    # Converting a 0 length source to destination
    for j in range(1, cols):
        # Insert all the characters
        table[0][j] = Cell(j, 'I', (0, j - 1))

    # Converting any string to 0 length destination
    for i in range(1, rows):
        # Delete all the characters
        table[i][0] = Cell(i, 'D', (i - 1, 0))

    # Computing the table
    for i in range(1, rows):
        for j in range(1, cols):
            # match / substitute cost
            m: Cell
            # they match
            if start[i] == end[j]:
                # (ABCD, ADCD) -> C(ABC, ADC) + 0
                m = Cell(table[i - 1][j - 1].cost,
                         'M',
                         (i - 1, j - 1))
            else:
                # substitute
                # (ABCD, ADCE) -> C(ABC, ADC) + 1 (D for E)
                m = Cell(table[i - 1][j - 1].cost + 1,  # for substitute
                         'S',
                         (i - 1, j - 1))

            # insert cost
            # (ADC, ABCE) -> C(ADC, ABC) + 1 (Insert E)
            insert: Cell = Cell(table[i][j - 1].cost + 1,  # for insertion
                                'I',
                                (i, j - 1))

            # delete cost
            # (ADCE, ABC) -> C(ADC, ABC) + 1 (Delete E)
            delete: Cell = Cell(table[i - 1][j].cost + 1,  # for deletion
                                'D',
                                (i - 1, j))

            # Update the parent
            m = minimum(m, insert, delete)
            table[i][j] = m

    return table


def find_path(table: List[List[Cell]], x: int, y: int) -> str:
    """
    Find the edit path
    """
    if (x < 0 or y < 0):
        return ''

    c: Cell = table[x][y]

    return find_path(table, *(c.parent)) + c.op


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
