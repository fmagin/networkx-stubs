from typing import Generic, Iterable, Dict, Any
from networkx.classes.graph import Graph, Node
from networkx.classes.coreviews import AdjacencyView
from networkx.classes.reportviews import (
    InDegreeView,
    InEdgeView,
    InMultiDegreeView,
    OutDegreeView,
    OutEdgeView,
    OutMultiDegreeView,
)
class DiGraph(Graph[Node], Generic[Node]):
    succ: AdjacencyView[Node, Node, Dict[str, Any]]
    pred: AdjacencyView[Node, Node, Dict[str, Any]]
    def has_successor(self, u: Node, v: Node) -> bool: ...
    def has_predecessor(self, u: Node, v: Node) -> bool: ...
    def successors(self, n: Node) -> Iterable[Node]: ...
    def predecessors(self, n: Node) -> Iterable[Node]: ...
    in_edges: InEdgeView[Node]
    in_degree: InDegreeView[Node] | InMultiDegreeView[Node]  # ugly hack to make MultiDiGraph work
    out_edges: OutEdgeView[Node]
    out_degree: OutDegreeView[Node] | OutMultiDegreeView[Node]  # ugly hack to make MultiDiGraph work
    def reverse(self, copy: bool = ...) -> DiGraph[Node]: ...
    def copy(self, as_view: bool = ...) -> DiGraph[Node]: ...
