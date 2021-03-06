# Stubs for networkx.algorithms.cuts (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def cut_size(G: Any, S: Any, T: Optional[Any] = ..., weight: Optional[Any] = ...): ...
def volume(G: Any, S: Any, weight: Optional[Any] = ...): ...
def normalized_cut_size(G: Any, S: Any, T: Optional[Any] = ..., weight: Optional[Any] = ...): ...
def conductance(G: Any, S: Any, T: Optional[Any] = ..., weight: Optional[Any] = ...): ...
def edge_expansion(G: Any, S: Any, T: Optional[Any] = ..., weight: Optional[Any] = ...): ...
def mixing_expansion(G: Any, S: Any, T: Optional[Any] = ..., weight: Optional[Any] = ...): ...
def node_expansion(G: Any, S: Any): ...
def boundary_expansion(G: Any, S: Any): ...
