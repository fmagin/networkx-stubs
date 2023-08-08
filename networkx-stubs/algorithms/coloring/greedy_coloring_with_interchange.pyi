# Stubs for networkx.algorithms.coloring.greedy_coloring_with_interchange (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class _Node:
    node_id: Any = ...
    color: int = ...
    adj_list: Any = ...
    adj_color: Any = ...
    def __init__(self, node_id: Any, n: Any) -> None: ...
    def assign_color(self, adj_entry: Any, color: Any) -> None: ...
    def clear_color(self, adj_entry: Any, color: Any) -> None: ...
    def iter_neighbors(self) -> None: ...
    def iter_neighbors_color(self, color: Any) -> None: ...

class AdjEntry:
    node_id: Any = ...
    next: Any = ...
    mate: Any = ...
    col_next: Any = ...
    col_prev: Any = ...
    def __init__(self, node_id: Any) -> None: ...

def greedy_coloring_with_interchange(original_graph: Any, nodes: Any) -> Any: ...
