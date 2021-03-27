"""
Graph Traversal Implementation
"""
import logging as log
from queue import Queue
from typing import Sequence

from algo.graphs.igraph import IGraph
from algo.graphs.traversal_helper import TraversalHelper
from algo.graphs.state import State
from algo.graphs.vertex import Vertex, EdgeContainer


def bfs(graph: IGraph, start: str):
    """
    Breadth First Search based traversal
    from the given start node
    """
    assert len(start) > 0, 'Empty start key {}'.format(start)
    v: Vertex = graph.get_vertex(start)
    assert v is not None, 'Invalid start key {}'.format(start)

    log.info('Starting BFS from %s', start)
    graph.clear()

    # Parent is None and distance = 0 (by default)
    vertices: Queue = Queue()
    vertices.put(v)
    # TODO: process_early(vertex)
    v.set_state(State.DISCOVERED)

    while not vertices.empty():
        # graph.stop_and_view()
        current: Vertex = vertices.get()

        log.debug('Processing node %s', current.id)
        for succ in current.get_connections():
            # If this is a new node
            if succ.state == State.UNDISCOVERED:
                # Mark it as newly discovered
                succ.set_state(State.DISCOVERED)
                # TODO: process_early(vertex)
                vertices.put(succ)

                edge: EdgeContainer = current.get_edge(succ)
                # process_edge
                log.debug('Processing edge between (%s, %s)',
                          current.id, succ.id)
                edge.state = State.PROCESSED
                # set the parent
                succ.set_parent(current, edge)

        # Mark it as PROCESSED
        current.set_state(State.PROCESSED)
        # TODO: process_late(vertex)

    return graph


def __dfs_single_node(graph: IGraph, start: str) -> int:
    """
    Depth First Search starting from the given node
    """
    assert len(start) > 0, 'Empty start key {}'.format(start)

    v: Vertex = graph.get_vertex(start)
    assert v is not None, 'Invalid start key {}'.format(start)

    # DFS from the given start node
    log.info('Starting DFS from %s', start)
    return __dfs_visit(graph, graph.get_vertex(start))


def topological_sort(graph: IGraph) -> Sequence[Vertex]:
    """
    Topological sorting of the graph
    """

    def check_cycle(source: Vertex, dest: Vertex, edge: EdgeContainer):
        log.info('Checking cycles in %s, %s, %s', source, dest, edge)
        if dest.get_state() == State.DISCOVERED:
            msg = 'Cycle exists between {} and {}'.format(source, dest)
            raise Exception(msg)

    graph.set_helper(TraversalHelper(process_edge=check_cycle))
    # do a Depth First Search (Forest style)
    dfs(graph)
    return sorted(graph, key=lambda v: v.finish, reverse=True)


def dfs(graph: IGraph, start: str = None) -> int:
    """
    Depth First Search based traversal
    """
    if start is None:
        return __dfs_forest(graph)

    return __dfs_single_node(graph, start)


def __dfs_forest(graph: IGraph) -> int:
    """
    Depth First Forest Traversal
    """
    # In case, we want to find all the nodes not connected to 'start'
    # do the following. This will generate a breadth first forest

    graph.clear()
    time: int = 1  # start from 1 to avoid confusion

    for v in graph:
        if v.get_state() == State.UNDISCOVERED:
            graph.num_connect_components += 1
            time = __dfs_visit(graph, v, time)

    return time


def __dfs_visit(graph: IGraph, vertex: Vertex, time: int = 1) -> int:
    """
    Visit the given node during DFS Traversal
    """
    assert vertex.get_state() == State.UNDISCOVERED

    # Set it as discovered
    log.debug('Vertex %s is %s at %s', vertex, State.DISCOVERED, time)
    vertex.set_state(State.DISCOVERED)
    vertex.discovery, time = time, (time + 1)
    # process vertex early
    if graph.helper.process_vertex_early:
        graph.helper.process_vertex_early(vertex)

    for nbr in vertex.get_connections():
        # # processing edge here
        # # can process edge twice
        # if graph.helper.process_edge:
        #     graph.helper.process_edge(vertex, nbr, edge)

        # Ideal Condition
        # To make sure edge is processed only once
        edge: EdgeContainer = vertex.get_edge(nbr)
        if ((nbr.get_state() == State.DISCOVERED) or graph.directed):
            # only process edge (leave the vertex)
            edge.state = State.DISCOVERED
            if graph.helper.process_edge:
                graph.helper.process_edge(vertex, nbr, edge)

        # found new vertex: process both edge and vertex
        if nbr.get_state() == State.UNDISCOVERED:
            # setting the parent
            nbr.set_parent(vertex, edge)

            edge.state = State.DISCOVERED
            if graph.helper.process_edge:
                graph.helper.process_edge(vertex, nbr, edge)

            # Only these are the real edges
            # that are walked through in DFS
            edge.state = State.PROCESSED

            # recurse with the new edge
            time = __dfs_visit(graph, nbr, time)

    # Fully Processed
    log.debug('Vertex %s is %s at %s', vertex, State.PROCESSED, time)
    vertex.set_state(State.PROCESSED)
    vertex.finish, time = time, (time + 1)
    if graph.helper.process_vertex_late:
        graph.helper.process_vertex_late(vertex)

    return time
