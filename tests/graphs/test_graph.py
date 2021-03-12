# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from algo.graphs.graph import Graph
from algo.graphs.vertex import Vertex


class TestGraph:
    """
    A Test Suite for Graph
    """
    G: Graph
    A: Vertex
    B: Vertex
    C: Vertex

    def setup_method(self):
        self.G = Graph()
        self.A = self.G.add_vertex('a')
        self.B = self.G.add_vertex('b')

    def test_empty(self):
        assert self.G is not None

    def test_two_vertices_default(self):
        self.G.add_edge_str('a', 'b')
        assert self.B in self.A.get_connections()
        assert self.A in self.B.get_connections()
        assert self.A.get_weight(self.B) == 1
        assert self.B.get_weight(self.A) == 1

    def test_two_vertices(self):
        self.G.add_edge(self.A, self.B)
        assert self.B in self.A.get_connections()
        assert self.A in self.B.get_connections()
        assert self.A.get_weight(self.B) == 1
        assert self.B.get_weight(self.A) == 1

    def test_two_vertices_2(self):
        self.G.add_edge(self.A, self.B, 5, True)
        assert self.B in self.A.get_connections()
        assert self.A not in self.B.get_connections()
        assert self.A.get_weight(self.B) == 5
