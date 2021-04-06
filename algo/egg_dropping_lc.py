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
            start = 1
            for j in range(2, floors + 1):
                result = sys.maxsize
                for x in range(start, j + 1):
                    if table[i-1][x-1] >= table[i][j-x]:
                        c = table[i-1][x-1] + 1
                        l1 = x-1
                    else:
                        c = table[i][j-x] + 1
                        l1 = j-x

                    if c < result:
                        result = c
                        l2 = l1
                        table[i][j] = result

                # # # remember the previous best level
                # if l2 > start:
                #     log.info('Start is modified to %s', l2)
                #     start = l2

        return table[eggs][floors]
