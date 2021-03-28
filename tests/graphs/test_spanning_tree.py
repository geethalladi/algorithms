# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from typing import Sequence

from algo.graphs.edge import EdgeInput
from algo.graphs.graph import Graph
from algo.graphs.igraph import IGraph
from algo.graphs.spanning_tree import prim


class TestSpanningTree:
    """
    A Test Suite for Spanning Tree
    """
    G: IGraph

    def setup_method(self):
        edges: Sequence[EdgeInput] = [
            ('a', 'b', 2),
            ('a', 'c', 3),
            ('b', 'c', 1),
            ('b', 'd', 1),
            ('b', 'e', 4),
            ('d', 'e', 1),
            ('e', 'f', 1),
            ('f', 'g', 1),
            ('c', 'f', 5)
        ]
        self.G: IGraph = Graph.build('test_mst',
                                     edges, directed=False)

    def test_prim(self):
        prim(self.G, 'A')
        # self.G.view(pause=True)
        # assert edges

    def test_parent(self):
        prim(self.G, 'A')
        assert self.G.get_vertex('A').parent is None
        assert self.G.get_vertex('B').parent.id == 'A'
        assert self.G.get_vertex('C').parent.id == 'B'
        assert self.G.get_vertex('D').parent.id == 'B'
        assert self.G.get_vertex('E').parent.id == 'D'
        assert self.G.get_vertex('F').parent.id == 'E'
        assert self.G.get_vertex('G').parent.id == 'F'
