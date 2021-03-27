# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use
from typing import Sequence

from algo.graphs.graph import Graph
from algo.graphs.igraph import IGraph
from algo.graphs.edge import Edge


class TestGraphBuilderMixin:
    """
    A Test Suite for GraphBuilderMixin
    """

    def setup_method(self):
        self.edges: Sequence[Edge] = [
            ('a', 'b', 5),
            ('a', 'c', 10),
            ('b', 'e', 20),
            ('b', 'c', 15),
            ('c', 'd')
        ]

    def test_graph(self):
        G: IGraph = Graph.build('test_graph_builder',
                                self.edges, directed=False)
        assert G is not None
        # G.view()

    def test_digraph(self):
        DG: IGraph = Graph.build('test_digraph_builder',
                                 self.edges, directed=True)
        assert DG is not None
        # DG.view()
