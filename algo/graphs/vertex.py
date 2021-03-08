from typing import Dict

import logging as log
log.basicConfig(level=log.INFO)

class Vertex:
    """
    Vertex using adjacency list representation
    """

    # TODO: How to qualify self here
    def __init__(self, key: str):
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
        

