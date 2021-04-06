"""
Given k eggs and a 'n' story building, find the minimum
droppings to find the smallest floor, where the egg breaks
"""

import sys

from typing import List

__all__ = ['egg_dropping']


def egg_dropping(eggs: int, floors: int) -> int:
    """
    Given the eggs, find the minimum droppings required to find the
    smallest floor, amongst the `floors` above which any dropped
    egg would break
    """
    table: List[List[int]] = []

    # Init an empty table
    for i in range(0, eggs + 1):
        table.append([])
        for _ in range(0, floors + 1):
            table[i].append(0)

    # on a single floor with k eggs, the answer is 1
    for i in range(0, eggs + 1):
        table[i][1] = 1

    # with a single egg, and n floors, the ans is n
    for j in range(0, floors + 1):
        table[1][j] = j

    for i in range(2, eggs + 1):
        for j in range(2, floors + 1):
            result = sys.maxsize
            for x in range(1, j + 1):
                c = __compute_cost(x, i, j, table)
                if c < result:
                    result = c
            table[i][j] = result
    return table[eggs][floors]


def __compute_cost(x: int, eggs: int, floors: int, table: List[List[int]]) -> int:
    return max(table[eggs - 1][x - 1], table[eggs][floors - x]) + 1
