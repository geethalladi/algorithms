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
