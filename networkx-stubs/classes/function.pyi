# Stubs for networkx.classes.function (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Iterable, TypeVar, overload

from networkx.classes.digraph import DiGraph

# GT = TypeVar("GT", bound=Graph)
_T = TypeVar("_T")

def nodes(G: Any): ...
def edges(G: Any, nbunch: Any | None = ...): ...
def degree(G: Any, nbunch: Any | None = ..., weight: Any | None = ...): ...
def neighbors(G: Any, n: Any): ...
def number_of_nodes(G: Any): ...
def number_of_edges(G: Any): ...
def density(G: Any): ...
def degree_histogram(G: Any): ...
def is_directed(G: Any): ...
def freeze(G: Any): ...
def is_frozen(G: Any): ...
def add_star(G_to_add_to: Any, nodes_for_star: Any, **attr: Any) -> None: ...
def add_path(G_to_add_to: Any, nodes_for_path: Any, **attr: Any) -> None: ...
def add_cycle(G_to_add_to: Any, nodes_for_cycle: Any, **attr: Any) -> None: ...
def subgraph(G: Any, nbunch: Any): ...
def induced_subgraph(G: DiGraph[_T], nbunch: _T | Iterable[_T] | None) -> DiGraph[_T]: ...
def edge_subgraph(G: Any, edges: Any): ...
def restricted_view(G: Any, nodes: Any, edges: Any): ...
def reverse_view(digraph: Any): ...
def to_directed(graph: Any): ...
def to_undirected(graph: Any): ...
def create_empty_copy(G: Any, with_data: bool = ...): ...
def info(G: Any, n: Any | None = ...): ...
@overload
def set_node_attributes(G: DiGraph[_T], values: dict[_T, Any], name: str = ...) -> None: ...

# Can "Any scalar value" be enforced?
@overload
def set_node_attributes(G: DiGraph[_T], values: Any, name: str = ...) -> None: ...
@overload
def set_node_attributes(G: DiGraph[_T], values: dict[_T, dict[Any, Any]], name: None = ...) -> None: ...
def get_node_attributes(G: DiGraph[_T], name: str): ...
@overload
def set_edge_attributes(G: DiGraph[_T], values: dict[tuple[_T, _T], Any], name: str = ...) -> None: ...
@overload
def set_edge_attributes(G: DiGraph[_T], values: Any, name: None = ...) -> None: ...
def get_edge_attributes(G: DiGraph[_T], name: str): ...
def all_neighbors(graph: Any, node: Any): ...
def non_neighbors(graph: Any, node: Any): ...
def non_edges(graph: Any) -> None: ...
def common_neighbors(G: Any, u: Any, v: Any): ...
def is_weighted(G: Any, edge: Any | None = ..., weight: str = ...): ...
def is_negatively_weighted(G: Any, edge: Any | None = ..., weight: str = ...): ...
def is_empty(G: Any): ...
def nodes_with_selfloops(G: Any): ...
def selfloop_edges(G: Any, data: bool = ..., keys: bool = ..., default: Any | None = ...): ...
def number_of_selfloops(G: Any): ...
