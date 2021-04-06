"""
Given k eggs and a 'n' story building, find the minimum
droppings to find the smallest floor, where the egg breaks
"""

import logging as log

from functools import lru_cache
import sys

from typing import List


# @lru_cache
# def superEggDropR(eggs: int, floors: int) -> int:
#     assert eggs >= 0 and floors >= 0, 'Invalid condition'
#     if eggs <= 0:
#         return 0
#     if floors <= 1:
#         return 1
#     if eggs == 1:
#         return floors

#     log.info('Call %s, %s', eggs, floors)
#     result = sys.maxsize
#     for x in range(1, floors + 1):
#         c1, c2 = superEggDropR(eggs-1, x-1), superEggDropR(eggs, floors-x)
#         c = max(c1, c2) + 1
#         if c < result:
#             result = c

#     return result


class Solution:  # pylint: disable=too-many-public-methods
    """ Solution ADT """

    def __get(self, i, j, x, table) -> int:
        return

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
                    c = max(table[i-1][x-1],
                            table[i][j-x]) + 1

                    if c < result:
                        result = c
                        table[i][j] = result

        return table[eggs][floors]


# class SolutionLC(object):
#     def superEggDrop(self, K, N):
#         # Right now, dp[i] represents dp(1, i)
#         dp = range(N+1)

#         for k in range(2, K+1):
#             # Now, we will develop dp2[i] = dp(k, i)
#             dp2 = [0]
#             x = 1
#             for n in range(1, N+1):
#                 # Let's find dp2[n] = dp(k, n)
#                 # Increase our optimal x while we can make our answer better.
#                 # Notice max(dp[x-1], dp2[n-x]) > max(dp[x], dp2[n-x-1])
#                 # is simply max(T1(x-1), T2(x-1)) > max(T1(x), T2(x)).
#                 while x < n and max(dp[x-1], dp2[n-x]) > \
#                         max(dp[x], dp2[n-x-1]):
#                     x += 1

#                 # The final answer happens at this x.
#                 dp2.append(1 + max(dp[x-1], dp2[n-x]))

#             dp = dp2

#         return dp[-1]
