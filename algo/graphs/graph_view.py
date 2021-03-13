"""
GraphViewMixin
"""

import graphviz
import logging as log

from algo.graphs.igraph import IGraph


class GraphViewMixin:
    """
    Mixin for visualizing Graphs
    """

    def view(self: IGraph):
        """
        Visualize this graph
        """

        if self.directed:
            log.info('Constructing a digraph instance for %s', self.name)
            dot = graphviz.Digraph(
                name=self.name, comment='Graph Visualization')
        else:
            log.info('Constructing a undirected graph instance for %s', self.name)
            dot = graphviz.Graph(name=self.name, comment='Graph Visualization')

        # Adding nodes
        log.debug('Adding nodes to dot representation')
        for v in self.get_vertices():
            dot.node(v, v)

        # Adding all edges
        log.debug('Adding edges to dot representation')
        for v in self.get_vertices():
            source = self.get_vertex(v)
            # Adding edges from vertex v
            log.debug('Adding edges in vertex %s', source.get_id())
            for dest in source.get_connections():
                # Always add if the graph is directed
                # If undirected add only once
                # add only from source to dest
                if self.directed or (source.get_id() <= dest.get_id()):
                    log.debug("Adding edge between %s and %s",
                              source.get_id(), dest.get_id())
                    weight = source.get_weight(dest)
                    dot.edge(source.get_id(), dest.get_id(), label=str(weight))

        return dot.view()
