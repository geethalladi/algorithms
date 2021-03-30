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

import pytest

from algo.fibonacci import fib_recursive as fr
from algo.fibonacci import fib_cached
from algo.fibonacci import fib_dp


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

    @pytest.mark.skip(reason="Took 1229.847708 seconds (20.5 minutes)")
    def test_recursive_fib_timer(self):
        start = time.process_time()
        for i in range(0, 45):
            log.debug('F[%s] = %s', i, fr(i))
        end = time.process_time()
        log.info('Took %s to complete recursive Fibonacci series', (end - start))

    def test_fib_cached(self):
        assert fib_cached(0) == 0
        assert fib_cached(1) == 1

        for i in range(0, len(self.result)):
            assert fib_cached(i) == self.result[i]

    def test_fib_cached_timer(self):
        start = time.process_time()
        for i in range(0, 45):
            log.debug('F[%s] = %s', i, fib_cached(i))
        end = time.process_time()
        # takes 0.005469000000000002 seconds
        log.info('Took %s to complete cached Fibonacci series', (end - start))

    def test_fib_dp(self):
        assert fib_dp(0) == 0
        assert fib_dp(1) == 1

        for i in range(0, len(self.result)):
            assert fib_dp(i) == self.result[i]

    def test_fib_dp_timer(self):
        start = time.process_time()
        for i in range(0, 45):
            log.debug('F[%s] = %s', i, fib_dp(i))
        end = time.process_time()
        # takes 0.0002770000000000272 seconds
        # (20 times faster than cached version)
        log.info('Took %s to complete DP Fibonacci series', (end - start))
