# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from algo.sub_sequence import longest_common_subsequence as lcb


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
