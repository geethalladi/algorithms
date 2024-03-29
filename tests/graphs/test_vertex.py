# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

import logging as log

from algo.graphs.state import State
from algo.graphs.vertex import Vertex


class TestVertex:
    """
    A Test Suite for Vertex
    """

    def test_singleton(self):
        v1: Vertex = Vertex('a')
        log.debug("Connections count is %s", len(v1.neighbours()))

    def test_empty(self):
        v1: Vertex = Vertex('v')
        assert v1 is not None

    def test_add_directed_edge(self):
        v1: Vertex = Vertex('a')
        v2: Vertex = Vertex('b')
        v1.add_edge(v2)
        assert v2 in v1.neighbours()
        assert v1 in v2.neighbours()

    def test_add_undirected_edge(self):
        v1: Vertex = Vertex('a')
        v2: Vertex = Vertex('b')
        v1.add_edge(v2, 2, directed=True)
        assert v2 in v1.neighbours()
        assert v1 not in v2.neighbours()

    def test_weight(self):
        v1: Vertex = Vertex('a')
        v2: Vertex = Vertex('b')
        v1.add_edge(v2, 2, directed=True)
        assert 2 == v1.weight(v2)

    def test_multiple_edges(self):
        v1: Vertex = Vertex('a')
        v2: Vertex = Vertex('b')
        v3: Vertex = Vertex('c')
        v1.add_edge(v2)
        v1.add_edge(v3)
        assert v2 in v1.neighbours()
        assert v3 in v1.neighbours()

    def test_state(self):
        v1: Vertex = Vertex('a')
        assert v1.state == State.UNDISCOVERED
        v1.state = State.DISCOVERED
        assert v1.state == State.DISCOVERED
        v1.state = State.PROCESSED
        assert v1.state == State.PROCESSED

    # def test_color(self):
    #     v1: Vertex = Vertex('a')
    #     assert v1.color() == State.UNDISCOVERED.color()
    #     v1.state = State.DISCOVERED
    #     assert v1.color() == State.DISCOVERED.color()
    #     v1.state = State.PROCESSED
    #     assert v1.color() == State.PROCESSED.color()

    def test_clear(self):
        v1: Vertex = Vertex('a')
        v1.state = State.DISCOVERED
        assert v1.state == State.DISCOVERED
        assert v1.distance == 0
        assert v1.parent is None
        v1.clear()
        assert v1.state == State.UNDISCOVERED
        assert v1.distance == 0
        assert v1.parent is None

    def test_same_edge(self):
        v1: Vertex = Vertex('a')
        v2: Vertex = Vertex('b')
        v1.add_edge(v2, 4, directed=False)
        assert v1.edge(v2) == v2.edge(v1)

    def test_same_edge_state_change(self):
        v1: Vertex = Vertex('a')
        v2: Vertex = Vertex('b')
        v1.add_edge(v2, 4, directed=False)
        v1.edge(v2).state = State.PROCESSED
        assert v1.edge(v2) == v2.edge(v1)

    def test_same_edge_id(self):
        """
        This test is not a hard requirement. It's just
        one of the ways of having the same edge state
        in an undirected edge
        """
        v1: Vertex = Vertex('a')
        v2: Vertex = Vertex('b')
        v1.add_edge(v2, 4, directed=False)
        assert v1.edge(v2) == v2.edge(v1)
        assert id(v1.edge(v2)) == id(v2.edge(v1))
