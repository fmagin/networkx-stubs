from _typeshed import Incomplete
from collections.abc import Generator

def dijkstra_path(G, source, target, weight: str = "weight"): ...
def dijkstra_path_length(G, source, target, weight: str = "weight"): ...
def single_source_dijkstra_path(
    G, source, cutoff: Incomplete | None = None, weight: str = "weight"
): ...
def single_source_dijkstra_path_length(
    G, source, cutoff: Incomplete | None = None, weight: str = "weight"
): ...
def single_source_dijkstra(
    G,
    source,
    target: Incomplete | None = None,
    cutoff: Incomplete | None = None,
    weight: str = "weight",
): ...
def multi_source_dijkstra_path(
    G, sources, cutoff: Incomplete | None = None, weight: str = "weight"
): ...
def multi_source_dijkstra_path_length(
    G, sources, cutoff: Incomplete | None = None, weight: str = "weight"
): ...
def multi_source_dijkstra(
    G,
    sources,
    target: Incomplete | None = None,
    cutoff: Incomplete | None = None,
    weight: str = "weight",
): ...
def dijkstra_predecessor_and_distance(
    G, source, cutoff: Incomplete | None = None, weight: str = "weight"
): ...
def all_pairs_dijkstra(
    G, cutoff: Incomplete | None = None, weight: str = "weight"
) -> Generator[Incomplete, None, None]: ...
def all_pairs_dijkstra_path_length(
    G, cutoff: Incomplete | None = None, weight: str = "weight"
) -> Generator[Incomplete, None, None]: ...
def all_pairs_dijkstra_path(
    G, cutoff: Incomplete | None = None, weight: str = "weight"
) -> Generator[Incomplete, None, None]: ...
def bellman_ford_predecessor_and_distance(
    G,
    source,
    target: Incomplete | None = None,
    weight: str = "weight",
    heuristic: bool = False,
): ...
def bellman_ford_path(G, source, target, weight: str = "weight"): ...
def bellman_ford_path_length(G, source, target, weight: str = "weight"): ...
def single_source_bellman_ford_path(G, source, weight: str = "weight"): ...
def single_source_bellman_ford_path_length(G, source, weight: str = "weight"): ...
def single_source_bellman_ford(
    G, source, target: Incomplete | None = None, weight: str = "weight"
): ...
def all_pairs_bellman_ford_path_length(
    G, weight: str = "weight"
) -> Generator[Incomplete, None, None]: ...
def all_pairs_bellman_ford_path(
    G, weight: str = "weight"
) -> Generator[Incomplete, None, None]: ...
def goldberg_radzik(G, source, weight: str = "weight"): ...
def negative_edge_cycle(G, weight: str = "weight", heuristic: bool = True): ...
def find_negative_cycle(G, source, weight: str = "weight"): ...
def bidirectional_dijkstra(G, source, target, weight: str = "weight"): ...
def johnson(G, weight: str = "weight"): ...
