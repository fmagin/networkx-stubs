from typing import Any, TypeVar
from _typeshed import Incomplete
from io import TextIOBase
from collections.abc import Callable
from typing_extensions import TypeAlias

# from pygraphviz.agraph import AGraph as _AGraph
_AGraph: TypeAlias = Incomplete
from networkx.classes.graph import Graph

_T = TypeVar("_T")

def from_agraph(A: Any, create_using: Any | None = ...) -> Graph[Any]: ...
def to_agraph(N: Graph[Any]) -> _AGraph: ...
def write_dot(G: Graph[Any], path: str | TextIOBase) -> None: ...
def read_dot(path: str | TextIOBase) -> Graph[Any]: ...
def graphviz_layout(
    G: Graph[_T], prog: str = ..., root: str | None = ..., args: str = ...
) -> dict[_T, tuple[float, float]]: ...

pygraphviz_layout = graphviz_layout

def view_pygraphviz(
    G: Graph[_T],
    edgelabel: str | Callable[[_T], str] | None = ...,
    prog: str = ...,
    args: str = ...,
    suffix: str = ...,
    path: str | None = ...,
) -> Incomplete: ...
