from typing import Any, overload
from typing_extensions import Literal
from collections.abc import Iterable, Callable

from networkx.classes.graph import Graph, _Node
from networkx.classes.digraph import DiGraph
from networkx.classes.multigraph import MultiGraph
from networkx.classes.multidigraph import MultiDiGraph

import numpy
#from pandas import DataFrame
#from pandas.core.dtypes.base import ExtensionDtype 
DataFrame = Any
ExtensionDtype = Any

def to_pandas_adjacency(
    G: Graph[_Node],
    nodelist: list[_Node] | None = ...,
    dtype: numpy.dtype[Any] | None = ...,
    order: Literal["C", "F"] | None = ...,
    multigraph_weight: Callable[[Iterable[float]], float] = ...,
    weight: str = ...,
    nonedge: float = ...,
) -> DataFrame: ...
@overload
def from_pandas_adjacency(
    df: DataFrame, create_using: type[Graph[Any]] = ...
) -> Graph[Any]: ...
@overload
def from_pandas_adjacency(
    df: DataFrame, create_using: type[DiGraph[Any]] = ...
) -> DiGraph[Any]: ...
@overload
def from_pandas_adjacency(
    df: DataFrame, create_using: type[MultiGraph[Any]] = ...
) -> MultiGraph[Any]: ...
@overload
def from_pandas_adjacency(
    df: DataFrame, create_using: type[MultiDiGraph[Any]] = ...
) -> MultiDiGraph[Any]: ...
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
    create_using: type[Graph[Any]] = ...,
) -> Graph[Any]: ...
@overload
def from_pandas_edgelist(
    df: DataFrame,
    source: str | int = ...,
    target: str | int = ...,
    edge_attr: str | int | Iterable[str | int] | Literal[True] | None = ...,
    create_using: type[DiGraph[Any]] = ...,
) -> DiGraph[Any]: ...
@overload
def from_pandas_edgelist(
    df: DataFrame,
    source: str | int = ...,
    target: str | int = ...,
    edge_attr: str | int | Iterable[str | int] | Literal[True] | None = ...,
    create_using: type[MultiGraph[Any]] = ...,
) -> MultiGraph[Any]: ...
@overload
def from_pandas_edgelist(
    df: DataFrame,
    source: str | int = ...,
    target: str | int = ...,
    edge_attr: str | int | Iterable[str | int] | Literal[True] | None = ...,
    create_using: type[MultiDiGraph[Any]] = ...,
) -> MultiDiGraph[Any]: ...
def to_numpy_array(
    G: Graph[_Node],
    nodelist: list[_Node] | None = ...,
    dtype: numpy.dtype[Any] | None = ...,
    order: Literal["C", "F"] | None = ...,
    multigraph_weight: Callable[[Iterable[float]], float] = ...,
    weight: str = ...,
    nonedge: float = ...,
) -> numpy.ndarray[Any, numpy.dtype[Any]]: ...
@overload
def from_numpy_array(
    A: numpy.ndarray[Any, Any],
    parallel_edges: bool = ...,
    create_using: type[Graph[Any]] = ...,
) -> Graph[Any]: ...
@overload
def from_numpy_array(
    A: numpy.ndarray[Any, Any],
    parallel_edges: bool = ...,
    create_using: type[DiGraph[Any]] = ...,
) -> DiGraph[Any]: ...
@overload
def from_numpy_array(
    A: numpy.ndarray[Any, Any],
    parallel_edges: bool = ...,
    create_using: type[MultiGraph[Any]] = ...,
) -> MultiGraph[Any]: ...
@overload
def from_numpy_array(
    A: numpy.ndarray[Any, Any],
    parallel_edges: bool = ...,
    create_using: type[MultiDiGraph[Any]] = ...,
) -> MultiDiGraph[Any]: ...
