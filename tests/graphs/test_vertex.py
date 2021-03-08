# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from algo.graphs.vertex import Vertex


class TestVertex:
    """
    A Test Suite for Vertex
    """

    def test_empty(self):
        v1 = Vertex('v')
        assert v1 is not None

    def test_add_edge(self):
        v1 = Vertex('a')
        v2 = Vertex('b')
        v1.add_edge(v2)
        assert v2 is not None
