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
    table: List[List[int]] = __init_table(eggs, floors)

    for i in range(2, eggs + 1):
        for j in range(2, floors + 1):
            result = sys.maxsize
            for x in range(1, j + 1):
                c = __compute_cost(x, i, j, table)
                if c < result:
                    result = c
            table[i][j] = result
    return table[eggs][floors]


def __init_table(eggs: int, floors: int) -> List[List[int]]:
    result: List[List[int]] = []

    # Init an empty table
    for i in range(0, eggs + 1):
        result.append([])
        for _ in range(0, floors + 1):
            result[i].append(0)

    # on a single floor with k eggs, the answer is 1
    for i in range(0, eggs + 1):
        result[i][1] = 1

    # with a single egg, and n floors, the ans is n
    for j in range(0, floors + 1):
        result[1][j] = j

    return result


# pylint: disable=invalid-name
def __compute_cost(x: int, eggs: int, floors: int, table: List[List[int]]) -> int:
    # if egg breaks
    c = table[eggs - 1][x - 1]
    # if it does not
    d = table[eggs][floors - x]

    # log.debug('From %s floor, %s, %s', x, c, d)

    # what is the maximum moves when the egg is thrown from floor 'x'
    # 1+ to account for throwing from floor 'x'
    if c >= d:
        return c + 1

    return d + 1
