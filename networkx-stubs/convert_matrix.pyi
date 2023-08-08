from typing import Any, TypeVar, Literal, Callable
from networkx.classes.graph import Graph
from collections.abc import Iterable

_T = TypeVar("_T")
_G = TypeVar("_G", bound=Graph[Any])

import numpy
import pandas.core.dtypes.base

def to_pandas_adjacency(
    G: Graph[_T],
    nodelist: list[_T] | None = ...,
    dtype: numpy.dtype[Any] | None = ...,
    order: Literal["C", "F"] | None = ...,
    multigraph_weight: Callable[[Iterable[float]], float] = ...,
    weight: str = ...,
    nonedge: float = ...,
) -> pandas.DataFrame: ...
def from_pandas_adjacency(
    df: pandas.DataFrame, create_using: type[_G] = Graph
) -> _G: ...
def to_pandas_edgelist(
    G: Graph[_T],
    source: str | int = ...,
    target: str | int = ...,
    nodelist: list[_T] | None = ...,
    dtype: pandas.core.dtypes.base.ExtensionDtype | None = ...,
    edge_key: str | int | None = ...,
) -> pandas.DataFrame: ...
def from_pandas_edgelist(
    df: pandas.DataFrame,
    source: str | int = ...,
    target: str | int = ...,
    edge_attr: str | int | Iterable[str | int] | Literal[True] | None = ...,
    create_using: type[_G] = Graph,
) -> _G: ...
def to_numpy_array(
    G: Graph[_T],
    nodelist: list[_T] | None = ...,
    dtype: numpy.dtype[Any] | None = ...,
    order: Literal["C", "F"] | None = ...,
    multigraph_weight: Callable[[Iterable[float]], float] = ...,
    weight: str = ...,
    nonedge: float = ...,
) -> numpy.ndarray[Any, numpy.dtype[Any]]: ...
def from_numpy_array(
    A: numpy.ndarray[Any, Any],
    parallel_edges: bool = ...,
    create_using: type[_G] = Graph,
) -> _G: ...
