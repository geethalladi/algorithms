"""
Given k eggs and a 'n' story building, find the minimum
droppings to find the smallest floor, where the egg breaks
"""

import logging as log

from functools import lru_cache
import sys

from typing import List


class Solution:  # pylint: disable=too-many-public-methods
    """ Solution ADT """

    def superEggDrop(self, eggs: int, floors: int) -> int:
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
                result = self.compute_result_for(i, j, table)
                table[i][j] = result

        return table[eggs][floors]

    def compute_result_for(self, eggs, floor, table):
        """
        For the given (eggs, floor), find the minimum drops
        required. Identify the best floor `x` where this drop
        can happen. The best floor `x` is where `t1` = `t2`
        Using binary search to find this floor
        """

        result = sys.maxsize
        start = 1

        for x in range(start, floor + 1):
            t1 = table[eggs-1][x-1]
            t2 = table[eggs][floor-x]
            if t1 >= t2:
                c = t1 + 1
            else:
                c = t2 + 1

            if c < result:
                result = c

        return result
