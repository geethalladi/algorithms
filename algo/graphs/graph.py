from typing import Dict

import Vertex

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
        selt.numVertices: int = 0
