# Stubs for networkx.algorithms.shortest_paths.dense (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def floyd_warshall_numpy(
    G: Any, nodelist: Any | None = ..., weight: str = ...
) -> Any: ...
def floyd_warshall_predecessor_and_distance(G: Any, weight: str = ...) -> Any: ...
def reconstruct_path(source: Any, target: Any, predecessors: Any) -> Any: ...
def floyd_warshall(G: Any, weight: str = ...) -> Any: ...
