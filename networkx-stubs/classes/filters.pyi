# Stubs for networkx.classes.filters (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def no_filter(*items: Any) -> Incomplete: ...
def hide_nodes(nodes: Any) -> Incomplete: ...
def hide_diedges(edges: Any) -> Incomplete: ...
def hide_edges(edges: Any) -> Incomplete: ...
def hide_multidiedges(edges: Any) -> Incomplete: ...
def hide_multiedges(edges: Any) -> Incomplete: ...

class show_nodes:
    nodes: Any = ...
    def __init__(self, nodes: Any) -> None: ...
    def __call__(self, node: Any) -> Incomplete: ...

def show_diedges(edges: Any) -> Incomplete: ...
def show_edges(edges: Any) -> Incomplete: ...
def show_multidiedges(edges: Any) -> Incomplete: ...
def show_multiedges(edges: Any) -> Incomplete: ...
