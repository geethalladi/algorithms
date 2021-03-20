# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from typing import Sequence

from algo.knights_tour import knights_tour
from algo.graphs.vertex import Vertex

import pytest


class TestKnightsTour:
    """
    A Test Suite for KnightsTour
    """

    @pytest.mark.skip(reason="Very slow running")
    def test_knights_tour_8(self):
        result: Sequence[Vertex] = knights_tour(8)
        expected = [
            '(0, 0)', '(1, 2)', '(0, 4)', '(2, 3)', '(0, 2)', '(2, 1)',
            '(1, 3)', '(0, 1)', '(2, 0)', '(3, 2)', '(1, 1)', '(0, 3)',
            '(2, 2)', '(1, 0)', '(3, 1)', '(5, 0)', '(4, 2)', '(3, 0)',
            '(5, 1)', '(4, 3)', '(2, 4)', '(0, 5)', '(1, 7)', '(3, 6)',
            '(1, 5)', '(0, 7)', '(2, 6)', '(1, 4)', '(0, 6)', '(2, 5)',
            '(4, 4)', '(6, 3)', '(7, 1)', '(5, 2)', '(4, 0)', '(6, 1)',
            '(5, 3)', '(3, 4)', '(4, 6)', '(2, 7)', '(3, 5)', '(1, 6)',
            '(3, 7)', '(4, 5)', '(5, 7)', '(7, 6)', '(6, 4)', '(7, 2)',
            '(6, 0)', '(4, 1)', '(3, 3)', '(5, 4)', '(7, 3)', '(6, 5)',
            '(7, 7)', '(5, 6)', '(7, 5)', '(6, 7)', '(5, 5)', '(4, 7)',
            '(6, 6)', '(7, 4)', '(6, 2)', '(7, 0)']
        assert result == expected

    def test_knights_tour_5(self):
        result: Sequence[Vertex] = knights_tour(5)
        expected = ['(0, 0)', '(1, 2)', '(0, 4)', '(2, 3)', '(0, 2)',
                    '(1, 4)', '(3, 3)', '(4, 1)', '(2, 0)', '(0, 1)',
                    '(1, 3)', '(3, 4)', '(2, 2)', '(1, 0)', '(3, 1)',
                    '(4, 3)', '(2, 4)', '(0, 3)', '(1, 1)', '(3, 0)',
                    '(4, 2)', '(2, 1)', '(4, 0)', '(3, 2)', '(4, 4)']
        assert [v.id for v in result] == expected
