# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from algo.graphs.graph import Graph
from algo.graphs.vertex import Vertex
from algo.graphs.igraph import IGraph


class TestGraph:
    """
    A Test Suite for Graph
    """
    G: IGraph
    A: Vertex
    B: Vertex
    C: Vertex
    D: Vertex
    E: Vertex

    def setup_method(self):
        self.G = Graph('test_graph')
        self.A = self.G.add_vertex('a')
        self.B = self.G.add_vertex('b')
        self.C = self.G.add_vertex('c')
        self.D = self.G.add_vertex('d')
        self.E = self.G.add_vertex('e')

    def test_empty(self):
        assert self.G is not None

    def test_igraph_instance(self):
        assert isinstance(self.G, IGraph)

    def test_two_vertices_default(self):
        self.G.add_edge_str('a', 'b')
        assert self.B in self.A.neighbours()
        assert self.A in self.B.neighbours()
        assert 'a' in self.G
        assert 'b' in self.G
        assert self.A.get_weight(self.B) == 1
        assert self.B.get_weight(self.A) == 1

    def test_two_vertices(self):
        self.G.add_edge(self.A, self.B)
        assert self.B in self.A.neighbours()
        assert self.A in self.B.neighbours()
        assert self.A.get_weight(self.B) == 1
        assert self.B.get_weight(self.A) == 1

    def test_two_vertices_2(self):
        self.G.add_edge(self.A, self.B, 5)
        assert self.B in self.A.neighbours()
        assert self.A in self.B.neighbours()
        assert self.A.get_weight(self.B) == 5
        assert self.B.get_weight(self.A) == 5

    def test_many_vertices(self):
        self.G.add_edge(self.A, self.B, 5)
        self.G.add_edge(self.B, self.C, 6)
        self.G.add_edge(self.D, self.E, 5)
        self.G.add_edge(self.E, self.A, 6)

        assert self.G.num_vertices == 5
        assert set([self.A, self.B, self.C,
                    self.D, self.E]) == set(self.G)

    def test_many_vertices_edges(self):
        self.G.add_edge(self.A, self.B, 5)
        self.G.add_edge(self.B, self.C, 6)
        self.G.add_edge(self.D, self.E, 5)
        self.G.add_edge(self.E, self.A, 6)

        assert self.A.get_weight(self.B) == 5
        assert self.B.get_weight(self.A) == 5

        assert self.A.get_weight(self.E) == 6
        assert self.E.get_weight(self.A) == 6

        assert self.D.get_weight(self.E) == 5
        assert self.E.get_weight(self.D) == 5

        assert self.B.get_weight(self.C) == 6
        assert self.C.get_weight(self.B) == 6

    def test_connected(self):
        self.G.add_edge(self.A, self.B, 5)
        self.G.add_edge(self.B, self.C, 6)
        assert self.G.is_connected(self.A, self.B)
        assert self.G.is_connected(self.B, self.A)

    def test_undirected(self):
        self.G.add_edge(self.A, self.B, 2)
        assert self.G.is_undirected(self.A, self.B)
        assert self.G.is_undirected(self.B, self.A)

    def test_transpose(self):
        self.G.add_edge(self.A, self.B, 5)
        self.G.add_edge(self.B, self.C, 6)
        self.G.add_edge(self.D, self.E, 5)
        self.G.add_edge(self.E, self.A, 6)

        result: IGraph = self.G.transpose()

        (A, B, C, D, E) = (result.get_vertex('a'),
                           result.get_vertex('b'),
                           result.get_vertex('c'),
                           result.get_vertex('d'),
                           result.get_vertex('e'))

        assert A.get_weight(B) == 5
        assert B.get_weight(A) == 5

        assert A.get_weight(E) == 6
        assert E.get_weight(A) == 6

        assert D.get_weight(E) == 5
        assert E.get_weight(D) == 5

        assert B.get_weight(C) == 6
        assert C.get_weight(B) == 6


class TestDigraph:
    """
    A Test Suite for Graph
    """
    DG: IGraph
    A: Vertex
    B: Vertex
    C: Vertex
    D: Vertex
    E: Vertex

    def setup_method(self):
        self.DG = Graph('test_digraph', directed=True)
        self.A = self.DG.add_vertex('a')
        self.B = self.DG.add_vertex('b')
        self.C = self.DG.add_vertex('c')
        self.D = self.DG.add_vertex('d')
        self.E = self.DG.add_vertex('e')

    def test_empty(self):
        assert self.DG is not None

    def test_two_vertices_default(self):
        self.DG.add_edge_str('a', 'b')
        assert self.B in self.A.neighbours()
        assert self.A not in self.B.neighbours()
        assert self.A.get_weight(self.B) == 1

    def test_two_vertices(self):
        self.DG.add_edge(self.A, self.B)
        assert self.B in self.A.neighbours()
        assert self.A.get_weight(self.B) == 1

    def test_two_vertices_2(self):
        self.DG.add_edge(self.A, self.B, 5)
        assert self.B in self.A.neighbours()
        assert self.A.get_weight(self.B) == 5

    def test_many_vertices(self):
        self.DG.add_edge(self.A, self.B, 5)
        self.DG.add_edge(self.B, self.C, 6)
        self.DG.add_edge(self.D, self.E, 5)
        self.DG.add_edge(self.E, self.A, 6)

        assert self.DG.num_vertices == 5
        assert set([self.A, self.B, self.C,
                    self.D, self.E]) == set(self.DG)

    def test_many_vertices_edges(self):
        self.DG.add_edge(self.A, self.B, 5)
        self.DG.add_edge(self.B, self.C, 6)
        self.DG.add_edge(self.D, self.E, 5)
        self.DG.add_edge(self.E, self.A, 6)

        assert self.A.get_weight(self.B) == 5
        assert self.B.get_weight(self.C) == 6
        assert self.D.get_weight(self.E) == 5
        assert self.E.get_weight(self.A) == 6

        assert self.A not in self.B.neighbours()
        assert self.E not in self.A.neighbours()

    def test_connected(self):
        self.DG.add_edge(self.A, self.B, 5)
        self.DG.add_edge(self.B, self.C, 6)
        assert self.DG.is_connected(self.A, self.B)
        assert not self.DG.is_connected(self.B, self.A)

    def test_directed(self):
        self.DG.add_edge(self.A, self.B, 5)
        self.DG.add_edge(self.B, self.A, 6)
        # Both of them should be true
        assert self.DG.is_directed(self.A, self.B)
        assert self.DG.is_directed(self.B, self.A)

    def test_transpose(self):
        self.DG.add_edge(self.A, self.B, 5)
        self.DG.add_edge(self.B, self.C, 6)
        self.DG.add_edge(self.D, self.E, 5)
        self.DG.add_edge(self.E, self.A, 6)

        result: IGraph = self.DG.transpose()

        (A, B, C, D, E) = (result.get_vertex('a'),
                           result.get_vertex('b'),
                           result.get_vertex('c'),
                           result.get_vertex('d'),
                           result.get_vertex('e'))

        assert B.get_weight(A) == 5
        assert C.get_weight(B) == 6
        assert E.get_weight(D) == 5
        assert A.get_weight(E) == 6

        assert B not in A.neighbours()
        assert A not in E.neighbours()
