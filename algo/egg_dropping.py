"""
Given k eggs and a 'n' story building, find the minimum
droppings to find the smallest floor, where the egg breaks
"""

import logging as log

from dataclasses import dataclass
from typing import List, Tuple

__all__ = ['egg_dropping']


@dataclass
class Cell:
    """
    An ADT for storing table contents
    """
    eggs: int = 0
    moves: int = 0
    parent: Tuple[int, int] = (-1, -1)


def egg_dropping(eggs: int, floors: int) -> int:
    """
    Given the eggs, find the minimum droppings required to find the
    smallest floor, amongst the `floors` above which any dropped
    egg would break
    """
    assert (eggs >= 0 and floors >=
            0), f'Invalid pre-condition {eggs}, {floors}'

    empty: Cell = Cell()
    table: List[List[Cell]] = []

    # Init an empty table
    for _ in range(0, eggs + 1):
        table.append([empty] * (floors + 1))

    # on a single floor with k eggs, the answer is 1
    for i in range(0, eggs + 1):
        table[i][1] = Cell(i, 1, (-1, -1))

    # with a single egg, and n floors, the ans is n
    for j in range(0, floors + 1):
        table[1][j] = Cell(1, j, (1, j - 1))

    for i in range(2, eggs + 1):
        for j in range(2, floors + 1):
            result = compute_cost(i, j, table)
            table[i][j] = result
            log.debug('E(%s, %s) = %s', i, j, result)

    return table[eggs][floors].moves


# pylint: disable=invalid-name
def compute_cost(eggs: int, floors: int, table: List[List[Cell]]) -> Cell:
    """
    Try dropping the egg from each of the 'x' floors
    and find its minimum
    """
    partials: List[Cell] = []
    for x in range(1, floors + 1):
        # if egg breaks
        c: Cell = table[eggs - 1][x - 1]
        # if it does not
        d: Cell = table[eggs][floors - x]

        # what is the maximum moves when the egg is thrown from floor 'x'
        # 1+ to account for throwing from floor 'x'
        if c.moves > d.moves:
            partials.append(Cell(eggs, c.moves + 1, (eggs - 1, x - 1)))
        else:
            partials.append(Cell(eggs, d.moves + 1, (eggs, floors - x)))

    # find which 'x' gives me the minimum result (minimum of all maximums)
    return min(partials, key=lambda c: c.moves)
