from typing import Any, overload
from typing_extensions import Literal
from collections.abc import Iterable, Callable

from networkx.classes.graph import Graph, _Node

def bridges(G: Graph[_Node], root: _Node | None = ...) -> Iterable[_Node]: ...
def has_bridges(G: Graph[_Node], root: Any | None = ...) -> bool: ...
@overload
def local_bridges(
    G: Graph[_Node],
    with_span: Literal[False] = False,
    weight: str | Callable[[_Node], float] | None = ...,
) -> Iterable[tuple[_Node, _Node]]: ...
@overload
def local_bridges(
    G: Graph[_Node],
    with_span: Literal[True] = True,
    weight: str | Callable[[_Node], float] | None = ...,
) -> Iterable[tuple[_Node, _Node, int]]: ...
