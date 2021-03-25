"""
Implementation of Shortest path algorithms
"""
import logging as log

from algo.graphs.igraph import IGraph


def dijkstra(graph: IGraph, source: str) -> IGraph:
    """
    Single source shortest path using dijkstra's algorithm
    """
    log.info('Implementing dijkstra\'s algorihm on %s from %s',
             graph.name,
             source)
    return graph
