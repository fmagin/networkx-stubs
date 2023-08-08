# Stubs for networkx.generators.random_graphs (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def fast_gnp_random_graph(
    n: Any, p: Any, seed: Any | None = ..., directed: bool = ...
) -> Any: ...
def gnp_random_graph(
    n: Any, p: Any, seed: Any | None = ..., directed: bool = ...
) -> Any: ...

binomial_graph = gnp_random_graph
erdos_renyi_graph = gnp_random_graph

def dense_gnm_random_graph(n: Any, m: Any, seed: Any | None = ...) -> Any: ...
def gnm_random_graph(
    n: Any, m: Any, seed: Any | None = ..., directed: bool = ...
) -> Any: ...
def newman_watts_strogatz_graph(
    n: Any, k: Any, p: Any, seed: Any | None = ...
) -> Any: ...
def watts_strogatz_graph(n: Any, k: Any, p: Any, seed: Any | None = ...) -> Any: ...
def connected_watts_strogatz_graph(
    n: Any, k: Any, p: Any, tries: int = ..., seed: Any | None = ...
) -> Any: ...
def random_regular_graph(d: Any, n: Any, seed: Any | None = ...) -> Any: ...
def barabasi_albert_graph(n: Any, m: Any, seed: Any | None = ...) -> Any: ...
def dual_barabasi_albert_graph(
    n: Any, m1: Any, m2: Any, p: Any, seed: Any | None = ...
) -> Any: ...
def extended_barabasi_albert_graph(
    n: Any, m: Any, p: Any, q: Any, seed: Any | None = ...
) -> Any: ...
def powerlaw_cluster_graph(n: Any, m: Any, p: Any, seed: Any | None = ...) -> Any: ...
def random_lobster(n: Any, p1: Any, p2: Any, seed: Any | None = ...) -> Any: ...
def random_shell_graph(constructor: Any, seed: Any | None = ...) -> Any: ...
def random_powerlaw_tree(
    n: Any, gamma: int = ..., seed: Any | None = ..., tries: int = ...
) -> Any: ...
def random_powerlaw_tree_sequence(
    n: Any, gamma: int = ..., seed: Any | None = ..., tries: int = ...
) -> Any: ...
def random_kernel_graph(
    n: Any, kernel_integral: Any, kernel_root: Any | None = ..., seed: Any | None = ...
) -> Any: ...
