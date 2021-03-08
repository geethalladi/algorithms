# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from algo.graphs.vertex import Vertex

class TestVertex:
    """
    A Test Suite for Vertex
    """
    def test_empty(self):
        v = Vertex('v')
        assert v != None
        
