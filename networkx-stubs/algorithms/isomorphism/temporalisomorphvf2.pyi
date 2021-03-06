# Stubs for networkx.algorithms.isomorphism.temporalisomorphvf2 (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .isomorphvf2 import DiGraphMatcher, GraphMatcher
from typing import Any, Optional

class TimeRespectingGraphMatcher(GraphMatcher):
    temporal_attribute_name: Any = ...
    delta: Any = ...
    def __init__(self, G1: Any, G2: Any, temporal_attribute_name: Any, delta: Any) -> None: ...
    def one_hop(self, Gx: Any, Gx_node: Any, neighbors: Any): ...
    def two_hop(self, Gx: Any, core_x: Any, Gx_node: Any, neighbors: Any): ...
    def semantic_feasibility(self, G1_node: Any, G2_node: Any): ...

class TimeRespectingDiGraphMatcher(DiGraphMatcher):
    temporal_attribute_name: Any = ...
    delta: Any = ...
    def __init__(self, G1: Any, G2: Any, temporal_attribute_name: Any, delta: Any) -> None: ...
    def get_pred_dates(self, Gx: Any, Gx_node: Any, core_x: Any, pred: Any): ...
    def get_succ_dates(self, Gx: Any, Gx_node: Any, core_x: Any, succ: Any): ...
    def one_hop(self, Gx: Any, Gx_node: Any, core_x: Any, pred: Any, succ: Any): ...
    def two_hop_pred(self, Gx: Any, Gx_node: Any, core_x: Any, pred: Any): ...
    def two_hop_succ(self, Gx: Any, Gx_node: Any, core_x: Any, succ: Any): ...
    def preds(self, Gx: Any, core_x: Any, v: Any, Gx_node: Optional[Any] = ...): ...
    def succs(self, Gx: Any, core_x: Any, v: Any, Gx_node: Optional[Any] = ...): ...
    def test_one(self, pred_dates: Any, succ_dates: Any): ...
    def test_two(self, pred_dates: Any, succ_dates: Any): ...
    def semantic_feasibility(self, G1_node: Any, G2_node: Any): ...
