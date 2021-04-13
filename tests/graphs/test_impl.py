# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from typing import Sequence

from algo.graphs.edge import EdgeInput
from algo.graphs.graph import Graph
from algo.graphs.igraph import IGraph
from algo.graphs.impl import is_bipartite


class TestGraphImplementations:
    """
    A Test Suite for GraphImplementations
    """

    def test_bipartite(self):
        edges: Sequence[EdgeInput] = [
            ('a', 'b'),
            ('a', 'c'),
            ('b', 'e'),
            ('c', 'd')
        ]
        g: IGraph = Graph.build('test_graph_builder',
                                edges, directed=True)

        assert is_bipartite(g, 'A')

    def test_bipartite2(self):
        edges: Sequence[EdgeInput] = [
            ('a', 'b'),
            ('a', 'c'),
            ('b', 'd'),
            ('c', 'd'),
            ('d', 'e')
        ]
        g: IGraph = Graph.build('test_graph_builder',
                                edges, directed=False)

        assert is_bipartite(g, 'A')

    def test_bipartite_false(self):
        edges: Sequence[EdgeInput] = [
            ('a', 'b'),
            ('a', 'c'),
            ('b', 'c'),
            ('c', 'd'),
            ('d', 'e')
        ]
        g: IGraph = Graph.build('test_graph_builder',
                                edges, directed=False)
        assert not is_bipartite(g, 'A')

    def test_bipartite2_false(self):
        edges: Sequence[EdgeInput] = [
            ('a', 'b'),
            ('a', 'c'),
            ('b', 'c'),
            ('c', 'd'),
            ('d', 'e')
        ]
        g: IGraph = Graph.build('test_graph_builder',
                                edges, directed=True)
        assert not is_bipartite(g, 'A')
