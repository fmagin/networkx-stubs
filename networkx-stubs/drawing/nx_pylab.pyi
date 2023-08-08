# Stubs for networkx.drawing.nx_pylab (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def draw(G: Any, pos: Any | None = ..., ax: Any | None = ..., **kwds: Any) -> None: ...
def draw_networkx(
    G: Any,
    pos: Any | None = ...,
    arrows: bool = ...,
    with_labels: bool = ...,
    **kwds: Any,
) -> None: ...
def draw_networkx_nodes(
    G: Any,
    pos: Any,
    nodelist: Any | None = ...,
    node_size: int = ...,
    node_color: str = ...,
    node_shape: str = ...,
    alpha: float = ...,
    cmap: Any | None = ...,
    vmin: Any | None = ...,
    vmax: Any | None = ...,
    ax: Any | None = ...,
    linewidths: Any | None = ...,
    edgecolors: Any | None = ...,
    label: Any | None = ...,
    **kwds: Any,
) -> Any: ...
def draw_networkx_edges(
    G: Any,
    pos: Any,
    edgelist: Any | None = ...,
    width: float = ...,
    edge_color: str = ...,
    style: str = ...,
    alpha: float = ...,
    arrowstyle: str = ...,
    arrowsize: int = ...,
    edge_cmap: Any | None = ...,
    edge_vmin: Any | None = ...,
    edge_vmax: Any | None = ...,
    ax: Any | None = ...,
    arrows: bool = ...,
    label: Any | None = ...,
    node_size: int = ...,
    nodelist: Any | None = ...,
    node_shape: str = ...,
    connectionstyle: Any | None = ...,
    **kwds: Any,
) -> Any: ...
def draw_networkx_labels(
    G: Any,
    pos: Any,
    labels: Any | None = ...,
    font_size: int = ...,
    font_color: str = ...,
    font_family: str = ...,
    font_weight: str = ...,
    alpha: float = ...,
    bbox: Any | None = ...,
    ax: Any | None = ...,
    **kwds: Any,
) -> Any: ...
def draw_networkx_edge_labels(
    G: Any,
    pos: Any,
    edge_labels: Any | None = ...,
    label_pos: float = ...,
    font_size: int = ...,
    font_color: str = ...,
    font_family: str = ...,
    font_weight: str = ...,
    alpha: float = ...,
    bbox: Any | None = ...,
    ax: Any | None = ...,
    rotate: bool = ...,
    **kwds: Any,
) -> Any: ...
def draw_circular(G: Any, **kwargs: Any) -> None: ...
def draw_kamada_kawai(G: Any, **kwargs: Any) -> None: ...
def draw_random(G: Any, **kwargs: Any) -> None: ...
def draw_spectral(G: Any, **kwargs: Any) -> None: ...
def draw_spring(G: Any, **kwargs: Any) -> None: ...
def draw_shell(G: Any, **kwargs: Any) -> None: ...
def draw_planar(G: Any, **kwargs: Any) -> None: ...
