# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from algo.graphs.graph import Graph


class TestGraph:
    """
    A Test Suite for Graph
    """

    def test_empty(self):
        g = Graph()
        assert g is not None
