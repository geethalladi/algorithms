import pytest

from algo.binary_search import binary_search as search


class TestBinarySearch:
    def test_empty(self):
        assert search([], 1, 0, 0) == -1

    def test_not_present(self):
        assert search([1, 2, 3, 4, 5], -2, 0, 4) == -1
