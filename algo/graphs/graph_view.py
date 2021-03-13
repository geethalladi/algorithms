"""
GraphViewMixin
"""

import logging as log
from typing import Collection

import graphviz

from algo.graphs.igraph import IGraph


class GraphViewMixin:
    """
    Mixin for visualizing Graphs
    """

    @classmethod
    def __construct_dot_instance(cls, name: str, directed: bool):
        if directed:
            log.info('Constructing a digraph instance for %s', name)
            return graphviz.Digraph(name=name, comment='Graph Visualization')
        log.info('Constructing a undirected graph instance for %s', name)
        return graphviz.Graph(name=name, comment='Graph Visualization')

    @classmethod
    def __add_nodes(cls, vertices: Collection[str], dot: graphviz.Graph):
        """
        Add nodes to the dot representation
        """
        log.debug('Adding nodes to dot representation')
        for v in vertices:
            dot.node(v, v)

    def view(self: IGraph):
        """
        Visualize this graph
        """
        dot = GraphViewMixin.__construct_dot_instance(self.name, self.directed)
        # Adding nodes
        GraphViewMixin.__add_nodes(self.get_vertices(), dot)

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
