# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from algo.graphs.shortest_path import dijkstra
from algo.graphs.graph import Graph


class TestDijkstra:
    """
    A Test Suite for dijkstra
    """

    def setup_method(self):
        edges: Sequence[Edge] = [
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

    def test_sample(self):
        assert self.DG.get_vertex('U').distance == 0
        assert self.DG.get_vertex('V').distance == 2
        assert self.DG.get_vertex('W').distance == 5
        assert self.DG.get_vertex('X').distance == 1
        assert self.DG.get_vertex('Y').distance == 2
        assert self.DG.get_vertex('Z').distance == 3
