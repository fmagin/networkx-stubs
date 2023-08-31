# Stubs for networkx.algorithms.similarity (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from operator import *
from typing import Any

def graph_edit_distance(
    G1: Any,
    G2: Any,
    node_match: Any | None = ...,
    edge_match: Any | None = ...,
    node_subst_cost: Any | None = ...,
    node_del_cost: Any | None = ...,
    node_ins_cost: Any | None = ...,
    edge_subst_cost: Any | None = ...,
    edge_del_cost: Any | None = ...,
    edge_ins_cost: Any | None = ...,
    upper_bound: Any | None = ...,
) -> Incomplete: ...
def optimal_edit_paths(
    G1: Any,
    G2: Any,
    node_match: Any | None = ...,
    edge_match: Any | None = ...,
    node_subst_cost: Any | None = ...,
    node_del_cost: Any | None = ...,
    node_ins_cost: Any | None = ...,
    edge_subst_cost: Any | None = ...,
    edge_del_cost: Any | None = ...,
    edge_ins_cost: Any | None = ...,
    upper_bound: Any | None = ...,
) -> Incomplete: ...
def optimize_graph_edit_distance(
    G1: Any,
    G2: Any,
    node_match: Any | None = ...,
    edge_match: Any | None = ...,
    node_subst_cost: Any | None = ...,
    node_del_cost: Any | None = ...,
    node_ins_cost: Any | None = ...,
    edge_subst_cost: Any | None = ...,
    edge_del_cost: Any | None = ...,
    edge_ins_cost: Any | None = ...,
    upper_bound: Any | None = ...,
) -> None: ...
def optimize_edit_paths(
    G1: Any,
    G2: Any,
    node_match: Any | None = ...,
    edge_match: Any | None = ...,
    node_subst_cost: Any | None = ...,
    node_del_cost: Any | None = ...,
    node_ins_cost: Any | None = ...,
    edge_subst_cost: Any | None = ...,
    edge_del_cost: Any | None = ...,
    edge_ins_cost: Any | None = ...,
    upper_bound: Any | None = ...,
    strictly_decreasing: bool = ...,
) -> Incomplete: ...
