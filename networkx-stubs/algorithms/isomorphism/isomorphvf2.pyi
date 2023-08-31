# Stubs for networkx.algorithms.isomorphism.isomorphvf2 (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from _typeshed import Incomplete

class GraphMatcher:
    G1: Incomplete = ...
    G2: Incomplete = ...
    G1_nodes: Incomplete = ...
    G2_nodes: Incomplete = ...
    G2_node_order: Incomplete = ...
    old_recursion_limit: Incomplete = ...
    test: str = ...
    def __init__(self, G1: Incomplete, G2: Incomplete) -> None: ...
    def reset_recursion_limit(self) -> None: ...
    def candidate_pairs_iter(self) -> None: ...
    core_1: Incomplete = ...
    core_2: Incomplete = ...
    inout_1: Incomplete = ...
    inout_2: Incomplete = ...
    state: Incomplete = ...
    mapping: Incomplete = ...
    def initialize(self) -> None: ...
    def is_isomorphic(self) -> Incomplete: ...
    def isomorphisms_iter(self) -> None: ...
    def match(self) -> None: ...
    def semantic_feasibility(
        self, G1_node: Incomplete, G2_node: Incomplete
    ) -> Incomplete: ...
    def subgraph_is_isomorphic(self) -> Incomplete: ...
    def subgraph_isomorphisms_iter(self) -> None: ...
    def syntactic_feasibility(
        self, G1_node: Incomplete, G2_node: Incomplete
    ) -> Incomplete: ...

class DiGraphMatcher(GraphMatcher):
    def __init__(self, G1: Incomplete, G2: Incomplete) -> None: ...
    def candidate_pairs_iter(self) -> None: ...
    core_1: Incomplete = ...
    core_2: Incomplete = ...
    in_1: Incomplete = ...
    in_2: Incomplete = ...
    out_1: Incomplete = ...
    out_2: Incomplete = ...
    state: Incomplete = ...
    mapping: Incomplete = ...
    def initialize(self) -> None: ...
    def syntactic_feasibility(
        self, G1_node: Incomplete, G2_node: Incomplete
    ) -> Incomplete: ...

class GMState:
    GM: Incomplete = ...
    G1_node: Incomplete = ...
    G2_node: Incomplete = ...
    depth: Incomplete = ...
    def __init__(
        self,
        GM: Incomplete,
        G1_node: Incomplete | None = ...,
        G2_node: Incomplete | None = ...,
    ) -> None: ...
    def restore(self) -> None: ...

class DiGMState:
    GM: Incomplete = ...
    G1_node: Incomplete = ...
    G2_node: Incomplete = ...
    depth: Incomplete = ...
    def __init__(
        self,
        GM: Incomplete,
        G1_node: Incomplete | None = ...,
        G2_node: Incomplete | None = ...,
    ) -> None: ...
    def restore(self) -> None: ...
