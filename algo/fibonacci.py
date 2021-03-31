"""
Different implementation of fibonacci series
"""

import logging as log
from typing import List, Dict

__all__ = ['fib_recursive', 'fib_cached', 'fib_dp']


def fib_recursive(n: int) -> int:  # pylint: disable=invalid-name
    """
    Naive recursive implementation of fibonacci
    """
    assert n >= 0, 'Negative index {} for computing Fib'.format(n)
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# use functool cache for a better implementation
# constructing the table by hand for a learning experience


# can be replaced with a list
# dictionary gives a more table like feel
cache_table: Dict[int, int] = {
    0: 0,
    1: 1
}


def fib_cached(n: int) -> int:  # pylint: disable=invalid-name
    """
    Cached version of fibonacci series
    """

    # return from the cache if already computed
    if n in cache_table:
        return cache_table[n]

    log.debug('Computing Fibo[%s]', n)
    result = fib_cached(n - 1) + fib_cached(n - 2)
    cache_table[n] = result
    return result


def fib_dp(n: int) -> int:  # pylint: disable=invalid-name
    """
    Fibonacci based on dynamic programming technique
    """
    if n <= 0:
        return 0
    # table for storing partial results
    table: List[int] = [0, 1]

    for i in range(2, n + 1):
        result = table[i-1] + table[i-2]
        table.append(result)

    return table[n]
