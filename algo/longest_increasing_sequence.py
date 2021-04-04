"""
Given a list of numbers, find the longest increasing sequence

Using dynamic programming technique to solve this problem
"""

import logging as log

from dataclasses import dataclass
from typing import List

__all__ = ['longest_increasing_sequence']


@dataclass
class Cell:
    size: int
    element: int
    parent: int = -1


def longest_increasing_sequence(xs: List[int]) -> List[int]:
    assert len(xs) > 0, 'Empty sequence'

    table: List[Cell] = []
    table.append(Cell(1, xs[0], -1))

    for i in range(1, len(xs)):
        element: int = xs[i]
        (max, index) = find_max_size(table, i, element)
        table.append(Cell(max + 1, element, index))

    (max, index) = find_max(table)

    result = get_sequence(table, index)

    assert len(result) == max
    return result


def find_max_size(table: List[Cell], index: int, element: int):
    max_size, max_index = 0, -1

    for i in range(0, index):
        if (table[i].element <= element) and table[i].size > max_size:
            max_size, max_index = table[i].size, i

    log.info('Max for %s is (%s, %s) ', index, max_size, max_index)
    return (max_size, max_index)


def find_max(table: List[Cell]):
    max, index = table[0].size, 0

    for i in range(1, len(table)):
        log.info('Index %s has size %s', i, table[i].size)
        if max < table[i].size:
            max, index = table[i].size, i

    return (max, index)


def get_sequence(table: List[Cell], index: int) -> List[int]:
    if table[index].parent == -1:
        e: int = table[index].element
        return [e]

    result: List[int] = get_sequence(table, table[index].parent)
    result.append(table[index].element)
    return result
