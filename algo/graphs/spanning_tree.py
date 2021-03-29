"""
Spanning Tree Implementation
"""
import logging as log
import sys

from algo.priority_queue import PriorityQueue as PQ

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

    queue: PQ[Vertex] = init_priority_queue(graph)

    while not queue.empty():
        _, vertex = queue.get()

        # this edge is choosen
        if vertex.parent:
            edge: Edge = vertex.parent.edge(vertex)
            edge.state = State.PROCESSED

        for neigh in vertex.neighbours():
            if already_added(neigh, queue):
                # this avoids circular edges in MST
                continue

            # in shortest path we use the full distance
            # in mst we just use the edge weight alone
            cost = vertex.weight(neigh)
            if cost < neigh.distance:
                neigh.parent = vertex
                neigh.distance = cost
                # update the priority queue
                queue.update(neigh.id, cost)


def already_added(vertex: Vertex, queue: PQ[Vertex]):
    """
    Check if the vertex has been added to the spanning tree
    """
    return vertex.id not in queue


def init_priority_queue(graph: IGraph) -> PQ[Vertex]:
    """
    Initialize the priority queue
    """
    # the one with the smallest priority wins
    queue: PQ[Vertex] = PQ[Vertex](reverse=True)
    for v in graph:
        queue.insert(v.id, v.distance, v)
    return queue
