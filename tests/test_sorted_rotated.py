# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from algo.sorted_rotated import find, rotation_index as ri


class TestUnrotated:
    def test_empty(self):
        assert find([], 1) == -1

    def test_not_present(self):
        assert find([1, 2, 3, 4, 5], -2) == -1

    def test_single_element(self):
        assert find([1], 1) == 0

    def test_multiple_elements_found(self):
        assert find([1, 3, 5, 7, 9, 11], 3) == 1

    def test_multiple_elements_not_found(self):
        assert find([1, 3, 5, 7, 9, 11], 12) == -1

    def test_multiple_elements_not_found2(self):
        assert find([1, 3, 5, 7, 9, 11], -1) == -1


class TestSortedRotatedFind:
    def test_empty(self):
        assert find([], 1) == -1

    def test_not_present(self):
        assert find([6, 7, 8, 9, 1, 2, 3, 4, 5], -2) == -1

    def test_single_element(self):
        assert find([1], 1) == 0

    def test_multiple_elements_found(self):
        assert find([13, 15, 16, 17, 18, 19, 20, 1, 3, 5, 7, 9, 11], 3) == 8

    def test_multiple_elements_not_found(self):
        assert find([11, 1, 3, 5, 7, 9], 14) == -1

    def test_multiple_elements_not_found2(self):
        assert find([12, 1, 3, 5, 7, 9, 11], -1) == -1

    def test_rotation_index(self):
        assert ri([1, 2, 3, 4]) == 0

    def test_rotation_index2(self):
        assert ri([5, 6, 1, 2, 3, 4]) == 2
