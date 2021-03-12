# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

import logging as log

from algo.graphs.vertex import Vertex


class TestVertex:
    """
    A Test Suite for Vertex
    """

    def test_singleton(self):
        v1: Vertex = Vertex('a')
        log.info("Connections count is %s", len(v1.get_connections()))

    def test_empty(self):
        v1: Vertex = Vertex('v')
        assert v1 is not None

    def test_add_directed_edge(self):
        v1: Vertex = Vertex('a')
        v2: Vertex = Vertex('b')
        v1.add_edge(v2)
        assert v2 in v1.get_connections()
        assert v1 in v2.get_connections()

    def test_add_undirected_edge(self):
        v1: Vertex = Vertex('a')
        v2: Vertex = Vertex('b')
        v1.add_edge(v2, 2, directed=True)
        assert v2 in v1.get_connections()
        assert v1 not in v2.get_connections()

    def test_get_weight(self):
        v1: Vertex = Vertex('a')
        v2: Vertex = Vertex('b')
        v1.add_edge(v2, 2, directed=True)
        assert 2 == v1.get_weight(v2)

    def test_multiple_edges(self):
        v1: Vertex = Vertex('a')
        v2: Vertex = Vertex('b')
        v3: Vertex = Vertex('c')
        v1.add_edge(v2)
        v1.add_edge(v3)
        assert v2 in v1.get_connections()
        assert v3 in v1.get_connections()
