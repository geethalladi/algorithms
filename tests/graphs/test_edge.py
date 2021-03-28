# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from algo.graphs.edge import Edge
from algo.graphs.state import State


class TestEdge:
    """
    A Test Suite for Edge
    """

    def test_default(self):
        assert Edge('A', 'B')

    def test_properties(self):
        edge: Edge = Edge('A', 'B', 1)
        assert edge.source == 'A'
        assert edge.dest == 'B'
        assert edge.weight == 1
        assert edge.directed is False
        assert edge.state is State.UNDISCOVERED

    def test_properties_2(self):
        edge: Edge = Edge('A', 'B', 4, directed=True, state=State.DISCOVERED)
        assert edge.source == 'A'
        assert edge.dest == 'B'
        assert edge.weight == 4
        assert edge.directed is True
        assert edge.state is State.DISCOVERED

    def test_equality(self):
        e1: Edge = Edge('A', 'B', 4, directed=True, state=State.DISCOVERED)
        e2: Edge = Edge('A', 'B', 4, directed=True, state=State.DISCOVERED)
        assert e1 == e2

    def test_inequality(self):
        e1: Edge = Edge('A', 'B', 4, directed=True, state=State.DISCOVERED)
        e2: Edge = Edge('B', 'A', 4, directed=True, state=State.DISCOVERED)
        assert e1 != e2

    def test_equality_undirected(self):
        e3: Edge = Edge('B', 'C', 4, directed=False, state=State.DISCOVERED)
        e4: Edge = Edge('C', 'B', 4, directed=False, state=State.UNDISCOVERED)
        e5: Edge = Edge('C', 'B', 4, directed=False, state=State.UNDISCOVERED)
        assert e3 == e4
        assert e4 == e3
        assert e3 == e5
        assert e4 == e5

    def test_set_membership(self):
        e1: Edge = Edge('A', 'B', 4, directed=True, state=State.DISCOVERED)
        e2: Edge = Edge('B', 'A', 4, directed=True, state=State.DISCOVERED)
        e3: Edge = Edge('B', 'C', 4, directed=False, state=State.DISCOVERED)
        e4: Edge = Edge('C', 'B', 4, directed=False, state=State.UNDISCOVERED)
        e5: Edge = Edge('C', 'B', 4, directed=False, state=State.UNDISCOVERED)
        assert set([e1, e2, e3, e4, e5]) == {e1, e2, e3}

    def test_transpose(self):
        edge: Edge = Edge('A', 'B', 4, directed=True, state=State.DISCOVERED)
        result: Edge = edge.transpose()
        assert result.source == 'B'
        assert result.dest == 'A'
        assert result.weight == 4
        assert result.directed is True
        assert result.state is State.UNDISCOVERED
