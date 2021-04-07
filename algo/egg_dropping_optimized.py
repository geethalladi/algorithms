"""
Given k eggs and a 'n' story building, find the minimum
droppings to find the smallest floor, where the egg breaks
"""

import logging as log

from typing import List

__all__ = ['egg_dropping']

"""
Lessons learnt by Leetcode submission and acceptance.

- Don't log, not even debug logs (String processing and output takes time)
- Avoid function calls. Calling and returning consumes time
- Use only the memory that is required. Storing large tables (DP)
  might not be a good idea
- Code readability will be sacrificed
- Only solve the given problem. Having more data to help yourself
  in future, to add a new feature on top, does not align with
  leetcode's submission and acceptance model.
"""


def egg_dropping(eggs: int, floors: int) -> int:
    """
    Given the eggs, find the minimum droppings required to find the
    smallest floor, amongst the `floors` above which any dropped
    egg would break
    """
    table: List[List[int]] = []

    # Init an empty table
    for _ in range(0, eggs + 1):
        table.append([0] * (floors + 1))

    # on a single floor with k eggs, the answer is 1
    for i in range(0, eggs + 1):
        table[i][1] = 1

    # with a single egg, and n floors, the ans is n
    for j in range(0, floors + 1):
        table[1][j] = j

    for i in range(2, eggs + 1):
        for j in range(2, floors + 1):
            result = compute_cost(i, j, table)
            table[i][j] = result
            log.debug('E(%s, %s) = %s', i, j, result)

    return table[eggs][floors]


def compute_cost(eggs: int, floors: int, table: List[List[int]]) -> int:
    """
    For the given (eggs, floors), find the minimum drops
    required. Identify the best floors `x` where this drop
    can happen. The best floors `x` is where `t1` = `t2`
    The curve resembles 'X' where t1 keeps on increasing
    and t2 keeps decreasing. The min(max(t1, t2)) occurs
    around the mid points. Using binary search to find
    this floor. This procedure was based on the solution
    from leetcode.
    (https://leetcode.com/problems/super-egg-drop/solution/)
    """

    low, high = 1, floors + 1
    while (low <= high):
        x = (low + high) // 2
        t1 = table[eggs - 1][x - 1]
        t2 = table[eggs][floors - x]
        if t1 == t2:
            # Found the optimal point where
            # the max(t1, t2) will be at its
            # minimal value
            break
        if t1 < t2:
            low = x + 1
        elif t2 < t1:
            high = x - 1

    return 1 + max(t1, t2)
