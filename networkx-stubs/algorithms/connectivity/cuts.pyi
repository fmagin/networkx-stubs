# Stubs for networkx.algorithms.connectivity.cuts (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from _typeshed import Incomplete

def minimum_st_edge_cut(
    G: Incomplete,
    s: Incomplete,
    t: Incomplete,
    flow_func: Incomplete | None = ...,
    auxiliary: Incomplete | None = ...,
    residual: Incomplete | None = ...,
) -> Incomplete: ...
def minimum_st_node_cut(
    G: Incomplete,
    s: Incomplete,
    t: Incomplete,
    flow_func: Incomplete | None = ...,
    auxiliary: Incomplete | None = ...,
    residual: Incomplete | None = ...,
) -> Incomplete: ...
def minimum_node_cut(
    G: Incomplete,
    s: Incomplete | None = ...,
    t: Incomplete | None = ...,
    flow_func: Incomplete | None = ...,
) -> Incomplete: ...
def minimum_edge_cut(
    G: Incomplete,
    s: Incomplete | None = ...,
    t: Incomplete | None = ...,
    flow_func: Incomplete | None = ...,
) -> Incomplete: ...
