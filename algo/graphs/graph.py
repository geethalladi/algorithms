from typing import Dict

from vertex import Vertex

class Graph:
    """
    An abstract data type for representing Graphs.
    This implementation uses the adjacency list representation.
    """
    
    def __init__(self):
        """
        Create a graph instance based on adjacency list
        """
        self.verList: Dict[id, Vertex] = {}
        self.numVertices: int = 0
