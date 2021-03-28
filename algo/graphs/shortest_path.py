"""
Implementation of Shortest path algorithms
"""
import sys
import logging as log

from typing import List

from algo.graphs.edge import Edge
from algo.graphs.igraph import IGraph
from algo.graphs.vertex import Vertex

# Only expose these methods
__all__ = ['dijkstra']


def dijkstra(graph: IGraph, source: str) -> IGraph:
    """
    Single source shortest path using dijkstra's algorithm
    """

    assert source in graph, 'Source {} not in graph'.format(source)

    # TODO: Do we need to clone this graph
    log.info('Implementing dijkstra\'s algorihm on %s from %s',
             graph.name,
             source)
    # Initialize the graph' state
    graph.clear()
    for v in graph:
        v.distance = sys.maxsize

    graph.get_vertex(source).distance = 0

    # Insert all the vertex into a PQ
    # WeightedVertex = Tuple[int, Vertex]
    # Using a list for now
    # Switch to a min-heap
    queue: List[Vertex] = list(graph)

    while len(queue) > 0:
        v = minimum(queue)
        log.debug('Using vertex %s with distance %s', v, v.distance)
        for neighbour in v.neighbours():
            edge: Edge = v.edge(neighbour)
            distance = v.distance + edge.weight

            # if distance is less than the existing distance
            # then update
            if distance < neighbour.distance:
                log.debug('Setting the new weight of %s to %s',
                          neighbour, distance)
                neighbour.set_parent(v, edge)
                neighbour.distance = distance
                # update the heap

    return graph


def minimum(queue: List[Vertex]) -> Vertex:
    """
    Return the vertex with the smallest distance
    """
    assert len(queue) > 0, 'Empty Vertices'

    i, v = 0, queue[0]
    for j in range(1, len(queue)):
        w = queue[j]
        if w.distance < v.distance:
            i, v = j, w

    return queue.pop(i)
