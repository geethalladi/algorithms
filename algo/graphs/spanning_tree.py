"""
Spanning Tree Implementation
"""
import sys

from typing import List

from algo.graphs.edge import Edge
from algo.graphs.igraph import IGraph
from algo.graphs.state import State
from algo.graphs.vertex import Vertex

__all__ = ['prim']


def prim(graph: IGraph, start: str):
    """
    Prim's Minimal Spanning Tree
    """
    assert start, 'Empty Start Vertex'
    assert start in graph, 'Start Vertex not part of graph'

    for v in graph:
        v.distance = sys.maxsize
        v.parent = None

    graph.get_vertex(start).distance = 0

    queue: List[Vertex] = list(graph)

    while len(queue) > 0:
        vertex: Vertex = minimum(queue)
        # this edge is choosen
        if vertex.parent:
            edge: Edge = vertex.parent.edge(vertex)
            edge.state = State.PROCESSED

        for neigh in vertex.neighbours():
            cost = vertex.weight(neigh)
            if neigh not in queue:
                # this avoids circular edges in MST
                continue
            if cost < neigh.distance:
                neigh.parent = vertex
                neigh.distance = cost


def minimum(queue: List[Vertex]) -> Vertex:
    """
    Chose the one with the minimum distance
    """
    assert len(queue) > 0, 'Empty PQ in prim'

    index, v = 0, queue[0]
    for i in range(1, len(queue)):
        w = queue[i]
        if w.distance < v.distance:
            index, v = i, w

    return queue.pop(index)
