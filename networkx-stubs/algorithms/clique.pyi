from typing import overload
from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.classes.digraph import DiGraph
from networkx.classes.multigraph import MultiGraph
from networkx.classes.multidigraph import MultiDiGraph

def enumerate_all_cliques(G: Graph[_Node]) -> Iterable[list[_Node]]: ...
def find_cliques(
    G: Graph[_Node], nodes: list[_Node] | None = ...
) -> Iterable[list[_Node]]: ...
def find_cliques_recursive(
    G: Graph[_Node], nodes: list[_Node] | None = ...
) -> Iterable[list[_Node]]: ...
@overload
def make_max_clique_graph(
    G: Graph[_Node], create_using: type[Graph[_Node]] = ...
) -> Graph[_Node]: ...
@overload
def make_max_clique_graph(
    G: Graph[_Node], create_using: type[DiGraph[_Node]] = ...
) -> DiGraph[_Node]: ...
@overload
def make_max_clique_graph(
    G: Graph[_Node], create_using: type[MultiGraph[_Node]] = ...
) -> MultiGraph[_Node]: ...
@overload
def make_max_clique_graph(
    G: Graph[_Node], create_using: type[MultiDiGraph[_Node]] = ...
) -> MultiDiGraph[_Node]: ...
@overload
def make_clique_bipartite(
    G: Graph[_Node],
    fpos: None = ...,
    create_using: type[Graph[_Node]] = ...,
    name: None = ...,
) -> Graph[_Node]: ...
@overload
def make_clique_bipartite(
    G: Graph[_Node],
    fpos: None = ...,
    create_using: type[DiGraph[_Node]] = ...,
    name: None = ...,
) -> DiGraph[_Node]: ...
@overload
def make_clique_bipartite(
    G: Graph[_Node],
    fpos: None = ...,
    create_using: type[MultiGraph[_Node]] = ...,
    name: None = ...,
) -> MultiGraph[_Node]: ...
@overload
def make_clique_bipartite(
    G: Graph[_Node],
    fpos: None = ...,
    create_using: type[MultiDiGraph[_Node]] = ...,
    name: None = ...,
) -> MultiDiGraph[_Node]: ...
def graph_clique_number(G: Graph[_Node], cliques: list[_Node] | None = ...) -> int: ...
def graph_number_of_cliques(
    G: Graph[_Node], cliques: list[_Node] | None = ...
) -> int: ...
def node_clique_number(
    G: Graph[_Node],
    nodes: list[_Node] | None = ...,
    cliques: list[list[_Node]] | None = ...,
) -> int: ...
def number_of_cliques(
    G: Graph[_Node],
    nodes: list[_Node] | None = ...,
    cliques: list[list[_Node]] | None = ...,
) -> int: ...
def cliques_containing_node(
    G: Graph[_Node],
    nodes: list[_Node] | None = ...,
    cliques: list[list[_Node]] | None = ...,
) -> Iterable[list[_Node]]: ...
