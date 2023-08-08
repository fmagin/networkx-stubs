# Stubs for networkx.readwrite.multiline_adjlist (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def generate_multiline_adjlist(G: Any, delimiter: str = ...) -> None: ...
def write_multiline_adjlist(
    G: Any, path: Any, delimiter: str = ..., comments: str = ..., encoding: str = ...
) -> None: ...
def parse_multiline_adjlist(
    lines: Any,
    comments: str = ...,
    delimiter: Any | None = ...,
    create_using: Any | None = ...,
    nodetype: Any | None = ...,
    edgetype: Any | None = ...,
) -> Any: ...
def read_multiline_adjlist(
    path: Any,
    comments: str = ...,
    delimiter: Any | None = ...,
    create_using: Any | None = ...,
    nodetype: Any | None = ...,
    edgetype: Any | None = ...,
    encoding: str = ...,
) -> Any: ...
