# Stubs for networkx.generators.lattice (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def grid_2d_graph(
    m: Any, n: Any, periodic: bool = ..., create_using: Any | None = ...
) -> Any: ...
def grid_graph(dim: Any, periodic: bool = ...) -> Any: ...
def hypercube_graph(n: Any) -> Any: ...
def triangular_lattice_graph(
    m: Any,
    n: Any,
    periodic: bool = ...,
    with_positions: bool = ...,
    create_using: Any | None = ...,
) -> Any: ...
def hexagonal_lattice_graph(
    m: Any,
    n: Any,
    periodic: bool = ...,
    with_positions: bool = ...,
    create_using: Any | None = ...,
) -> Any: ...
