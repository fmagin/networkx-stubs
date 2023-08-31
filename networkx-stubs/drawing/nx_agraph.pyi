from collections.abc import Callable
from io import TextIOBase
from typing import Incomplete, TypeVar

from _typeshed import Incomplete
from typing_extensions import TypeAlias

# from pygraphviz.agraph import AGraph as _AGraph
_AGraph: TypeAlias = Incomplete
from networkx.classes.graph import Graph

_T = TypeVar("_T")

def from_agraph(
    A: Incomplete, create_using: Incomplete | None = ...
) -> Graph[Incomplete]: ...
def to_agraph(N: Graph[Incomplete]) -> _AGraph: ...
def write_dot(G: Graph[Incomplete], path: str | TextIOBase) -> None: ...
def read_dot(path: str | TextIOBase) -> Graph[Incomplete]: ...
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
