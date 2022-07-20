# Stubs for networkx.algorithms.connectivity.disjoint_paths (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from networkx.algorithms.flow import edmonds_karp
from typing import Any, Optional

def edge_disjoint_paths(G: Any, s: Any, t: Any, flow_func: Optional[Any] = ..., cutoff: Optional[Any] = ..., auxiliary: Optional[Any] = ..., residual: Optional[Any] = ...) -> None: ...
def node_disjoint_paths(G: Any, s: Any, t: Any, flow_func: Optional[Any] = ..., cutoff: Optional[Any] = ..., auxiliary: Optional[Any] = ..., residual: Optional[Any] = ...) -> None: ...
