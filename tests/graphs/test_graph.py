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
    D: Vertex
    E: Vertex

    def setup_method(self):
        self.G = Graph()
        self.A = self.G.add_vertex('a')
        self.B = self.G.add_vertex('b')
        self.C = self.G.add_vertex('c')
        self.D = self.G.add_vertex('d')
        self.E = self.G.add_vertex('e')

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

    def test_many_vertices(self):
        self.G.add_edge(self.A, self.B, 5, True)
        self.G.add_edge(self.B, self.C, 6, False)
        self.G.add_edge(self.D, self.E, 5, False)
        self.G.add_edge(self.E, self.A, 6, False)

        assert self.G.num_vertices == 5
        assert set([self.A, self.B, self.C,
                    self.D, self.E]) == set(self.G)

    def test_many_vertices_edges(self):
        self.G.add_edge(self.A, self.B, 5, True)
        self.G.add_edge(self.B, self.C, 6, False)
        self.G.add_edge(self.D, self.E, 5, False)
        self.G.add_edge(self.E, self.A, 6, False)

        assert self.A.get_weight(self.B) == 5
        assert self.A.get_weight(self.E) == 6
        assert self.B.get_weight(self.C) == 6
        assert self.C.get_weight(self.B) == 6
        assert self.D.get_weight(self.E) == 5
        assert self.E.get_weight(self.D) == 5

    def test_connected(self):
        self.G.add_edge(self.A, self.B, 5, True)
        self.G.add_edge(self.B, self.C, 6, False)
        assert self.G.is_connected(self.A, self.B)
        assert not self.G.is_connected(self.B, self.A)

    def test_directed(self):
        self.G.add_edge(self.A, self.B, 5, True)
        self.G.add_edge(self.B, self.C, 6, False)
        assert self.G.is_directed(self.A, self.B)
        assert not self.G.is_directed(self.C, self.B)

    def test_directed_2(self):
        self.G.add_edge(self.A, self.B, 5, True)
        self.G.add_edge(self.B, self.A, 6, True)
        # Both of them should be true
        assert self.G.is_directed(self.A, self.B)
        assert self.G.is_directed(self.B, self.A)

    def test_undirected(self):
        self.G.add_edge(self.A, self.B, 2, False)
        assert self.G.is_undirected(self.A, self.B)
        assert self.G.is_undirected(self.B, self.A)

    def test_undirected_2(self):
        self.G.add_edge(self.A, self.B, 2, True)
        assert not self.G.is_undirected(self.A, self.B)
        assert not self.G.is_undirected(self.B, self.A)
