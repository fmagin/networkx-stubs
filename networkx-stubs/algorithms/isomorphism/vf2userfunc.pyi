# Stubs for networkx.algorithms.isomorphism.vf2userfunc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

from . import isomorphvf2 as vf2

class GraphMatcher(vf2.GraphMatcher):
    node_match: Any = ...
    edge_match: Any = ...
    G1_adj: Any = ...
    G2_adj: Any = ...
    def __init__(
        self,
        G1: Any,
        G2: Any,
        node_match: Any | None = ...,
        edge_match: Any | None = ...,
    ) -> None: ...
    semantic_feasibility: Any = ...

class DiGraphMatcher(vf2.DiGraphMatcher):
    node_match: Any = ...
    edge_match: Any = ...
    G1_adj: Any = ...
    G2_adj: Any = ...
    def __init__(
        self,
        G1: Any,
        G2: Any,
        node_match: Any | None = ...,
        edge_match: Any | None = ...,
    ) -> None: ...
    def semantic_feasibility(self, G1_node: Any, G2_node: Any) -> Incomplete: ...

class MultiGraphMatcher(GraphMatcher): ...
class MultiDiGraphMatcher(DiGraphMatcher): ...
