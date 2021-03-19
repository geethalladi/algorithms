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

    G: IGraph

    def setup_method(self):
        edges: Sequence[Edge] = [
            ('a', 'b'),
            ('b', 'c'),
            ('d', 'e'),
            ('e', 'a')
        ]
        self.G: IGraph = Graph.build('test_digraph_view',
                                     edges, directed=False)

    def test_dfs_single(self):
        assert self.G is not None

    def test_bfs_parent(self):
        self.G.bfs('A')
        assert self.G.get_vertex('A').parent is None
        assert self.G.get_vertex('B').parent == 'A'
        assert self.G.get_vertex('E').parent == 'A'
        assert self.G.get_vertex('C').parent == 'B'
        assert self.G.get_vertex('D').parent == 'E'

    def test_bfs_distance(self):
        self.G.bfs('A')
        assert self.G.get_vertex('A').distance == 0
        assert self.G.get_vertex('B').distance == 1
        assert self.G.get_vertex('E').distance == 1
        assert self.G.get_vertex('C').distance == 2
        assert self.G.get_vertex('D').distance == 2
