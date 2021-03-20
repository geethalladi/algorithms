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

    def dfs(self: IGraph, start: str):
        """
        Depth First Search based traversal
        from the given start node
        """
        assert len(start) > 0, 'Empty start key {}'.format(start)
        v: Vertex = self.get_vertex(start)
        assert v is not None, 'Invalid start key {}'.format(start)

        log.info('Starting DFS from %s', start)
        self.clear()
        return self
