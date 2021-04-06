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
    table: List[List[Cell]] = __init_table(eggs, floors)

    for i in range(2, eggs + 1):
        for j in range(2, floors + 1):
            # Try dropping the egg from each of the 'x' floors
            # and find its minimum
            partials: List[Cell] = [__compute_cost(x, i, j, table)
                                    for x in range(1, floors + 1)]
            result: Cell = min(partials, key=lambda c: c.moves)
            # log.info('Cost for %s eggs with %s floors is %s',
            #          i, j, result.moves)
            table[i][j] = result

    return table[eggs][floors].moves


def __init_table(eggs: int, floors: int) -> List[List[Cell]]:
    result: List[List[Cell]] = []
    empty: Cell = Cell()

    # Init an empty table
    for i in range(0, eggs + 1):
        result.append([])
        for _ in range(0, floors + 1):
            result[i].append(empty)

    # on a single floor with k eggs, the answer is 1
    for i in range(0, eggs + 1):
        result[i][1] = Cell(i, 1, (-1, -1))

    # with a single egg, and n floors, the ans is n
    for j in range(0, floors + 1):
        result[1][j] = Cell(1, j, (1, j - 1))

    return result


# pylint: disable=invalid-name
def __compute_cost(x: int, eggs: int, floors: int, table: List[List[Cell]]) -> Cell:
    # if egg breaks
    c: Cell = table[eggs - 1][x - 1]
    # if it does not
    d: Cell = table[eggs][floors - x]

    # log.debug('From %s floor, %s, %s', x, c, d)

    # what is the maximum moves when the egg is thrown from floor 'x'
    # 1+ to account for throwing from floor 'x'
    if c.moves > d.moves:
        return Cell(eggs, c.moves + 1, (eggs - 1, x - 1))

    return Cell(eggs, d.moves + 1, (eggs, floors - x))
