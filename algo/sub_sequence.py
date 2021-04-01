"""
Implementation of longest common subsequence
"""

import logging as log

from dataclasses import dataclass
from typing import Any, List


__all__ = ['longest_common_subsequence',
           'max_monotonically_increasing']


@dataclass
class Cell:
    """
    ADT for Cell
    """
    cost: int = 0
    op: str = 'M'
    seq: str = ''
    parent: Any = None

    def __repr__(self):
        return '({}, {}, {})'.format(self.seq, self.parent, self.cost)


def longest_common_subsequence(left: str, right: str) -> str:
    """
    Return the longest common subsequence between left and right

    The procedure is an extension of edit_distance using Dynamic Programming.
    The only difference is substitution of characters (in edit_distance) is
    not allowed, and hence made a very costly operation. The other operations
    (matching, insert, deletion) are allowed. The cost of matching is zero.
    Whereas the cost of inserting and deleting one character is one each.

    The Longest Common Subsequence is the one which has most matching characters.
    Since the cost of matching is zero and substitution is not allowed, the lcb
    is the one obtained by least number of insertion and deletion

    This DP tries to optimize to minimize this cost and use this optimization to
    compute the result.
    """

    # for 1 based index and simplifying table access
    left, right = (' ' + left), (' ' + right)
    rows, cols = len(left), len(right)

    # initialize everything
    table: List[List[Cell]] = init_table(rows, cols)

    # 0 cost change
    table[0][0] = Cell(0)

    #  inserting everything to get the right
    for j in range(1, cols):
        # costs 'j' to insert j characters
        table[0][j] = Cell(j, 'I')

    # delete everything in left to get right
    for i in range(1, rows):
        # costs 'i' to delete 'i' characters
        table[i][0] = Cell(i, 'D')

    for i in range(1, rows):
        for j in range(1, cols):
            # match
            match = None
            if left[i] == right[j]:
                match = Cell((table[i - 1][j - 1].cost) + 0,
                             'M',
                             table[i - 1][j - 1].seq + left[i],
                             (i - 1, j - 1))
            else:
                # Substitution is not allowed
                # and hence the cost is made very high
                match = Cell((table[i - 1][j - 1].cost) + rows,
                             'S',
                             table[i - 1][j - 1].seq, (i - 1, j - 1))

            # insert
            insert = Cell((table[i][j - 1].cost + 1),  # 1 for insertion
                          'I',
                          table[i][j - 1].seq,
                          (i, j - 1))

            # delete
            delete = Cell((table[i - 1][j].cost + 1),  # 1 for deletion
                          'D',
                          table[i - 1][j].seq,
                          (i - 1, j))

            result = match
            for op in [insert, delete]:
                if op.cost < result.cost:
                    result = op

            table[i][j] = result

    return table[rows - 1][cols - 1].seq


def init_table(rows: int, cols: int) -> List[List[Cell]]:
    """
    Initialize the table
    """
    table: List[List[Cell]] = []
    for i in range(0, rows):
        table.append([])
        for _ in range(0, cols):
            table[i].append(Cell())
    return table


def max_monotonically_increasing(nums: List[int]) -> List[int]:
    """
    Return the maximum monotonically increasing sub sequence

    Using Longest Common Subsequence as an abstraction. The problem
    of finding maximum monotonically increasing subsequence can be
    converted to LC subsequence between the original string and the
    string of sorted numbers. The longest common subsequence of this
    input becomes the required result
    """
    assert all([(0 <= n <= 9)
                for n in nums]), 'Input is expected to be single digit'

    left: str = ''.join([str(n) for n in nums])
    right: str = ''.join(sorted([str(n) for n in nums]))

    result = longest_common_subsequence(left, right)
    log.info(result)

    return [int(c) for c in list(result)]
