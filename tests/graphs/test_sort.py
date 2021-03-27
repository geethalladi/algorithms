# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from typing import Sequence

from algo.graphs.edge import Edge
from algo.graphs.graph import Graph
from algo.graphs.igraph import IGraph
from algo.graphs.sort import topological_sort

import pytest


class TestGraphSort:
    """
    A Test Suite for Sorting Graphs
    """

    edges: Sequence[Edge]

    def test_topological_sorting(self):
        edges: Sequence[Edge] = [
            ('3/4 cup milk', '1 cup mix'),
            ('1 egg', '1 cup mix'),
            ('1 Tbl Oil', '1 cup mix'),
            ('1 cup mix', 'pour 1/4 cup'),
            ('1 cup mix', 'heat syrup'),
            ('head griddle', 'pour 1/4 cup'),
            ('pour 1/4 cup', 'turn when bubbly'),
            ('turn when bubbly', 'eat'),
            ('heat syrup', 'eat')
        ]
        graph: IGraph = Graph.build('test_dfs_distance_directed',
                                    edges, directed=True)
        topological_sort(graph)

    def test_topological_sorting_2(self):
        edges: Sequence[Edge] = [
            ('A', 'B'),
            ('A', 'C'),
            ('B', 'C'),
            ('B', 'D'),
            ('C', 'E'),
            ('C', 'F'),
            ('E', 'D'),
            ('G', 'A'),
            ('G', 'F'),
            ('F', 'E')
        ]
        graph: IGraph = Graph.build('test_dfs_distance_directed',
                                    edges, directed=True)
        assert [v.id for v in topological_sort(graph)] == list('GABCFED')

    def test_topo_cycle(self):
        edges: Sequence[Edge] = [
            ('A', 'B'),
            ('B', 'C'),
            ('C', 'D'),
            ('D', 'A')
        ]
        graph: IGraph = Graph.build('test_dfs_distance_directed',
                                    edges, directed=True)
        with pytest.raises(Exception):
            print(topological_sort(graph))
