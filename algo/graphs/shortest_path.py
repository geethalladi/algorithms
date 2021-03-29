"""
Implementation of Shortest path algorithms
"""
import sys
import logging as log

from algo.priority_queue import PriorityQueue as PQ

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

    queue = init_priority_queue(graph)

    while not queue.empty():
        # Choosing the vertex with shortest
        # distance in this round
        _, v = queue.get()
        log.debug('Using vertex %s with distance %s', v, v.distance)
        for neighbour in v.neighbours():
            edge: Edge = v.edge(neighbour)
            # in shortest path we use the full distance
            # in mst we just use the edge weight alone
            distance = v.distance + edge.weight

            # if distance is less than the existing distance
            # then update
            if distance < neighbour.distance:
                log.debug('Setting the new weight of %s to %s',
                          neighbour, distance)
                neighbour.set_parent(v, edge)
                neighbour.distance = distance
                queue.update(neighbour.id, neighbour.distance)

    return graph


def init_priority_queue(graph: IGraph) -> PQ[Vertex]:
    """
    Initialize the priority_queue
    """
    # return the one with the shortest distance
    queue = PQ[Vertex](reverse=True)

    for v in graph:
        log.debug('Adding %s, %s, %s', v.id, v.distance, v)
        queue.insert(v.id, v.distance, v)

    return queue
