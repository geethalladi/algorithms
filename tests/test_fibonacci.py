# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

import logging as log
import time

from typing import List

from algo.fibonacci import fib_recursive as fr


class TestFibonacci:
    """
    A Test Suite for Fibonacci
    """

    result: List[int]

    def setup_method(self):
        self.result = [0, 1, 1, 2, 3, 5, 8, 13,
                       21, 34, 55, 89, 144, 233, 377, 610]

    def test_recursive_fib(self):
        assert fr(0) == 0
        assert fr(1) == 1

        for i in range(0, len(self.result)):
            assert fr(i) == self.result[i]

    def test_recursive_fib_timer(self):
        for i in range(0, 45):
            log.info('F[%s] = %s', i, fr(i))
