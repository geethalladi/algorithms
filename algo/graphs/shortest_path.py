"""
Implementation of Shortest path algorithms
"""
import sys
import logging as log

from dataclasses import dataclass, field
from typing import List

from algo.graphs.igraph import IGraph
from algo.graphs.vertex import Vertex, EdgeContainer

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
    # Using a list for now
    # Switch to a min-heap
    vertices: List[WeightedVertex] = []
    for v in graph:
        vertices.append(WeightedVertex(v.distance, v))

    while len(vertices) > 0:
        v = get_smallest(vertices)
        log.debug('Using vertex %s with distance %s', v, v.distance)
        for neighbour in v.get_connections():
            edge: EdgeContainer = v.get_edge(neighbour)
            distance = v.distance + edge.weight

            # if distance is less than the existing distance
            # then update
            if distance < neighbour.distance:
                log.debug('Setting the new weight of %s to %s',
                          neighbour, distance)
                neighbour.set_parent(v, edge)
                # update the heap
                update_vertex(vertices, neighbour, distance)

    return graph


def update_vertex(vertices: List[WeightedVertex], vertex: Vertex, distance: int):
    """
    Update this vertex's new distance
    """
    for wv in vertices:
        if wv.vertex == vertex:
            wv.distance = distance
            return

    assert False, 'Vertex Weight not updated'


def get_smallest(vertices: List[WeightedVertex]) -> Vertex:
    """
    Return the vertex with the smallest distance
    """
    assert len(vertices) > 0, 'Empty Vertices'
    i, result = 0, vertices[0]
    for j in range(1, len(vertices)):
        wv = vertices[j]
        if wv.distance < result.distance:
            result = wv
            i = j

    vertices.pop(i)
    return result.vertex


def init_distance(graph: IGraph):
    """
    Initialize distance of every vertex to infinity
    """
    for v in graph:
        v.distance = sys.maxsize
