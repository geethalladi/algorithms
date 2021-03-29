"""
Priority Queue Implementation
"""

from typing import Any, Dict, Generic, List, Tuple, TypeVar

from dataclasses import dataclass

__all__ = ['PriorityQueue']

T = TypeVar('T')


@dataclass
class Container:
    """
    Creating a container class
    """
    identity: int
    priority: int
    task: Any
    position: int = -1


class PriorityQueue(Generic[T]):
    """
    Priority Queue storing elements of type  T
    """

    entries: List[Container]
    map: Dict[int, Container]
    size: int

    def __init__(self):
        self.entries = []
        self.size = 0

    def empty(self):
        """
        Check if the PQ is empty
        """
        return self.size <= 0

    def insert(self, identity: int, priority: int, task: T):
        """
        Insert the element with the given priority
        """

    def get(self) -> Tuple[int, T]:
        """
        Return the task with the highest priority
        """

    def update(self, identity: int, new_priority: int):
        """
        Update the priority of an existing element
        """

    @classmethod
    def __create_container(cls, identity: int, priority: int, task: T):
        return Container(identity, priority, task)
