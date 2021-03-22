"""
Definition of TraversalHelper
"""

from dataclasses import dataclass
from typing import Callable, Optional

from algo.graphs.vertex import Vertex, EdgeContainer


@dataclass
class TraversalHelper:
    """
    Container with helpers during Traversal
    """
    process_vertex_early: Optional[Callable[[Vertex], None]] = None
    process_vertex_late: Optional[Callable[[Vertex], None]] = None
    process_edge: Optional[
        Callable[[Vertex, Vertex, EdgeContainer], None]] = None
