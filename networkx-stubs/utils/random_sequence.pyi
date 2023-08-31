# Stubs for networkx.utils.random_sequence (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from _typeshed import Incomplete

def powerlaw_sequence(
    n: Incomplete, exponent: float = ..., seed: Incomplete | None = ...
) -> Incomplete: ...
def zipf_rv(
    alpha: Incomplete, xmin: int = ..., seed: Incomplete | None = ...
) -> Incomplete: ...
def cumulative_distribution(distribution: Incomplete) -> Incomplete: ...
def discrete_sequence(
    n: Incomplete,
    distribution: Incomplete | None = ...,
    cdistribution: Incomplete | None = ...,
    seed: Incomplete | None = ...,
) -> Incomplete: ...
def random_weighted_sample(
    mapping: Incomplete, k: Incomplete, seed: Incomplete | None = ...
) -> Incomplete: ...
def weighted_choice(
    mapping: Incomplete, seed: Incomplete | None = ...
) -> Incomplete: ...
