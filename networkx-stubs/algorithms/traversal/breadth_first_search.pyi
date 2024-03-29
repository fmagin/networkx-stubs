from _typeshed import Incomplete
from collections.abc import Generator

def bfs_edges(
    G,
    source,
    reverse: bool = False,
    depth_limit: Incomplete | None = None,
    sort_neighbors: Incomplete | None = None,
) -> Generator[Incomplete, Incomplete, None]: ...
def bfs_tree(
    G,
    source,
    reverse: bool = False,
    depth_limit: Incomplete | None = None,
    sort_neighbors: Incomplete | None = None,
): ...
def bfs_predecessors(
    G,
    source,
    depth_limit: Incomplete | None = None,
    sort_neighbors: Incomplete | None = None,
) -> Generator[Incomplete, None, None]: ...
def bfs_successors(
    G,
    source,
    depth_limit: Incomplete | None = None,
    sort_neighbors: Incomplete | None = None,
) -> Generator[Incomplete, None, None]: ...
def bfs_layers(G, sources) -> Generator[Incomplete, None, None]: ...
def descendants_at_distance(G, source, distance): ...
