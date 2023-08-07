# Stubs for networkx.algorithms.clique (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def enumerate_all_cliques(G: Any) -> None: ...
def find_cliques(G: Any): ...
def find_cliques_recursive(G: Any): ...
def make_max_clique_graph(G: Any, create_using: Any | None = ...): ...
def make_clique_bipartite(G: Any, fpos: Any | None = ..., create_using: Any | None = ..., name: Any | None = ...): ...
def graph_clique_number(G: Any, cliques: Any | None = ...): ...
def graph_number_of_cliques(G: Any, cliques: Any | None = ...): ...
def node_clique_number(G: Any, nodes: Any | None = ..., cliques: Any | None = ...): ...
def number_of_cliques(G: Any, nodes: Any | None = ..., cliques: Any | None = ...): ...
def cliques_containing_node(G: Any, nodes: Any | None = ..., cliques: Any | None = ...): ...
