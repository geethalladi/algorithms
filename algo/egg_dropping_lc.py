"""
Given k eggs and a 'n' story building, find the minimum
droppings to find the smallest floor, where the egg breaks
"""

import logging as log

import functools
import sys

from typing import List


class Solution:  # pylint: disable=too-many-public-methods
    """ Solution ADT """

    def __get(self, i, j, x, table) -> int:
        return max(table[i-1][x-1],
                   table[i][j-x]) + 1
    @functools.lru_cache
    def superEggDropR(self, eggs: int, floors: int) -> int:
        assert eggs >= 0 and floors >= 0, 'Invalid condition'
        if eggs <= 0:
            return 0
        if floors <= 1:
            return 1
        if eggs == 1:
            return floors

        log.info('Call %s, %s', eggs, floors)
        result = sys.maxsize
        for x in range(1, floors + 1):
            c1, c2 = self.superEggDropR(
                eggs - 1, x - 1), self.superEggDropR(eggs, floors - x)
            c = max(c1, c2) + 1
            if c < result:
                result = c

        return result

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
                result = sys.maxsize
                for x in range(1, j + 1):
                    c = self.__get(i, j, x, table)
                    if c < result:
                        result = c
                        table[i][j] = result

        return table[eggs][floors]
