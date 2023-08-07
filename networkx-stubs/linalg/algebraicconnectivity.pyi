# Stubs for networkx.linalg.algebraicconnectivity (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

from numpy import dot  # type: ignore

ddot = dot

class _PCGSolver:
    def __init__(self, A: Any, M: Any) -> None: ...
    def solve(self, B: Any, tol: Any): ...

class _CholeskySolver:
    def __init__(self, A: Any) -> None: ...
    def solve(self, B: Any, tol: Any | None = ...): ...

class _LUSolver:
    def __init__(self, A: Any) -> None: ...
    def solve(self, B: Any, tol: Any | None = ...): ...

def algebraic_connectivity(
    G: Any, weight: str = ..., normalized: bool = ..., tol: float = ..., method: str = ..., seed: Any | None = ...
): ...
def fiedler_vector(
    G: Any, weight: str = ..., normalized: bool = ..., tol: float = ..., method: str = ..., seed: Any | None = ...
): ...
def spectral_ordering(
    G: Any, weight: str = ..., normalized: bool = ..., tol: float = ..., method: str = ..., seed: Any | None = ...
): ...
def setup_module(module: Any) -> None: ...
