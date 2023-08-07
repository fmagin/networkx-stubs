# Stubs for networkx.algorithms.traversal.depth_first_search (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Iterator, TypeVar

from networkx.classes.graph import Graph

_T = TypeVar("_T")

def dfs_edges(G: Graph[_T], source: _T | None = ..., depth_limit: int | None = ...) -> Iterator[tuple[_T, _T]]: ...
def dfs_tree(G: Any, source: Any | None = ..., depth_limit: Any | None = ...): ...
def dfs_predecessors(G: Any, source: Any | None = ..., depth_limit: Any | None = ...): ...
def dfs_successors(G: Any, source: Any | None = ..., depth_limit: Any | None = ...): ...
def dfs_postorder_nodes(G: Any, source: Any | None = ..., depth_limit: Any | None = ...): ...
def dfs_preorder_nodes(G: Any, source: Any | None = ..., depth_limit: Any | None = ...): ...
def dfs_labeled_edges(G: Any, source: Any | None = ..., depth_limit: Any | None = ...) -> None: ...
