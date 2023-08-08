from typing import Any, TypeVar, Mapping, overload
from typing_extensions import Literal

from networkx.classes.graph import Graph
from networkx.classes.digraph import DiGraph
from networkx.classes.multigraph import MultiGraph
from networkx.classes.multidigraph import MultiDiGraph

_X = TypeVar("_X")
_Y = TypeVar("_Y")

@overload
def relabel_nodes(
    G: Graph[_X], mapping: Mapping[_X, _Y], copy: bool = ...
) -> Graph[_X | _Y]: ...
@overload
def relabel_nodes(
    G: DiGraph[_X], mapping: Mapping[_X, _Y], copy: bool = ...
) -> DiGraph[_X | _Y]: ...
@overload
def relabel_nodes(
    G: MultiGraph[_X], mapping: Mapping[_X, _Y], copy: bool = ...
) -> MultiGraph[_X | _Y]: ...
@overload
def relabel_nodes(
    G: MultiDiGraph[_X], mapping: Mapping[_X, _Y], copy: bool = ...
) -> MultiDiGraph[_X | _Y]: ...
@overload
def convert_node_labels_to_integers(
    G: Graph[Any],
    first_label: int = ...,
    ordering: Literal[
        "default", "sorted", "increasing degree", "decreasing degree"
    ] = ...,
    label_attribute: Any | None = ...,
) -> Graph[int]: ...
@overload
def convert_node_labels_to_integers(
    G: DiGraph[Any],
    first_label: int = ...,
    ordering: Literal[
        "default", "sorted", "increasing degree", "decreasing degree"
    ] = ...,
    label_attribute: Any | None = ...,
) -> DiGraph[int]: ...
@overload
def convert_node_labels_to_integers(
    G: MultiGraph[Any],
    first_label: int = ...,
    ordering: Literal[
        "default", "sorted", "increasing degree", "decreasing degree"
    ] = ...,
    label_attribute: Any | None = ...,
) -> MultiGraph[int]: ...
@overload
def convert_node_labels_to_integers(
    G: MultiDiGraph[Any],
    first_label: int = ...,
    ordering: Literal[
        "default", "sorted", "increasing degree", "decreasing degree"
    ] = ...,
    label_attribute: Any | None = ...,
) -> MultiDiGraph[int]: ...
