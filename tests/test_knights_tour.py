# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from algo.knights_tour import knights_tour


class TestKnightsTour:
    """
    A Test Suite for KnightsTour
    """

    def test_empty(self):
        assert 1 == 1

    def test_knights_tour(self):
        knights_tour(8)
