# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

import logging
from algo.sub_sequence import longest_common_subsequence as lcb
from algo.sub_sequence import max_monotonically_increasing as mono


class TestSubsequence:
    """
    A Test Suite for subsequence
    """

    def test_same(self):
        assert lcb('hello', 'hello') == 'hello'

    def test_example(self):
        assert lcb('demo', 'repu') == 'e'
        assert lcb('democrat', 'republican') == 'eca'
        assert lcb('yyabczzdexx', 'zzabxxcdeyy') == 'abcde'

    def test_monotonic_sequence(self):


 assert mono([1, 4, 2, 3, 5, 8, 6, 7, 9]) == [1, 2, 3, 5, 6, 7, 9]
