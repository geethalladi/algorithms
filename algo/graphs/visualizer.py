"""
GraphViewMixin
"""

import logging as log
from typing import Union

import graphviz  # type: ignore

from algo.graphs.edge import Edge
from algo.graphs.igraph import IGraph
from algo.graphs.vertex import Vertex

GraphView = Union[IGraph, 'GraphViewMixin']

__all__ = ['GraphViewMixin']


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
    def __add_node(cls, vertex: Vertex, dot: graphviz.Graph):
        """
        Add nodes to the dot representation
        """
        log.debug('Adding nodes to dot representation')
        dot.node(vertex.id, str(vertex),
                 color=cls.color(vertex))

    @classmethod
    def color(cls, v: Vertex) -> str:
        """
        Return the color of the vertex
        """
        if v.color:
            return v.color
        return v.state.color()

    @classmethod
    def __is_edge_required(cls, source: Vertex, dest: Vertex, directed: bool):
        # Always add if the graph is directed
        if directed:
            return True
        # If undirected add only once
        # add only from source to dest
        return source.id <= dest.id

    @classmethod
    def __add_edge(cls, source: Vertex, dest: Vertex, directed: bool, dot: graphviz.Graph):
        if not cls.__is_edge_required(source, dest, directed):
            log.debug('Ignoring redundant edge %s -> %s', source.id, dest.id)
            return

        log.debug("Adding edge between %s and %s", source.id, dest.id)

        edge: Edge = source.edge(dest)
        color: str = edge.state.color()

        if edge.weight == 1:
            # Ignore unit weights while viewing
            dot.edge(source.id, dest.id, color=color)
        else:
            dot.edge(source.id, dest.id, label=str(edge.weight), color=color)

    def to_dot(self: GraphView):
        """
        Returns the Graphviz#dot representation
        """
        if isinstance(self, IGraph) and isinstance(self, GraphViewMixin):
            dot = self.__construct_dot_instance(self.name, self.directed)
            # Adding nodes
            for v in self.get_vertices():
                self.__add_node(self.get_vertex(v), dot)
            # Adding all edges
            log.debug('Adding edges to dot representation')
            for v in self.get_vertices():
                source = self.get_vertex(v)
                # Adding edges from vertex v
                log.debug('Adding edges in vertex %s', source.id)
                for dest in source.neighbours():
                    self.__add_edge(source, dest, self.directed, dot)
            return dot
        msg: str = 'GraphType {} is not compatible'.format(type(self))
        raise AssertionError(msg)

    def visualize(self: IGraph):
        """
        Visualize this graph
        """
        dot = self.to_dot()
        return dot.view()
