# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from typing import Sequence

from algo.graphs.edge import EdgeInput
from algo.graphs.graph import Graph
from algo.graphs.igraph import IGraph
from algo.graphs.shortest_path import dijkstra


class TestDijkstra:
    """
    A Test Suite for dijkstra
    """
    DG: IGraph

    def setup_method(self):
        edges: Sequence[EdgeInput] = [
            ('u', 'v', 2),
            ('u', 'x', 1),
            ('u', 'w', 5),
            ('w', 'z', 5),
            ('x', 'y', 1),
            ('x', 'w', 3),
            ('x', 'v', 2),
            ('y', 'z', 1),
            ('y', 'w', 1),
            ('v', 'w', 3)
        ]
        self.DG: IGraph = Graph.build('test_digraph_view',
                                      edges, directed=False)

    def test_distance(self):
        self.DG = dijkstra(self.DG, 'U')
        assert self.DG.get_vertex('U').distance == 0
        assert self.DG.get_vertex('V').distance == 2
        assert self.DG.get_vertex('W').distance == 3
        assert self.DG.get_vertex('X').distance == 1
        assert self.DG.get_vertex('Y').distance == 2
        assert self.DG.get_vertex('Z').distance == 3

    def test_parent(self):
        self.DG = dijkstra(self.DG, 'U')
        assert self.DG.get_vertex('U').parent is None
        assert self.DG.get_vertex('V').parent.id == 'U'
        assert self.DG.get_vertex('W').parent.id == 'Y'
        assert self.DG.get_vertex('X').parent.id == 'U'
        assert self.DG.get_vertex('Y').parent.id == 'X'
        assert self.DG.get_vertex('Z').parent.id == 'Y'
