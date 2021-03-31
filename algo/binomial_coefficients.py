"""
Algorithm to compute binomial coefficients

Based on Pascal's Triangle. Uses Dynamic Programming
design technique

Dynamic Programming - Identify the partial results required
Construct a table to store all the partial results. Populate
the table. Based on these partial results, compute the final
result. Avoids recursive function calls
"""

import logging as log
from typing import List


def binomial_coefficient(n: int, k: int) -> int:  # pylint: disable=invalid-name
    assert (k <= n), 'Cannot choose when k, {} is more than n {}'.format(k, n)

    # table is a 2D square matrix
    # with only the left bottom half filled
    # the partical results resemble the pascal's triangle
    table: List[List[int]] = []

    # rows 0 - n
    for i in range(0, n + 1):
        table.append([])
        for j in range(0, n + 1):
            table[i].append(0)

    print_table(table, n + 1)

    # (n, k) -> Given n choose k
    # (n, 0) is always 1 == {}
    for i in range(0, n + 1):
        table[i][0] = 1

    # (n, n) is always 1 == every-thing()
    for i in range(0, n + 1):
        table[i][i] = 1

    print_table(table, n + 1)

    # compute (n, k) = (n-1, k-1) + (n-1, k)
    for i in range(1, n + 1):
        for j in range(1, i):
            table[i][j] = table[i - 1][j - 1] + table[i - 1][j]

    print_table(table, n + 1)

    return table[n][k]


# def init_2d_array():


def print_table(table: List[List[int]], size: int):
    log.info('***********************')
    for i in range(0, size):
        log.info(table[i])
