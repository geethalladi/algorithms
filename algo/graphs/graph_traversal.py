"""
Graph Traversal Implementation
"""
import logging as log
from queue import Queue


from algo.graphs.igraph import IGraph
from algo.graphs.vertex import Vertex, EdgeContainer
from algo.graphs.state import State


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

                    # process_edge
                    log.info('Processing edge between (%s, %s)',
                             current.id, succ.id)
                    edge: EdgeContainer = current.get_edge(succ)
                    edge.state = State.PROCESSED
                    # set the parent and the distance
                    succ.set_parent(current, edge.weight)

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
        assert vertex.get_state() == State.UNDISCOVERED

        # Set it as discovered
        log.info('Vertex %s is %s at %s', vertex, State.DISCOVERED, time)
        vertex.set_state(State.DISCOVERED)
        vertex.discovery, time = time, (time + 1)
        # TODO: process_early(vertex)

        for nbr in vertex.get_connections():
            # Found a new vertex
            if nbr.get_state() == State.UNDISCOVERED:
                # processing edge here
                edge: EdgeContainer = vertex.get_edge(nbr)
                edge.state = State.PROCESSED
                # setting the parent and distance
                nbr.set_parent(vertex, edge.weight)
                time = self.__dfs_visit(nbr, time)

        # Fully Processed
        log.info('Vertex %s is %s at %s', vertex, State.PROCESSED, time)
        vertex.set_state(State.PROCESSED)
        vertex.finish, time = time, (time + 1)
        # process_late(vertex)

        return time
