from collections.abc import Mapping
from typing import Incomplete, TypeVar, overload

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph
from networkx.classes.multidigraph import MultiDiGraph
from networkx.classes.multigraph import MultiGraph
from typing_extensions import Literal

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
    G: Graph[Incomplete],
    first_label: int = ...,
    ordering: Literal[
        "default", "sorted", "increasing degree", "decreasing degree"
    ] = ...,
    label_attribute: Incomplete | None = ...,
) -> Graph[int]: ...
@overload
def convert_node_labels_to_integers(
    G: DiGraph[Incomplete],
    first_label: int = ...,
    ordering: Literal[
        "default", "sorted", "increasing degree", "decreasing degree"
    ] = ...,
    label_attribute: Incomplete | None = ...,
) -> DiGraph[int]: ...
@overload
def convert_node_labels_to_integers(
    G: MultiGraph[Incomplete],
    first_label: int = ...,
    ordering: Literal[
        "default", "sorted", "increasing degree", "decreasing degree"
    ] = ...,
    label_attribute: Incomplete | None = ...,
) -> MultiGraph[int]: ...
@overload
def convert_node_labels_to_integers(
    G: MultiDiGraph[Incomplete],
    first_label: int = ...,
    ordering: Literal[
        "default", "sorted", "increasing degree", "decreasing degree"
    ] = ...,
    label_attribute: Incomplete | None = ...,
) -> MultiDiGraph[int]: ...
