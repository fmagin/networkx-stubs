from _typeshed import Incomplete

def fast_gnp_random_graph(
    n, p, seed: Incomplete | None = None, directed: bool = False
): ...
def gnp_random_graph(n, p, seed: Incomplete | None = None, directed: bool = False): ...

binomial_graph = gnp_random_graph
erdos_renyi_graph = gnp_random_graph

def dense_gnm_random_graph(n, m, seed: Incomplete | None = None): ...
def gnm_random_graph(n, m, seed: Incomplete | None = None, directed: bool = False): ...
def newman_watts_strogatz_graph(n, k, p, seed: Incomplete | None = None): ...
def watts_strogatz_graph(n, k, p, seed: Incomplete | None = None): ...
def connected_watts_strogatz_graph(
    n, k, p, tries: int = 100, seed: Incomplete | None = None
): ...
def random_regular_graph(d, n, seed: Incomplete | None = None): ...
def barabasi_albert_graph(
    n, m, seed: Incomplete | None = None, initial_graph: Incomplete | None = None
): ...
def dual_barabasi_albert_graph(
    n,
    m1,
    m2,
    p,
    seed: Incomplete | None = None,
    initial_graph: Incomplete | None = None,
): ...
def extended_barabasi_albert_graph(n, m, p, q, seed: Incomplete | None = None): ...
def powerlaw_cluster_graph(n, m, p, seed: Incomplete | None = None): ...
def random_lobster(n, p1, p2, seed: Incomplete | None = None): ...
def random_shell_graph(constructor, seed: Incomplete | None = None): ...
def random_powerlaw_tree(
    n, gamma: int = 3, seed: Incomplete | None = None, tries: int = 100
): ...
def random_powerlaw_tree_sequence(
    n, gamma: int = 3, seed: Incomplete | None = None, tries: int = 100
): ...
def random_kernel_graph(
    n,
    kernel_integral,
    kernel_root: Incomplete | None = None,
    seed: Incomplete | None = None,
): ...
