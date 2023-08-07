from typing import Any
from collections.abc import Iterable

import networkx as nx
from networkx.classes.graph import Graph, Node
class NetworkXTreewidthBoundExceeded(nx.NetworkXException): ...

def is_chordal(G: Graph[Any]) -> bool: ...
def find_induced_nodes(G: Graph[Node], s: Node, t: Node, treewidth_bound: int = ...) -> set[Node]: ...
def chordal_graph_cliques(G: Graph[Node]) -> Iterable[frozenset[Node]]: ...
def chordal_graph_treewidth(G: Graph[Any]) -> int: ...
