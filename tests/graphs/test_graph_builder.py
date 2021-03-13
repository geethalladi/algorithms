# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from algo.graphs.graph import Graph
from algo.graphs.igraph import IGraph


class TestGraphBuilderMixin:
    """
    A Test Suite for GraphBuilderMixin
    """

    def test_graph(self):
        G: IGraph = Graph(name='test_graph_builder', directed=False)
        G.build([
            ('a', 'b', 5),
            ('a', 'c', 10),
            ('b', 'e', 20),
            ('b', 'c', 15),
            ('c', 'd')
        ])
        assert G is not None
        G.view()

    def test_digraph(self):
        DG: IGraph = Graph(name='test_digraph_builder', directed=True)
        DG.build([
            ('a', 'b', 5),
            ('a', 'c', 10),
            ('b', 'e', 20),
            ('b', 'c', 15),
            ('c', 'd', 10)
        ])
        assert DG is not None
        DG.view()
