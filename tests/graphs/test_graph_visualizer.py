# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from algo.graphs.graph_visualizer import GraphVisualizer
from algo.graphs.vertex import Vertex


class TestDigraphVisualizer:
    """
    A Test Suite for DigraphVisualizer
    """

    DG: GraphVisualizer
    A: Vertex
    B: Vertex
    C: Vertex
    D: Vertex
    E: Vertex

    def setup_method(self):
        self.DG = GraphVisualizer('test_digraph', directed=True)
        self.A = self.DG.add_vertex('a')
        self.B = self.DG.add_vertex('b')
        self.C = self.DG.add_vertex('c')
        self.D = self.DG.add_vertex('d')
        self.E = self.DG.add_vertex('e')

    def test_empty(self):
        assert self.DG is not None

    def test_view(self):
        self.DG.add_edge(self.A, self.B, 5)
        self.DG.add_edge(self.B, self.C, 6)
        self.DG.add_edge(self.D, self.E, 5)
        self.DG.add_edge(self.E, self.A, 6)
        self.DG.view()


class TestGraphVisualizer:
    """
    A Test Suite for GraphVisualizer
    """
    G: GraphVisualizer
    A: Vertex
    B: Vertex
    C: Vertex
    D: Vertex
    E: Vertex

    def setup_method(self):
        self.G = GraphVisualizer('test_graph')
        self.A = self.G.add_vertex('a')
        self.B = self.G.add_vertex('b')
        self.C = self.G.add_vertex('c')
        self.D = self.G.add_vertex('d')
        self.E = self.G.add_vertex('e')

    def test_empty(self):
        assert self.G is not None

    def test_view(self):
        self.G.add_edge(self.A, self.B, 5)
        self.G.add_edge(self.B, self.C, 6)
        self.G.add_edge(self.D, self.E, 5)
        self.G.add_edge(self.E, self.A, 6)
        self.G.view()
