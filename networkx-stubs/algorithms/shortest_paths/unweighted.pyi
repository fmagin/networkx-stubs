# Stubs for networkx.algorithms.shortest_paths.unweighted (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from _typeshed import Incomplete

def single_source_shortest_path_length(
    G: Any, source: Any, cutoff: Any | None = ...
) -> Incomplete: ...
def single_target_shortest_path_length(
    G: Any, target: Any, cutoff: Any | None = ...
) -> Incomplete: ...
def all_pairs_shortest_path_length(G: Any, cutoff: Any | None = ...) -> None: ...
def bidirectional_shortest_path(G: Any, source: Any, target: Any) -> Incomplete: ...
def single_source_shortest_path(
    G: Any, source: Any, cutoff: Any | None = ...
) -> Incomplete: ...
def single_target_shortest_path(
    G: Any, target: Any, cutoff: Any | None = ...
) -> Incomplete: ...
def all_pairs_shortest_path(G: Any, cutoff: Any | None = ...) -> None: ...
def predecessor(
    G: Any,
    source: Any,
    target: Any | None = ...,
    cutoff: Any | None = ...,
    return_seen: Any | None = ...,
) -> Incomplete: ...
