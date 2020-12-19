# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from algo.binary_search import binary_search as search


class TestBinarySearch:
    def test_empty(self):
        assert search([], 1) == -1

    def test_not_present(self):
        assert search([1, 2, 3, 4, 5], -2) == -1

    def test_single_element(self):
        assert search([1], 1) == 0

    def test_multiple_elements_found(self):
        assert search([1, 3, 5, 7, 9, 11], 3) == 1

    def test_multiple_elements_not_found(self):
        assert search([1, 3, 5, 7, 9, 11], 12) == -1

    def test_multiple_elements_not_found2(self):
        assert search([1, 3, 5, 7, 9, 11], -1) == -1
        
