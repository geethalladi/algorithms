import pytest

import os; print(os.getcwd())

from algo.binary_search import binary_search as bs

class TestBinarySearch:
    def test_element_not_found(self):
        assert bs([], 1, 0, 0) == -1
