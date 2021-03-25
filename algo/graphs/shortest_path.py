"""
Implementation of Shortest path algorithms
"""
import logging as log

from dataclasses import dataclass, field
from queue import PriorityQueue, Queue

from algo.graphs.igraph import IGraph
from algo.graphs.vertex import Vertex

# Only expose these methods
__all__ = ['dijkstra']


@dataclass(order=True)
class WeightedVertex:
    """
    Weighted Vertex for use in PriorityQueue
    """
    distance: int
    vertex: Vertex = field(compare=False)


def dijkstra(graph: IGraph, source: str) -> IGraph:
    """
    Single source shortest path using dijkstra's algorithm
    """

    assert source in graph, 'Source {} not in graph'.format(source)

    # TODO: Do we need to clone this graph
    log.info('Implementing dijkstra\'s algorihm on %s from %s',
             graph.name,
             source)
    # Clear the contents of the graph
    graph.clear()
    init_distance(graph)
    graph.get_vertex(source).distance = 0

    # Insert all the vertex into a PQ
    # WeightedVertex = Tuple[int, Vertex]
    queue: Queue = PriorityQueue()
    for v in graph:
        queue.put(WeightedVertex(v.distance, v))

    return graph


def init_distance(graph: IGraph):
    """
    Initialize distance of every vertex to infinity
    """
    pass
