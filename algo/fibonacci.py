"""
Different implementation of fibonacci series
"""

# import logging as log


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
