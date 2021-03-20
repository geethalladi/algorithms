# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from typing import List, Sequence

from algo.knights_tour import knights_tour, is_valid_tour, KT
from algo.graphs.vertex import Vertex
from algo.graphs.graph import Graph
from algo.graphs.edge import Edge

import pytest


class TestKnightsTour:
    """
    A Test Suite for KnightsTour
    """

    expected_5: Sequence[str]
    expected_8: Sequence[str]

    def setup_method(self):
        self.expected_5 = [
            '(0, 0)', '(1, 2)', '(0, 4)', '(2, 3)', '(0, 2)',
            '(1, 4)', '(3, 3)', '(4, 1)', '(2, 0)', '(0, 1)',
            '(1, 3)', '(3, 4)', '(2, 2)', '(1, 0)', '(3, 1)',
            '(4, 3)', '(2, 4)', '(0, 3)', '(1, 1)', '(3, 0)',
            '(4, 2)', '(2, 1)', '(4, 0)', '(3, 2)', '(4, 4)']
        self.expected_8 = [
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

    @pytest.mark.skip(reason="Very slow running")
    def test_knights_tour_8(self):
        result: Sequence[Vertex] = knights_tour(8)
        result_str: Sequence[str] = [v.id for v in result]
        assert is_valid_tour(result_str, 8)
        assert result_str == self.expected_8

    def test_knights_tour_5(self):
        result: Sequence[Vertex] = knights_tour(5)
        result_str: Sequence[str] = [v.id for v in result]
        assert is_valid_tour(result_str, 5)
        assert result_str == self.expected_5

    def test_valid_tour(self):
        assert is_valid_tour(self.expected_5, 5)
        assert is_valid_tour(self.expected_8, 8)

    def test_kt(self):
        edges = [('A', 'B'),
                 ('A', 'D'),
                 ('B', 'C'),
                 ('B', 'D'),
                 ('D', 'E'),
                 ('E', 'B'),
                 ('E', 'F'),
                 ('F', 'C')]
        g = Graph.build('test_KT', edges, directed=True)
        g.view()
