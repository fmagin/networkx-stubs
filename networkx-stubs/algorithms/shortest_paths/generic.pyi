# Stubs for networkx.algorithms.shortest_paths.generic (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, TypeVar, overload
from collections.abc import Iterable

from networkx.classes.graph import Graph

_T = TypeVar("_T")

def has_path(G: Any, source: Any, target: Any) -> Any: ...
@overload
def shortest_path(
    G: Graph[_T], source: _T, target: _T, weight: Any | None = ..., method: str = ...
) -> list[_T]: ...
@overload
def shortest_path(
    G: Graph[_T], target: _T, method: str = ...
) -> dict[_T, list[_T]]: ...
@overload
def shortest_path(
    G: Graph[_T], source: _T, method: str = ...
) -> dict[_T, list[_T]]: ...
def shortest_path_length(
    G: Any,
    source: Any | None = ...,
    target: Any | None = ...,
    weight: Any | None = ...,
    method: str = ...,
) -> Any: ...
def average_shortest_path_length(
    G: Any, weight: Any | None = ..., method: str = ...
) -> Any: ...
def all_shortest_paths(
    G: Graph[_T], source: _T, target: _T, weight: Any | None = ..., method: str = ...
) -> Iterable[list[_T]]: ...
