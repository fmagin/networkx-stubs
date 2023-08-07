# Stubs for networkx.algorithms.centrality.current_flow_betweenness (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

from networkx.algorithms.centrality.flow_matrix import *

def approximate_current_flow_betweenness_centrality(
    G: Any,
    normalized: bool = ...,
    weight: Any | None = ...,
    dtype: Any = ...,
    solver: str = ...,
    epsilon: float = ...,
    kmax: int = ...,
    seed: Any | None = ...,
): ...
def current_flow_betweenness_centrality(
    G: Any, normalized: bool = ..., weight: Any | None = ..., dtype: Any = ..., solver: str = ...
): ...
def edge_current_flow_betweenness_centrality(
    G: Any, normalized: bool = ..., weight: Any | None = ..., dtype: Any = ..., solver: str = ...
): ...
