from typing import Dict

# TODO: This should be a sibling package
from algo.graphs.vertex import Vertex

class Graph:
    """
    An abstract data type for representing Graphs.
    This implementation uses the adjacency list representation.
    """
    
    def __init__(self):
        """
        Create a graph instance based on adjacency list
        """
        self.vertices: Dict[id, Vertex] = {}
        self.numVertices: int = 0

print(Graph)
