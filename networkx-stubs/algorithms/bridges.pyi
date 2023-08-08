from typing import Any, overload, Callable
from typing_extensions import Literal
from collections.abc import Iterable

from networkx.classes.graph import Graph, Node

def bridges(G: Graph[Node], root: Node | None = ...) -> Iterable[Node]: ...
def has_bridges(G: Graph[Node], root: Any | None = ...) -> bool: ...
@overload
def local_bridges(
    G: Graph[Node],
    with_span: Literal[False] = False,
    weight: str | Callable[[Node], int | float] | None = ...,
) -> Iterable[tuple[Node, Node]]: ...
@overload
def local_bridges(
    G: Graph[Node],
    with_span: Literal[True] = True,
    weight: str | Callable[[Node], int | float] | None = ...,
) -> Iterable[tuple[Node, Node, int]]: ...
