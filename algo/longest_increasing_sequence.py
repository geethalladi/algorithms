"""
Given a list of numbers, find the longest increasing sequence

Using dynamic programming technique to solve this problem
"""

import logging as log

from dataclasses import dataclass
from typing import List, Tuple

__all__ = ['longest_increasing_sequence']


@dataclass
class Cell:
    """
    ADT for storing data in the table (DP)
    """
    element: int
    size: int
    parent: int = -1


def longest_increasing_sequence(nums: List[int]) -> List[int]:
    """
    Return the longest increasing sequence in the given input.

    Uses Dynamic Programming recurrence to solve the problem. At each
    index 'i' store the size of the longest sequence, ending at that
    index. This size is computed by looking at the previous longest
    sequence whose largest element is less than the given element,
    `nums[i]`.

    The DP stores all the possible longest sequence ending at each
    index. The final result is obtained by finding the maximum of
    these sizes.

    Once the end index is identified, the parent property can be used
    to traceback the exact sequence.

    """
    assert len(nums) > 0, 'Empty sequence'

    table: List[Cell] = []
    table.append(Cell(nums[0], 1, -1))

    for i in range(1, len(nums)):
        element: int = nums[i]
        (size, index) = __find_longest_sequence(table, i, element)
        # add one more to the existing (longest) sequence
        table.append(Cell(element, size + 1, index))

    # find the max longest sequence with index
    (index, r) = max(enumerate(table), key=lambda x: x[1].size)

    result = __get_sequence(table, index)
    assert len(result) == r.size, 'Longest sequence does not match'

    return result


def __find_longest_sequence(table: List[Cell], index: int, element: int) -> Tuple[int, int]:
    """
    Find the longest sequence in range [0, i) whose values are less
    than the given element
    """
    # chose only cells whose value is less than the given element
    cells = list(filter(lambda c: c.element <= element, table[0:index]))
    if len(cells) == 0:
        # if none match, then
        # the default size is 0
        # parent index is -1
        return (0, -1)

    (end, result) = max(enumerate(cells), key=lambda x: x[1].size)
    log.debug('Max for %s is (%s, %s) ', index, result.size, end)
    return (result.size, end)


def __get_sequence(table: List[Cell], index: int) -> List[int]:
    """
    Recursively reconstruct the entire sequence
    """
    if index == -1:
        return []

    result: List[int] = __get_sequence(table, table[index].parent)
    result.append(table[index].element)
    return result
