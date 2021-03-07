from typing import Dict

import logging as log
log.basicConfig(level=log.INFO)

class Vertex:
    """
    Vertex using adjacency list representation
    """
    
    def __init__(self: Vertex, key: str):
        """
        Initialize the Vertex instance
        """
        self.id: str = key
        self.connectedTo: Dict[str, int] = {}


    def getId(self) -> int:
        """
        Return the identifier of this vertex
        """
        return self.id
        
