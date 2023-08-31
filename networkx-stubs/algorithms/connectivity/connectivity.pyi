# Stubs for networkx.algorithms.connectivity.connectivity (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def local_node_connectivity(
    G: Any,
    s: Any,
    t: Any,
    flow_func: Any | None = ...,
    auxiliary: Any | None = ...,
    residual: Any | None = ...,
    cutoff: Any | None = ...,
) -> Incomplete: ...
def node_connectivity(
    G: Any, s: Any | None = ..., t: Any | None = ..., flow_func: Any | None = ...
) -> Incomplete: ...
def average_node_connectivity(G: Any, flow_func: Any | None = ...) -> Incomplete: ...
def all_pairs_node_connectivity(
    G: Any, nbunch: Any | None = ..., flow_func: Any | None = ...
) -> Incomplete: ...
def local_edge_connectivity(
    G: Any,
    s: Any,
    t: Any,
    flow_func: Any | None = ...,
    auxiliary: Any | None = ...,
    residual: Any | None = ...,
    cutoff: Any | None = ...,
) -> Incomplete: ...
def edge_connectivity(
    G: Any,
    s: Any | None = ...,
    t: Any | None = ...,
    flow_func: Any | None = ...,
    cutoff: Any | None = ...,
) -> Incomplete: ...
