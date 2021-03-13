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

    G: IGraph

    def setup_method(self):
        self.G = Graph(name='test_graph_builder', directed=False)
        self.G.build([
            ('a', 'b', 5),
            ('a', 'c', 10),
            ('b', 'e', 20),
            ('b', 'c', 15),
            ('c', 'd', 10)
        ])

    def test_empty(self):
        assert self.G is not None
        self.G.view()
