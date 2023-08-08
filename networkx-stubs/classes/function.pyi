from typing import Any, TypeVar, overload
from typing_extensions import Literal
from collections.abc import Iterable

from networkx.classes.graph import Graph

_T = TypeVar("_T")
_U = TypeVar("_U")

def nodes(G: Any) -> Any: ...
def edges(G: Any, nbunch: Any | None = ...) -> Any: ...
def degree(G: Any, nbunch: Any | None = ..., weight: Any | None = ...) -> Any: ...
def neighbors(G: Any, n: Any) -> Any: ...
def number_of_nodes(G: Any) -> Any: ...
def number_of_edges(G: Any) -> Any: ...
def density(G: Any) -> Any: ...
def degree_histogram(G: Any) -> Any: ...
def is_directed(G: Any) -> Any: ...
def freeze(G: Any) -> Any: ...
def is_frozen(G: Any) -> Any: ...
def add_star(G_to_add_to: Any, nodes_for_star: Any, **attr: Any) -> None: ...
def add_path(G_to_add_to: Any, nodes_for_path: Any, **attr: Any) -> None: ...
def add_cycle(G_to_add_to: Any, nodes_for_cycle: Any, **attr: Any) -> None: ...
def subgraph(G: Any, nbunch: Any) -> Any: ...
def induced_subgraph(G: Graph[_T], nbunch: _T | Iterable[_T] | None) -> Graph[_T]: ...
def edge_subgraph(G: Any, edges: Any) -> Any: ...
def restricted_view(G: Any, nodes: Any, edges: Any) -> Any: ...
def reverse_view(digraph: Any) -> Any: ...
def to_directed(graph: Any) -> Any: ...
def to_undirected(graph: Any) -> Any: ...
def create_empty_copy(G: Any, with_data: bool = ...) -> Any: ...
def info(G: Any, n: Any | None = ...) -> Any: ...
@overload
def set_node_attributes(
    G: Graph[_T], values: dict[_T, Any], name: str = ...
) -> None: ...

# Can "Any scalar value" be enforced?
@overload
def set_node_attributes(G: Graph[Any], values: Any, name: str = ...) -> None: ...
@overload
def set_node_attributes(
    G: Graph[_T], values: dict[_T, dict[Any, Any]], name: None = ...
) -> None: ...
def get_node_attributes(G: Graph[_T], name: str) -> dict[_T, Any]: ...
@overload
def set_edge_attributes(
    G: Graph[_T], values: dict[tuple[_T, _T], Any], name: str = ...
) -> None: ...
@overload
def set_edge_attributes(G: Graph[Any], values: Any, name: None = ...) -> None: ...
def get_edge_attributes(G: Graph[_T], name: str) -> dict[tuple[_T, _T], Any]: ...
def all_neighbors(graph: Graph[_T], node: _T) -> Iterable[_T]: ...
def non_neighbors(graph: Graph[_T], node: _T) -> Iterable[_T]: ...
def non_edges(graph: Graph[_T]) -> Iterable[tuple[_T, _T]]: ...
def common_neighbors(G: Graph[_T], u: _T, v: _T) -> Iterable[_T]: ...
def is_weighted(
    G: Graph[_T], edge: tuple[_T, _T] | None = ..., weight: str | None = ...
) -> bool: ...
def is_negatively_weighted(
    G: Graph[_T], edge: tuple[_T, _T] | None = ..., weight: str | None = ...
) -> Any: ...
def is_empty(G: Graph[Any]) -> bool: ...
def nodes_with_selfloops(G: Graph[_T]) -> Iterable[_T]: ...
@overload
def selfloop_edges(
    G: Graph[_T],
    data: Literal[False] = False,
    keys: Literal[False] = ...,
    default: Any = ...,
) -> Iterable[tuple[_T, _T]]: ...
@overload
def selfloop_edges(
    G: Graph[_T],
    data: Literal[True] = True,
    keys: Literal[False] = ...,
    default: Any = ...,
) -> Iterable[tuple[_T, _T, dict[str, Any]]]: ...
@overload
def selfloop_edges(
    G: Graph[_T], data: str = ..., keys: Literal[False] = ..., default: _U = None
) -> Iterable[tuple[_T, _T, _U]]: ...
@overload
def selfloop_edges(
    G: Graph[_T],
    data: Literal[False] = False,
    keys: Literal[True] = True,
    default: Any = ...,
) -> Iterable[tuple[_T, _T, int]]: ...
@overload
def selfloop_edges(
    G: Graph[_T],
    data: Literal[True] = True,
    keys: Literal[True] = True,
    default: Any = ...,
) -> Iterable[tuple[_T, _T, int, dict[str, Any]]]: ...
@overload
def selfloop_edges(
    G: Graph[_T], data: str = ..., keys: Literal[True] = True, default: _U = None
) -> Iterable[tuple[_T, _T, int, _U]]: ...
def number_of_selfloops(G: Graph[Any]) -> int: ...
