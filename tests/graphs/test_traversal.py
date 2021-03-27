# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from typing import Sequence

from algo.graphs.edge import EdgeInput
from algo.graphs.graph import Graph
from algo.graphs.igraph import IGraph
from algo.graphs.traversal import breadth_first_search as bfs
from algo.graphs.traversal import depth_first_search as dfs


class TestGraphTraversal:
    """
    A Test Suite for GraphTraversal
    """

    edges: Sequence[EdgeInput]

    def setup_method(self):
        self.edges = [
            ('a', 'b'),
            ('b', 'c'),
            ('d', 'e'),
            ('e', 'a')
        ]

    def test_bfs_parent(self):
        graph: IGraph = Graph.build('test_bfs',
                                    self.edges, directed=False)
        bfs(graph, 'A')
        assert graph.get_vertex('A').parent is None
        assert graph.get_vertex('B').parent.id == 'A'
        assert graph.get_vertex('E').parent.id == 'A'
        assert graph.get_vertex('C').parent.id == 'B'
        assert graph.get_vertex('D').parent.id == 'E'

    def test_bfs_distance(self):
        graph: IGraph = Graph.build('test_bfs_distance',
                                    self.edges, directed=False)
        bfs(graph, 'A')
        assert graph.get_vertex('A').distance == 0
        assert graph.get_vertex('B').distance == 1
        assert graph.get_vertex('E').distance == 1
        assert graph.get_vertex('C').distance == 2
        assert graph.get_vertex('D').distance == 2

    def test_dfs_parent(self):
        graph: IGraph = Graph.build('test_dfs',
                                    self.edges, directed=False)
        dfs(graph, 'A')
        assert graph.get_vertex('A').parent is None
        assert graph.get_vertex('B').parent.id == 'A'
        assert graph.get_vertex('E').parent.id == 'A'
        assert graph.get_vertex('C').parent.id == 'B'
        assert graph.get_vertex('D').parent.id == 'E'

    def test_dfs_parent_directed(self):
        edges: Sequence[EdgeInput] = [
            ('a', 'b'),
            ('b', 'c'),
            ('d', 'e'),
            ('e', 'f'),
            ('e', 'b'),
            ('a', 'd'),
            ('f', 'c'),
            ('b', 'd')
        ]

        graph: IGraph = Graph.build('test_dfs_parent_directed',
                                    edges, directed=True)
        dfs(graph, 'A')
        assert graph.get_vertex('A').parent is None
        assert graph.get_vertex('B').parent.id == 'A'
        assert graph.get_vertex('C').parent.id == 'B'
        assert graph.get_vertex('D').parent.id == 'B'
        assert graph.get_vertex('E').parent.id == 'D'
        assert graph.get_vertex('F').parent.id == 'E'

    def test_dfs_distance_directed(self):
        edges: Sequence[EdgeInput] = [
            ('a', 'b'),
            ('b', 'c'),
            ('d', 'e'),
            ('e', 'f'),
            ('e', 'b'),
            ('a', 'd'),
            ('f', 'c'),
            ('b', 'd')
        ]

        graph: IGraph = Graph.build('test_dfs_distance_directed',
                                    edges, directed=True)
        dfs(graph, 'A')
        assert graph.get_vertex('A').distance == 0
        assert graph.get_vertex('B').distance == 1
        assert graph.get_vertex('C').distance == 2
        assert graph.get_vertex('D').distance == 2
        assert graph.get_vertex('E').distance == 3
