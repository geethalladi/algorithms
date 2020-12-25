"""
Given a list of numbers, sort them. Use Merge sort
The Complexity is O(nlgn) in time and O(n) in space.
"""

from typing import List
import logging as log

log.basicConfig(level=log.DEBUG)


def sort(elements: List[int]) -> List[int]:
    """
    Given a list of numbers, sort the elements. Uses Merge Sort for
    sorting the elements. The algorithm has a complexity of O(nlgn)
    for time and O(n) for space.
    """
    if elements is None:
        log.debug("NO NEED TO SORT %s", str(elements))
        return []

    size = len(elements)

    if len(elements) <= 1:
        log.debug("NO NEED TO SORT %s", str(elements))
        return elements

    return __merge_sort(elements, 0, size - 1)


def __merge_sort(elements: List[int], low: int, high: int) -> List[int]:
    """
    Apply merge sort in the given list, between [low, high]
    """

    log.debug("__merge(%s)", str(elements[low:(high+1)]))
    if low >= high:
        log.debug("SORT IS IDEMPOTENT HERE. SKIPPING")
        return elements[low:(high+1)]

    mid = (low + high) // 2

    left = __merge_sort(elements, low, mid)
    right = __merge_sort(elements, mid + 1, high)

    return __merge(left, right)


def __merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merge two sorted lists
    """
    log.debug("Merging %s with %s", str(left), str(right))
    result = []
    result.extend(left)
    result.extend(right)
    return result
