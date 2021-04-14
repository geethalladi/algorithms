"""
Graph Traversal Implementation
"""
import logging as log
from dataclasses import dataclass
from queue import Queue
from typing import Callable, Optional


from algo.graphs.edge import Edge, EdgeType
from algo.graphs.igraph import IGraph
from algo.graphs.state import State
from algo.graphs.vertex import Vertex

__all__ = ['breadth_first_search', 'depth_first_search', 'Hooks',
           'classify_edge']


@dataclass
class Hooks:
    """
    Container Type with hooks for processing
    """
    process_vertex_early: Optional[Callable[[Vertex], None]] = None
    process_vertex_late: Optional[Callable[[Vertex], None]] = None
    process_edge: Optional[Callable[[Vertex, Vertex, Edge], None]] = None


def breadth_first_search(graph: IGraph, start: str):
    """
    Breadth First Search based traversal
    from the given start node
    """
    assert len(start) > 0, 'Empty start key {}'.format(start)
    v: Vertex = graph.get_vertex(start)
    assert v is not None, 'Invalid start key {}'.format(start)

    log.debug('Starting BFS from %s', start)
    graph.clear()

    # Parent is None and distance = 0 (by default)
    vertices: Queue = Queue()
    vertices.put(v)
    # TODO: process_early(vertex)
    v.state = State.DISCOVERED

    while not vertices.empty():
        # graph.view(pause = True)
        current: Vertex = vertices.get()

        log.debug('Processing node %s', current.id)
        for succ in current.neighbours():
            # If this is a new node
            if succ.state == State.UNDISCOVERED:
                # Mark it as newly discovered
                succ.state = State.DISCOVERED
                # TODO: process_early(vertex)
                vertices.put(succ)

                edge: Edge = current.edge(succ)
                # process_edge
                log.debug('Processing edge between (%s, %s)',
                          current.id, succ.id)
                edge.state = State.PROCESSED
                # set the parent
                succ.set_parent(current, edge)

        # Mark it as PROCESSED
        current.state = State.PROCESSED
        # TODO: process_late(vertex)

    return graph


def depth_first_search(graph: IGraph, start: str = None, hooks: Hooks = Hooks()) -> int:
    """
    Depth First Search based traversal
    """
    if start is None:
        return dfs_forest(graph, hooks)

    return dfs_single_node(graph, start, hooks)


def dfs_single_node(graph: IGraph, start: str, hooks: Hooks) -> int:
    """
    Depth First Search starting from the given node
    """
    assert len(start) > 0, 'Empty start key {}'.format(start)

    v: Vertex = graph.get_vertex(start)
    assert v is not None, 'Invalid start key {}'.format(start)

    # DFS from the given start node
    log.debug('Starting DFS from %s', start)
    return dfs_visit(graph, graph.get_vertex(start), 1, hooks)


def dfs_forest(graph: IGraph, hooks: Hooks) -> int:
    """
    Depth First Forest Traversal
    """
    # In case, we want to find all the nodes not connected to 'start'
    # do the following. This will generate a breadth first forest

    graph.clear()
    time: int = 1  # start from 1 to avoid confusion

    for v in graph:
        if v.state == State.UNDISCOVERED:
            graph.num_connect_components += 1
            time = dfs_visit(graph, v, time, hooks)

    return time


def dfs_visit(graph: IGraph, vertex: Vertex, time: int, hooks: Hooks) -> int:
    """
    Visit the given node during DFS Traversal
    """
    assert vertex.state == State.UNDISCOVERED

    # Set it as discovered
    log.debug('Vertex %s is %s at %s', vertex, State.DISCOVERED, time)
    vertex.state = State.DISCOVERED
    vertex.discovery, time = time, (time + 1)

    # process vertex early
    if hooks.process_vertex_early:
        hooks.process_vertex_early(vertex)

    for nbr in vertex.neighbours():
        # # processing edge here
        # # can process edge twice
        # if hooks.process_edge:
        #     hooks.process_edge(vertex, nbr, edge)

        # Ideal Condition
        # To make sure edge is processed only once
        edge: Edge = vertex.edge(nbr)

        # found new vertex: process both edge and vertex
        if nbr.state == State.UNDISCOVERED:
            # setting the parent
            nbr.set_parent(vertex, edge)

            assert edge.state == State.UNDISCOVERED
            edge.state = State.DISCOVERED
            if hooks.process_edge:
                hooks.process_edge(vertex, nbr, edge)

            # Only these are the real edges
            # that are walked through in DFS
            edge.state = State.PROCESSED

            # recurse with the new edge
            time = dfs_visit(graph, nbr, time, hooks)

        elif (graph.directed or (not nbr.is_processed())):
            # this avoids reprocessing the edge
            # again from (dest, source)
            if edge.state == State.UNDISCOVERED:
                # only process edge (leave the vertex)
                edge.state = State.DISCOVERED
                if hooks.process_edge:
                    hooks.process_edge(vertex, nbr, edge)

    # Fully Processed
    log.debug('Vertex %s is %s at %s', vertex, State.PROCESSED, time)
    vertex.state = State.PROCESSED
    vertex.finish, time = time, (time + 1)
    if hooks.process_vertex_late:
        hooks.process_vertex_late(vertex)

    return time


def classify_edge(source: Vertex, dest: Vertex) -> EdgeType:
    """
    Classify this edge
    """
    if dest.parent == source:
        return EdgeType.TREE

    # "checking dest's parent is not source" is not required here
    # adding it for the sake of completion
    if (dest.parent != source) and (dest.state == State.DISCOVERED):
        return EdgeType.BACK

    if (dest.state == State.PROCESSED) and (source.discovery < dest.discovery):
        # then source is likely one of its ancestors
        return EdgeType.FORWARD

    if (dest.state == State.PROCESSED) and (source.discovery > dest.discovery):
        return EdgeType.CROSS

    raise AssertionError(f'Invalid edge classification for {source}, {dest}')
