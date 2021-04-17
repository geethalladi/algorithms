"""
Given a list of sorted numbers find the index of the given
element using "binary search" algorithm. If the element is not
present then return -1.
"""

from typing import List

import logging as log
log.basicConfig(level=log.INFO)

__all__ = ['binary_search', 'search']


def binary_search(elements: List[int], key: int) -> int:
    """
    Returns the index of the `key` inside the `elements`
    list. The `elements` list is assumed to be sorted in
    ascending order. Returns -1 when the key element is not
    found
    """
    start, end = 0, (len(elements) - 1)
    return search(elements, key, start, end)


def search(elements: List[int], key: int, start: int, end: int) -> int:
    """
    Private function doing the recursive binary search
    """
    log.debug("Searching for %d in the range [%d, %d]", key, start, end)

    if((len(elements) <= 0) or (start > end)):
        # when there are no elements return -1
        return -1

    mid = (start + end) // 2
    if elements[mid] == key:
        log.debug("Element %d found in location, %d", key, mid)
        return mid

    if key < elements[mid]:
        # then find in the left half
        return search(elements, key, start, mid - 1)

    # find in the right half
    return search(elements, key, mid + 1, end)
