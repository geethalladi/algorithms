"""
Given a sorted array, which is rotated
find the index of the given element.
"""

import logging as log

from typing import List

from algo.binary_search import search

__all__ = ['find', 'rotation_index']


def find(elements: List[int], key: int) -> int:
    """
    The input is a sorted array, but has
    been rotated a few times. Find the position
    of the given element
    """
    if len(elements) <= 0:
        log.debug('Empty array, returning default value')
        return -1

    # Position where the smallest element is found
    pos: int = rotation_index(elements)

    # (0, pos-1), (pos, len-1)
    i = search(elements, key, 0, pos - 1)
    j = search(elements, key, pos, len(elements) - 1)
    if i == -1 and j == -1:
        log.debug('Element %s not found', key)
        return -1
    if i == -1:
        return j

    return i


def rotation_index(elements: List[int]) -> int:
    """
    In the given rotated sorted array, find the
    position of rotation. It's also the position
    of the smallest element.
    """
    low, high = 0, len(elements) - 1
    mid = (low + high) // 2

    # Flaw: Fails for [5, 5, 5, 5, 5, 5, 5, 3, 5]
    # Assumption the list will not have duplicates
    if (elements[low] <= elements[mid]) and (elements[mid] <= elements[high]):
        log.debug('No rotation found in [%s, %s, %s]', low, mid, high)
        return 0

    while low <= high:
        mid = (low + high) // 2
        # Check rotation around mid on both sides
        # Since mid will not be part of next iteration
        # we have to check if rotation is around mid
        # on both the sides
        if __is_rotation_point(elements, mid):
            return mid
        if __is_rotation_point(elements, mid + 1):
            return mid + 1
        if elements[low] > elements[mid]:
            high = mid - 1
        else:
            low = mid + 1

    raise AssertionError(f"Unable to find rotation in {elements}")


def __is_rotation_point(elements: List[int], pos: int) -> bool:
    """
    Predicate to check if this is the point of rotation
    """
    n = len(elements)
    pos, previous = pos % n, (pos - 1) % n

    log.debug('Comparing %s, %s', elements[previous], elements[pos])
    # if previous element is more then it is the rotation point
    return elements[previous] > elements[pos]
