# Stubs for networkx.algorithms.link_prediction (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def resource_allocation_index(G: Any, ebunch: Any | None = ...) -> Any: ...
def jaccard_coefficient(G: Any, ebunch: Any | None = ...) -> Any: ...
def adamic_adar_index(G: Any, ebunch: Any | None = ...) -> Any: ...
def preferential_attachment(G: Any, ebunch: Any | None = ...) -> Any: ...
def cn_soundarajan_hopcroft(
    G: Any, ebunch: Any | None = ..., community: str = ...
) -> Any: ...
def ra_index_soundarajan_hopcroft(
    G: Any, ebunch: Any | None = ..., community: str = ...
) -> Any: ...
def within_inter_cluster(
    G: Any, ebunch: Any | None = ..., delta: float = ..., community: str = ...
) -> Any: ...
