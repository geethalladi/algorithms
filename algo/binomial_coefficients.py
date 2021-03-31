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
