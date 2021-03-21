"""
State Enumeration for processing Vertex and Edge
"""

from enum import Enum, auto, unique


@unique
class State(Enum):
    """
    State Enum for vertices and edges
    """
    UNDISCOVERED = auto()
    DISCOVERED = auto()
    PROCESSED = auto()

    def get_color(self):
        """
        Return the color associate with the State
        """
        if self is State.PROCESSED:
            return 'red'
        if self is State.DISCOVERED:
            return 'gray'
        # default to 'black'
        return 'black'
