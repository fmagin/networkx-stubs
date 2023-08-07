from collections.abc import Iterable
from networkx.classes.graph import Graph, Node

def chain_decomposition(G: Graph[Node], root: Node | None = ...) -> Iterable[tuple[Node, Node]]: ...
