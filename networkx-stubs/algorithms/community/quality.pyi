# Stubs for networkx.algorithms.community.quality (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

from networkx import NetworkXError

class NotAPartition(NetworkXError):
    def __init__(self, G: Any, collection: Any) -> None: ...

def performance(G: Any, partition: Any): ...
def coverage(G: Any, partition: Any): ...
def modularity(G: Any, communities: Any, weight: str = ...): ...
