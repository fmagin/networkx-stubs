# Stubs for networkx.drawing.layout (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def random_layout(
    G: Any, center: Any | None = ..., dim: int = ..., seed: Any | None = ...
) -> Incomplete: ...
def circular_layout(
    G: Any, scale: int = ..., center: Any | None = ..., dim: int = ...
) -> Incomplete: ...
def shell_layout(
    G: Any,
    nlist: Any | None = ...,
    scale: int = ...,
    center: Any | None = ...,
    dim: int = ...,
) -> Incomplete: ...
def bipartite_layout(
    G: Any,
    nodes: Any,
    align: str = ...,
    scale: int = ...,
    center: Any | None = ...,
    aspect_ratio: Any = ...,
) -> Incomplete: ...
def fruchterman_reingold_layout(
    G: Any,
    k: Any | None = ...,
    pos: Any | None = ...,
    fixed: Any | None = ...,
    iterations: int = ...,
    threshold: float = ...,
    weight: str = ...,
    scale: int = ...,
    center: Any | None = ...,
    dim: int = ...,
    seed: Any | None = ...,
) -> Incomplete: ...

spring_layout = fruchterman_reingold_layout

def kamada_kawai_layout(
    G: Any,
    dist: Any | None = ...,
    pos: Any | None = ...,
    weight: str = ...,
    scale: int = ...,
    center: Any | None = ...,
    dim: int = ...,
) -> Incomplete: ...
def spectral_layout(
    G: Any,
    weight: str = ...,
    scale: int = ...,
    center: Any | None = ...,
    dim: int = ...,
) -> Incomplete: ...
def planar_layout(
    G: Any, scale: int = ..., center: Any | None = ..., dim: int = ...
) -> Incomplete: ...
def rescale_layout(pos: Any, scale: int = ...) -> Incomplete: ...
