# Stubs for networkx.utils.union_find (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from _typeshed import Incomplete

class UnionFind:
    parents: Any = ...
    weights: Any = ...
    def __init__(self, elements: Any | None = ...) -> None: ...
    def __getitem__(self, object: Any) -> Incomplete: ...
    def __iter__(self) -> Incomplete: ...
    def to_sets(self) -> None: ...
    def union(self, *objects: Any) -> Incomplete: ...
