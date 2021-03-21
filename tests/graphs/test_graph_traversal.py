# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from typing import Sequence

from algo.graphs.edge import Edge
from algo.graphs.graph import Graph
from algo.graphs.igraph import IGraph


class TestGraphTraversalMixin:
    """
    A Test Suite for GraphTraversalMixin
    """

    def setup_method(self):
        self.edges: Sequence[Edge] = [
            ('a', 'b'),
            ('b', 'c'),
            ('d', 'e'),
            ('e', 'a')
        ]

    def test_bfs_parent(self):
        graph: IGraph = Graph.build('test_bfs',
                                    self.edges, directed=False)
        graph.bfs('A')
        assert graph.get_vertex('A').parent is None
        assert graph.get_vertex('B').parent == 'A'
        assert graph.get_vertex('E').parent == 'A'
        assert graph.get_vertex('C').parent == 'B'
        assert graph.get_vertex('D').parent == 'E'

    def test_bfs_distance(self):
        graph: IGraph = Graph.build('test_bfs_distance',
                                    self.edges, directed=False)
        graph.bfs('A')
        assert graph.get_vertex('A').distance == 0
        assert graph.get_vertex('B').distance == 1
        assert graph.get_vertex('E').distance == 1
        assert graph.get_vertex('C').distance == 2
        assert graph.get_vertex('D').distance == 2

    def test_dfs_parent(self):
        graph: IGraph = Graph.build('test_dfs',
                                    self.edges, directed=False)
        graph.dfs('A')
        assert graph.get_vertex('A').parent is None
        assert graph.get_vertex('B').parent == 'A'
        assert graph.get_vertex('E').parent == 'A'
        assert graph.get_vertex('C').parent == 'B'
        assert graph.get_vertex('D').parent == 'E'
