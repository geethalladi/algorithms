"""
Algorithm to compute binomial coefficients

Dynamic Programming - Identify the partial results required
Construct a table to store all the partial results. Populate
the table. Based on these partial results, compute the final
result. Avoids recursive function calls
"""

import logging as log
from typing import List

__all__ = ['binomial_coefficient']


def binomial_coefficient(n: int, k: int) -> int:  # pylint: disable=invalid-name
    """
    Binomial Coefficients using Dynamic Programming.

    The implementation is based on constructing the Pascal's triangle using
    Dynamic Programming Technique. Store all the partial results in the table
    and use them to compute the required (n, k), 'given n, choose k'.

    This method avoids using recursion at runtime by computing the partial
    results from the beginning (0, 0) till the original result. It then boils
    down to looking up the result in the table and returning it
    """
    assert (k <= n), 'Cannot choose when k, {} is more than n {}'.format(k, n)

    # table is a 2D square matrix
    # with only the left bottom half filled
    # the partical results resemble the pascal's triangle
    table = init_table(n + 1)

    # (n, k) -> Given n choose k
    # (n, 0) is always 1 == {}
    for i in range(0, n + 1):
        table[i][0] = 1

    # (n, n) is always 1 == every-thing()
    for i in range(0, n + 1):
        table[i][i] = 1

    # compute (n, k) = (n-1, k-1) + (n-1, k)
    for i in range(1, n + 1):
        for j in range(1, i):
            table[i][j] = table[i - 1][j - 1] + table[i - 1][j]

    log.debug(table)

    # look up the entry and return
    return table[n][k]


def init_table(size: int):
    """
    Initialize the table
    """
    table: List[List[int]] = []
    for i in range(0, size):
        table.append([])
        for _ in range(0, size):
            table[i].append(0)
    return table
