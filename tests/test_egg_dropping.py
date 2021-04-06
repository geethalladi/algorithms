# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from algo.egg_dropping import egg_dropping


class TestEggDropping:
    """
    A Test Suite for egg_dropping
    """

    def test_empty(self):
        assert egg_dropping(2, 100) == 50
