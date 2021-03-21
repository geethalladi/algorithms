"""
Graph Traversal Implementation
"""
import logging as log
from queue import Queue

from algo.graphs.igraph import IGraph
from algo.graphs.vertex import Vertex
from algo.graphs.vertex import State as VState


class GraphTraversalMixin:
    """
    Mixin providing Graph Traversal Implementation
    """

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
        v.set_state(VState.DISCOVERED)

        while not vertices.empty():
            # self.stop_and_view()
            current: Vertex = vertices.get()
            log.debug('Processing node %s', current.id)
            for succ in current.get_connections():
                # If this is a new node
                if succ.state == VState.UNDISCOVERED:
                    # Mark it as newly discovered
                    succ.set_state(VState.DISCOVERED)
                    vertices.put(succ)
                    # set the parent
                    succ.set_parent(current, 1)

            # Mark it as PROCESSED
            current.set_state(VState.PROCESSED)

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
        time: int = 0

        for v in self:
            if v.get_state() == VState.UNDISCOVERED:
                time = self.__dfs_visit(v, time)

        return time

    def __dfs_visit(self, vertex: Vertex, time: int = 0) -> int:
        """
        Visit the given node during DFS Traversal
        """
        assert vertex.get_state() == VState.UNDISCOVERED

        log.info('Vertex %s is %s at %s', vertex, VState.DISCOVERED, time)

        # Set it as discovered
        vertex.set_state(VState.DISCOVERED)
        vertex.discovery = time
        time += 1

        for nbr in vertex.get_connections():
            # Found a new vertex
            if nbr.get_state() == VState.UNDISCOVERED:
                nbr.parent = vertex.id
                time = self.__dfs_visit(nbr, time)

        log.info('Vertex %s is %s at %s', vertex, VState.PROCESSED, time)

        # Fully Processed
        vertex.set_state(VState.PROCESSED)
        vertex.finish = time
        time += 1

        return time
