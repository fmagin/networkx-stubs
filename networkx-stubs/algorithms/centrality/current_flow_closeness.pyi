# Stubs for networkx.algorithms.centrality.current_flow_closeness (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

from networkx.algorithms.centrality.flow_matrix import *

def current_flow_closeness_centrality(
    G: Any, weight: Any | None = ..., dtype: Any = ..., solver: str = ...
) -> Any: ...

information_centrality = current_flow_closeness_centrality
