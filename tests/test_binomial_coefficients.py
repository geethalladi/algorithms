# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from typing import List

from algo.binomial_coefficients import binomial_coefficient as bc


class TestBinomialCoefficient:
    """
    A Test Suite for binomial_coefficient
    """

    result = List[List[int]]

    def setup_method(self):
        self.result = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1]
        ]

    def test_binomial_coefficient(self):
        for i in range(1, len(self.result)):
            for j in range(0, i):
                assert bc(i, j)
