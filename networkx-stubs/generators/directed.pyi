# Stubs for networkx.generators.directed (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from _typeshed import Incomplete

def gn_graph(
    n: Incomplete,
    kernel: Incomplete | None = ...,
    create_using: Incomplete | None = ...,
    seed: Incomplete | None = ...,
) -> Incomplete: ...
def gnr_graph(
    n: Incomplete,
    p: Incomplete,
    create_using: Incomplete | None = ...,
    seed: Incomplete | None = ...,
) -> Incomplete: ...
def gnc_graph(
    n: Incomplete, create_using: Incomplete | None = ..., seed: Incomplete | None = ...
) -> Incomplete: ...
def scale_free_graph(
    n: Incomplete,
    alpha: float = ...,
    beta: float = ...,
    gamma: float = ...,
    delta_in: float = ...,
    delta_out: int = ...,
    create_using: Incomplete | None = ...,
    seed: Incomplete | None = ...,
) -> Incomplete: ...
def random_k_out_graph(
    n: Incomplete,
    k: Incomplete,
    alpha: Incomplete,
    self_loops: bool = ...,
    seed: Incomplete | None = ...,
) -> Incomplete: ...
