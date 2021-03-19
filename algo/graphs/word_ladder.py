"""
Module for word ladder problem
"""

import logging as log

from typing import Dict, Sequence, List

from algo.graphs.edge import Edge
from algo.graphs.graph import Graph
from algo.graphs.igraph import IGraph
from algo.graphs.vertex import Vertex

log.basicConfig(level=log.INFO)


def find_shortest_path(words: Sequence[str], start: str, end: str) -> Sequence[str]:
    """
    Given the list of words, find the shortest path in the word ladder.
    Obtained by replacing only one character. All the words in the given
    input should be of the same length
    """
    assert len(words) > 0, "Empty Dictionary supplied"
    assert len(start) > 0, "Empty start word"
    assert len(start) == len(
        end), "Start and end words does not have the same length"

    length = len(words[0])
    assert len(
        start) == length, "Start / End does not match with dictionary lengths"

    assert all([len(x) == length for x in words]
               ), "Invalid length found in words"

    graph: IGraph = construct_word_ladder([w.capitalize() for w in words])
    return find_path_bfs(graph, start.capitalize(), end.capitalize())


def bucket(word: str) -> List[str]:
    """
    Find all the possible buckets
    """
    result: List[str] = []
    for i in range(len(word)):
        tmp: List[str] = list(word)
        tmp[i] = '_'
        result.append(''.join(tmp))

    return result


def to_buckets(words: Sequence[str]) -> Dict[str, List[str]]:
    """
    Identify the buckets for each word
    """
    result: Dict[str, List[str]] = {}
    for w in words:
        bs: Sequence[str] = bucket(w)
        for b in bs:
            v: List[str] = result.get(b, [])
            v.append(w)
            result[b] = v

    return result


def add_to_edges(edges: List[Edge], words: Sequence[str]):
    """
    Add each pair for words into an edge
    """
    length = len(words)
    for i in range(0, length):
        for j in range((i + 1), length):
            e: Edge = Edge(words[i], words[j])
            edges.append(e)


def construct_word_ladder(words: Sequence[str]):
    """
    Construct a graph from the given dictionary words
    """
    buckets: Dict[str, List[str]] = to_buckets(words)
    edges: List[Edge] = []

    for _, ws in buckets.items():
        # every word should have an edge
        add_to_edges(edges, ws)

    return Graph.build('word-ladder', edges, directed=False)


def find_path_bfs(graph: IGraph, start: str, end: str) -> Sequence[str]:
    """
    Using Breadth First Search, find the path between start and end
    """
    # traverse the entire graph using BFS
    graph.bfs(start)
    graph.view()
    # return __find_path(graph, start, end)
    return [start, end]


def __find_path(graph: IGraph, start: str, end: str) -> List[str]:
    """
    After BFS, extract the path from start to end
    """
    if start == end:
        return [start]

    # Traverse till end's parent and then add 'end' node
    e: Vertex = graph.get_vertex(end)
    result: List[str] = __find_path(graph, start, e.parent)
    result.append(end)
    return result
