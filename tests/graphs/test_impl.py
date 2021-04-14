# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

import logging as log

from typing import Sequence

from algo.graphs.edge import EdgeInput, EdgeType as ET
from algo.graphs.graph import Graph
from algo.graphs.igraph import IGraph
from algo.graphs.impl import is_bipartite, edge_classifier


class TestEdgeClassifier:
    """
    A Test Suite for edge classification
    """

    def test_undirected_tree_back(self):
        edges: Sequence[EdgeInput] = [
            ('1', '2'),
            ('1', '5'),
            ('1', '6'),
            ('2', '3'),
            ('2', '5'),
            ('3', '4'),
            ('4', '5'),
            ('5', '6'),
            ('2', '6'),
            ('2', '4')
        ]
        g: IGraph = Graph.build('test_edge_classification',
                                edges, directed=False)
        edge_classifier(g, '1')
        # undirected graph should only have
        # (tree, back) edges
        for e in g.edges():
            assert e.type in [ET.TREE, ET.BACK]

    def test_undirected(self):
        edges: Sequence[EdgeInput] = [
            ('1', '2'),
            ('1', '5'),
            ('1', '6'),
            ('2', '3'),
            ('2', '5'),
            ('3', '4'),
            ('4', '5')
        ]
        g: IGraph = Graph.build('test_graph_builder',
                                edges, directed=False)

        result = {
            '(1, 2)': ET.TREE,
            '(2, 3)': ET.TREE,
            '(3, 4)': ET.TREE,
            '(4, 5)': ET.TREE,
            '(1, 6)': ET.TREE,
            '(2, 5)': ET.BACK,
            '(1, 5)': ET.BACK
        }
        edge_classifier(g, '1')
        for e in g.edges():
            assert e.type == result[f'({e.source}, {e.dest})']

    def test_directed(self):
        edges: Sequence[EdgeInput] = [
            ('1', '2'),
            ('2', '3'),
            ('1', '3'),
            ('2', '4'),
            ('4', '1')
        ]
        g: IGraph = Graph.build('test_graph_builder',
                                edges, directed=True)

        result = {
            '(1, 2)': ET.TREE,
            '(2, 3)': ET.TREE,
            '(1, 3)': ET.FORWARD,
            '(2, 4)': ET.TREE,
            '(4, 1)': ET.BACK
        }
        edge_classifier(g, '1')
        for e in g.edges():
            log.info(e)
            assert e.type == result[f'({e.source}, {e.dest})']

    def test_directed_cross(self):
        edges: Sequence[EdgeInput] = [
            ('1', '2'),
            ('2', '3'),
            ('4', '2')
        ]
        g: IGraph = Graph.build('test_graph_builder',
                                edges, directed=True)

        result = {
            '(1, 2)': ET.TREE,
            '(2, 3)': ET.TREE,
            '(4, 2)': ET.CROSS
        }
        edge_classifier(g, '1')
        for e in g.edges():
            log.info(e)
            assert e.type == result[f'({e.source}, {e.dest})']


class TestBiPartite:
    """
    A Test Suite for bipartite
    """

    def test_bipartite(self):
        edges: Sequence[EdgeInput] = [
            ('a', 'b'),
            ('a', 'c'),
            ('b', 'e'),
            ('c', 'd')
        ]
        g: IGraph = Graph.build('test_graph_builder',
                                edges, directed=True)

        assert is_bipartite(g, 'A')

    def test_bipartite2(self):
        edges: Sequence[EdgeInput] = [
            ('a', 'b'),
            ('a', 'c'),
            ('b', 'd'),
            ('c', 'd'),
            ('d', 'e')
        ]
        g: IGraph = Graph.build('test_graph_builder',
                                edges, directed=False)

        assert is_bipartite(g, 'A')

    def test_bipartite_false(self):
        edges: Sequence[EdgeInput] = [
            ('a', 'b'),
            ('a', 'c'),
            ('b', 'c'),
            ('c', 'd'),
            ('d', 'e')
        ]
        g: IGraph = Graph.build('test_graph_builder',
                                edges, directed=False)
        assert not is_bipartite(g, 'A')

    def test_bipartite2_false(self):
        edges: Sequence[EdgeInput] = [
            ('a', 'b'),
            ('a', 'c'),
            ('b', 'c'),
            ('c', 'd'),
            ('d', 'e')
        ]
        g: IGraph = Graph.build('test_graph_builder',
                                edges, directed=True)
        assert not is_bipartite(g, 'A')


class TestHasCycle:
    """
    A Test Suite for testing cycle
    """

    def test(self):
        assert 1 == 1
