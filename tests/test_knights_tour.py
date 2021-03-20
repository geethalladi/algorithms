# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from typing import Sequence

from algo.knights_tour import knights_tour
from algo.graphs.vertex import Vertex


class TestKnightsTour:
    """
    A Test Suite for KnightsTour
    """

    def test_knights_tour_8(self):
        assert 1 == 1

    def test_knights_tour_5(self):
        result: Sequence[Vertex] = knights_tour(5)
        expected = ['(0, 0)', '(1, 2)', '(0, 4)', '(2, 3)', '(0, 2)',
                    '(1, 4)', '(3, 3)', '(4, 1)', '(2, 0)', '(0, 1)',
                    '(1, 3)', '(3, 4)', '(2, 2)', '(1, 0)', '(3, 1)',
                    '(4, 3)', '(2, 4)', '(0, 3)', '(1, 1)', '(3, 0)',
                    '(4, 2)', '(2, 1)', '(4, 0)', '(3, 2)', '(4, 4)']
        assert [v.id for v in result] == expected
