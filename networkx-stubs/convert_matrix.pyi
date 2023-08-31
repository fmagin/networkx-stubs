from collections.abc import Callable, Iterable
from typing import overload
from _typeshed import Incomplete

import numpy
from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph, _Node
from networkx.classes.multidigraph import MultiDiGraph
from networkx.classes.multigraph import MultiGraph
from pandas import DataFrame
from pandas.core.dtypes.base import ExtensionDtype
from typing_extensions import Literal

def to_pandas_adjacency(
    G: Graph[_Node],
    nodelist: list[_Node] | None = ...,
    dtype: numpy.dtype[Incomplete] | None = ...,
    order: Literal["C", "F"] | None = ...,
    multigraph_weight: Callable[[Iterable[float]], float] = ...,
    weight: str = ...,
    nonedge: float = ...,
) -> DataFrame: ...
@overload
def from_pandas_adjacency(
    df: DataFrame, create_using: type[Graph[Incomplete]] = ...
) -> Graph[Incomplete]: ...
@overload
def from_pandas_adjacency(
    df: DataFrame, create_using: type[DiGraph[Incomplete]] = ...
) -> DiGraph[Incomplete]: ...
@overload
def from_pandas_adjacency(
    df: DataFrame, create_using: type[MultiGraph[Incomplete]] = ...
) -> MultiGraph[Incomplete]: ...
@overload
def from_pandas_adjacency(
    df: DataFrame, create_using: type[MultiDiGraph[Incomplete]] = ...
) -> MultiDiGraph[Incomplete]: ...
def to_pandas_edgelist(
    G: Graph[_Node],
    source: str | int = ...,
    target: str | int = ...,
    nodelist: list[_Node] | None = ...,
    dtype: ExtensionDtype | None = ...,
    edge_key: str | int | None = ...,
) -> DataFrame: ...
@overload
def from_pandas_edgelist(
    df: DataFrame,
    source: str | int = ...,
    target: str | int = ...,
    edge_attr: str | int | Iterable[str | int] | Literal[True] | None = ...,
    create_using: type[Graph[Incomplete]] = ...,
) -> Graph[Incomplete]: ...
@overload
def from_pandas_edgelist(
    df: DataFrame,
    source: str | int = ...,
    target: str | int = ...,
    edge_attr: str | int | Iterable[str | int] | Literal[True] | None = ...,
    create_using: type[DiGraph[Incomplete]] = ...,
) -> DiGraph[Incomplete]: ...
@overload
def from_pandas_edgelist(
    df: DataFrame,
    source: str | int = ...,
    target: str | int = ...,
    edge_attr: str | int | Iterable[str | int] | Literal[True] | None = ...,
    create_using: type[MultiGraph[Incomplete]] = ...,
) -> MultiGraph[Incomplete]: ...
@overload
def from_pandas_edgelist(
    df: DataFrame,
    source: str | int = ...,
    target: str | int = ...,
    edge_attr: str | int | Iterable[str | int] | Literal[True] | None = ...,
    create_using: type[MultiDiGraph[Incomplete]] = ...,
) -> MultiDiGraph[Incomplete]: ...
def to_numpy_array(
    G: Graph[_Node],
    nodelist: list[_Node] | None = ...,
    dtype: numpy.dtype[Incomplete] | None = ...,
    order: Literal["C", "F"] | None = ...,
    multigraph_weight: Callable[[Iterable[float]], float] = ...,
    weight: str = ...,
    nonedge: float = ...,
) -> numpy.ndarray[Incomplete, numpy.dtype[Incomplete]]: ...
@overload
def from_numpy_array(
    A: numpy.ndarray[Incomplete, Incomplete],
    parallel_edges: bool = ...,
    create_using: type[Graph[Incomplete]] = ...,
) -> Graph[Incomplete]: ...
@overload
def from_numpy_array(
    A: numpy.ndarray[Incomplete, Incomplete],
    parallel_edges: bool = ...,
    create_using: type[DiGraph[Incomplete]] = ...,
) -> DiGraph[Incomplete]: ...
@overload
def from_numpy_array(
    A: numpy.ndarray[Incomplete, Incomplete],
    parallel_edges: bool = ...,
    create_using: type[MultiGraph[Incomplete]] = ...,
) -> MultiGraph[Incomplete]: ...
@overload
def from_numpy_array(
    A: numpy.ndarray[Incomplete, Incomplete],
    parallel_edges: bool = ...,
    create_using: type[MultiDiGraph[Incomplete]] = ...,
) -> MultiDiGraph[Incomplete]: ...
