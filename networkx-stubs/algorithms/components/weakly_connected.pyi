from collections.abc import Iterable
from typing import Incomplete, TypeVar

from networkx.classes.graph import Graph

_N = TypeVar("_N")

def weakly_connected_components(G: Graph[_N]) -> Iterable[set[_N]]: ...
def number_weakly_connected_components(G: Graph[Incomplete]) -> int: ...
def is_weakly_connected(G: Graph[Incomplete]) -> bool: ...
