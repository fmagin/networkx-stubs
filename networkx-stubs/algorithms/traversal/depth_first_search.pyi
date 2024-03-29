from collections.abc import Iterator
from typing import TypeVar

from _typeshed import Incomplete
from networkx.classes.graph import Graph

_T = TypeVar("_T")

def dfs_edges(
    G: Graph[_T], source: _T | None = ..., depth_limit: int | None = ...
) -> Iterator[tuple[_T, _T]]: ...
def dfs_tree(
    G: Incomplete, source: Incomplete | None = ..., depth_limit: Incomplete | None = ...
) -> Incomplete: ...
def dfs_predecessors(
    G: Incomplete, source: Incomplete | None = ..., depth_limit: Incomplete | None = ...
) -> Incomplete: ...
def dfs_successors(
    G: Incomplete, source: Incomplete | None = ..., depth_limit: Incomplete | None = ...
) -> Incomplete: ...
def dfs_postorder_nodes(
    G: Incomplete, source: Incomplete | None = ..., depth_limit: Incomplete | None = ...
) -> Incomplete: ...
def dfs_preorder_nodes(
    G: Incomplete, source: Incomplete | None = ..., depth_limit: Incomplete | None = ...
) -> Incomplete: ...
def dfs_labeled_edges(
    G: Incomplete, source: Incomplete | None = ..., depth_limit: Incomplete | None = ...
) -> None: ...
