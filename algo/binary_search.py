"""
Module containing a method to do binary_search
"""

from typing import List

import logging as log

log.basicConfig(level=log.DEBUG)


def binary_search(elements: List[int], key: int) -> int:
    """
    Returns the index of the `key` inside the `elements`
    list. The `elements` list is assumed to be sorted in
    ascending order. Returns -1 when the key element is not
    found
    """
    start, end = 0, (len(elements) - 1)
    return _binary_search(elements, key, start, end)


def _binary_search(elements: List[int], key: int,
                   start: int, end: int) -> int:
    log.info("Searching for %d in the range [%d, %d]", key, start, end)

    if((len(elements) <= 0) or (start > end)):
        # when there are no elements return -1
        return -1

    mid = (start + end) // 2
    if elements[mid] == key:
        # add logger here
        return mid

    if key < elements[mid]:
        # then find in the left half
        return _binary_search(elements, key, start, mid - 1)

    # find in the right half
    return _binary_search(elements, key, mid + 1, end)
