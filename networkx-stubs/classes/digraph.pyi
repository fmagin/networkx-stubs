from typing import Any, Generic, Iterator

from networkx.classes.coreviews import AdjacencyView
from networkx.classes.graph import Graph, Node
from networkx.classes.reportviews import (
    InDegreeView,
    InEdgeView,
    InMultiDegreeView,
    OutDegreeView,
    OutEdgeView,
    OutMultiDegreeView,
)

class DiGraph(Graph[Node], Generic[Node]):
    succ: AdjacencyView[Node, Node, dict[str, Any]]
    pred: AdjacencyView[Node, Node, dict[str, Any]]
    def has_successor(self, u: Node, v: Node) -> bool: ...
    def has_predecessor(self, u: Node, v: Node) -> bool: ...
    def successors(self, n: Node) -> Iterator[Node]: ...
    def predecessors(self, n: Node) -> Iterator[Node]: ...
    in_edges: InEdgeView[Node]
    in_degree: InDegreeView[Node] | InMultiDegreeView[Node]  # ugly hack to make MultiDiGraph work
    out_edges: OutEdgeView[Node]
    out_degree: OutDegreeView[Node] | OutMultiDegreeView[Node]  # ugly hack to make MultiDiGraph work
    def reverse(self, copy: bool = ...) -> DiGraph[Node]: ...
    def copy(self, as_view: bool = ...) -> DiGraph[Node]: ...
