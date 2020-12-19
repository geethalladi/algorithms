import pytest

from algo.binary_search import binary_search as search


class TestBinarySearch:
    def test_empty(self):
        assert search([], 1, 0, 0) == -1
