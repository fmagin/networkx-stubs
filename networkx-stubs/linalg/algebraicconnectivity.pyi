# Stubs for networkx.linalg.algebraicconnectivity (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

from numpy import dot  # type: ignore

ddot = dot

class _PCGSolver:
    def __init__(self, A: Any, M: Any) -> None: ...
    def solve(self, B: Any, tol: Any) -> Incomplete: ...

class _CholeskySolver:
    def __init__(self, A: Any) -> None: ...
    def solve(self, B: Any, tol: Any | None = ...) -> Incomplete: ...

class _LUSolver:
    def __init__(self, A: Any) -> None: ...
    def solve(self, B: Any, tol: Any | None = ...) -> Incomplete: ...

def algebraic_connectivity(
    G: Any,
    weight: str = ...,
    normalized: bool = ...,
    tol: float = ...,
    method: str = ...,
    seed: Any | None = ...,
) -> Incomplete: ...
def fiedler_vector(
    G: Any,
    weight: str = ...,
    normalized: bool = ...,
    tol: float = ...,
    method: str = ...,
    seed: Any | None = ...,
) -> Incomplete: ...
def spectral_ordering(
    G: Any,
    weight: str = ...,
    normalized: bool = ...,
    tol: float = ...,
    method: str = ...,
    seed: Any | None = ...,
) -> Incomplete: ...
def setup_module(module: Any) -> None: ...
