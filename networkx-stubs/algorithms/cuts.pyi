# Stubs for networkx.algorithms.cuts (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def cut_size(G: Any, S: Any, T: Any | None = ..., weight: Any | None = ...) -> Incomplete: ...
def volume(G: Any, S: Any, weight: Any | None = ...) -> Incomplete: ...
def normalized_cut_size(
    G: Any, S: Any, T: Any | None = ..., weight: Any | None = ...
) -> Incomplete: ...
def conductance(
    G: Any, S: Any, T: Any | None = ..., weight: Any | None = ...
) -> Incomplete: ...
def edge_expansion(
    G: Any, S: Any, T: Any | None = ..., weight: Any | None = ...
) -> Incomplete: ...
def mixing_expansion(
    G: Any, S: Any, T: Any | None = ..., weight: Any | None = ...
) -> Incomplete: ...
def node_expansion(G: Any, S: Any) -> Incomplete: ...
def boundary_expansion(G: Any, S: Any) -> Incomplete: ...
