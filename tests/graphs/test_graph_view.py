# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from typing import Sequence

from algo.graphs.igraph import IGraph
from algo.graphs.graph import Graph
from algo.graphs.edge import Edge

import pytest  # type: ignore


class TestDigraphView:
    """
    A Test Suite for DigraphView
    """

    DG: Graph

    def setup_method(self):
        edges: Sequence[Edge] = [
            ('a', 'b', 5),
            ('b', 'c', 6),
            ('d', 'e', 5),
            ('e', 'a', 6)
        ]
        self.DG: IGraph = Graph.build('test_digraph_view',
                                      edges, directed=True)

    def test_empty(self):
        assert self.DG is not None

    @pytest.mark.skip(reason="generates graph")
    def test_view(self):
        self.DG.view()


class TestGraphView:
    """
    A Test Suite for GraphView
    """
    G: Graph

    def setup_method(self):
        edges: Sequence[Edge] = [
            ('a', 'b', 5),
            ('b', 'c', 6),
            ('d', 'e', 5),
            ('e', 'a', 6)
        ]
        self.G: IGraph = Graph.build('test_graph_view',
                                     edges, directed=False)

    def test_empty(self):
        assert self.G is not None

    @pytest.mark.skip(reason="generates graph")
    def test_view(self):
        self.G.view()
