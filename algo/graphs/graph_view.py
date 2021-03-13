"""
GraphViewMixin
"""

import graphviz
import logging as log

from algo.graphs.vertex import Vertex
# from algo.graphs.graph import Graph


class GraphViewMixin:
    """
    Mixin for visualizing Graphs
    """

    def __create_dot_instance(self):
        """
        Factory method to create dot instance
        """
        if self.directed:
            log.info('Constructing a digraph instance for %s', self.name)
            return graphviz.Digraph(name=self.name, comment='Graph Visualization')

        log.info('Constructing a undirected graph instance for %s', self.name)
        return graphviz.Graph(name=self.name, comment='Graph Visualization')

    def __add_nodes(self, dot: graphviz.Graph):
        """
        Add all the vertices to the dot representation
        """
        log.debug('Adding nodes to dot representation')
        for v in self.get_vertices():
            dot.node(v, v)

    def __should_add(self, source: Vertex, dest: Vertex):
        """
        Predicate to check if the edge needs to be added to the dot representation
        """
        if self.directed:
            # Always add if the graph is directed
            return True
        # If undirected add only once
        # add only from source to dest
        return (source.get_id() <= dest.get_id())

    def __add_edge(self, dot: graphviz.Graph, source: Vertex, dest: Vertex):
        """
        Add this edge detail to the dot representation
        """
        assert source is not None, "Source is empty"
        assert dest is not None, "Dest is empty"

        log.debug("Adding edge between %s and %s",
                  source.get_id(), dest.get_id())
        weight = source.get_weight(dest)
        dot.edge(source.get_id(), dest.get_id(), label=str(weight))

    def __add_edges_in(self, dot: graphviz.Graph, source: Vertex):
        """
        Add all the edges in the given vertex to the dot representation
        """
        log.debug('Adding edges in vertex %s', source.get_id())
        for dest in source.get_connections():
            if self.__should_add(source, dest):
                self.__add_edge(dot, source, dest)

    def __add_edges(self, dot: graphviz.Graph):
        log.debug('Adding edges to dot representation')
        for v in self.get_vertices():
            self.__add_edges_in(dot, self.vertices[v])

    def to_dot(self):
        """
        Construct a dot representation of the entire graph
        """
        dot: graphviz.Graph = self.__create_dot_instance()
        self.__add_nodes(dot)
        self.__add_edges(dot)
        return dot

    def view(self):
        """
        Visualize this graph
        """
        return self.to_dot().view()
