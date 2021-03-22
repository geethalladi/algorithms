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


class GraphTraversalMixin:
    """
    Mixin providing Graph Traversal Implementation
    """

    # TODO: dirty hack to make num_connect_components work
    num_connect_components: int = 0

    def bfs(self: IGraph, start: str):
        """
        Breadth First Search based traversal
        from the given start node
        """
        assert len(start) > 0, 'Empty start key {}'.format(start)
        v: Vertex = self.get_vertex(start)
        assert v is not None, 'Invalid start key {}'.format(start)

        log.info('Starting BFS from %s', start)
        self.clear()

        # Parent is None and distance = 0 (by default)
        vertices: Queue[Vertex] = Queue()
        vertices.put(v)
        # TODO: process_early(vertex)
        v.set_state(State.DISCOVERED)

        while not vertices.empty():
            # self.stop_and_view()
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

        return self

    def dfs(self: IGraph, start: str = None) -> int:
        """
        Depth First Search based traversal
        """
        assert isinstance(self, GraphTraversalMixin), 'Untraversible Graph'

        if start is None:
            return self.__dfs_forest()

        return self.__dfs_single_node(start)

    def __dfs_single_node(self: IGraph, start: str) -> int:
        """
        Depth First Search starting from the given node
        """
        assert isinstance(self, GraphTraversalMixin), 'Untraversible Graph'
        assert len(start) > 0, 'Empty start key {}'.format(start)

        v: Vertex = self.get_vertex(start)
        assert v is not None, 'Invalid start key {}'.format(start)

        # DFS from the given start node
        log.info('Starting DFS from %s', start)
        return self.__dfs_visit(self.get_vertex(start))

    def __dfs_forest(self: IGraph) -> int:
        """
        Depth First Forest Traversal
        """
        # In case, we want to find all the nodes not connected to 'start'
        # do the following. This will generate a breadth first forest
        assert isinstance(self, GraphTraversalMixin), 'Untraversible Graph'

        self.clear()
        time: int = 1  # start from 1 to avoid confusion

        for v in self:
            if v.get_state() == State.UNDISCOVERED:
                self.num_connect_components += 1
                time = self.__dfs_visit(v, time)

        return time

    def __dfs_visit(self, vertex: Vertex, time: int = 1) -> int:
        """
        Visit the given node during DFS Traversal
        """
        assert isinstance(self, IGraph),  'Graph not traversible'
        assert vertex.get_state() == State.UNDISCOVERED

        # Set it as discovered
        log.debug('Vertex %s is %s at %s', vertex, State.DISCOVERED, time)
        vertex.set_state(State.DISCOVERED)
        vertex.discovery, time = time, (time + 1)
        # process vertex early
        if self.helper.process_vertex_early:
            self.helper.process_vertex_early(vertex)

        for nbr in vertex.get_connections():
            # There are more conditions here
            edge: EdgeContainer = vertex.get_edge(nbr)
            edge.state = State.DISCOVERED

            # processing edge here
            if self.helper.process_edge:
                self.helper.process_edge(vertex, nbr, edge)

            # Found a new vertex
            if nbr.get_state() == State.UNDISCOVERED:
                # Only these are the real edges
                # that are walked through in DFS
                edge.state = State.PROCESSED
                # setting the parent
                nbr.set_parent(vertex, edge)
                # recurse with the new edge
                time = self.__dfs_visit(nbr, time)

        # Fully Processed
        log.debug('Vertex %s is %s at %s', vertex, State.PROCESSED, time)
        vertex.set_state(State.PROCESSED)
        vertex.finish, time = time, (time + 1)
        if self.helper.process_vertex_late:
            self.helper.process_vertex_late(vertex)

        return time

    def topological_sort(self: IGraph) -> Sequence[Vertex]:
        """
        Topological sorting of the graph
        """

        def check_cycle(source: Vertex, dest: Vertex, edge: EdgeContainer):
            log.info('Checking cycles in %s, %s, %s', source, dest, edge)
            if dest.get_state() == State.DISCOVERED:
                msg = 'Cycle exists between {} and {}'.format(source, dest)
                raise Exception(msg)

        self.set_helper(TraversalHelper(process_edge=check_cycle))
        # do a Depth First Search (Forest style)
        self.dfs()
        return sorted(self, key=lambda v: v.finish, reverse=True)
