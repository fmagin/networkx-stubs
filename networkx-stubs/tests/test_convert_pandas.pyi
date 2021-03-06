# Stubs for networkx.tests.test_convert_pandas (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class TestConvertPandas:
    numpy: int = ...
    @classmethod
    def setupClass(cls) -> None: ...
    rng: Any = ...
    df: Any = ...
    mdf: Any = ...
    def __init__(self) -> None: ...
    def test_exceptions(self) -> None: ...
    def test_from_edgelist_all_attr(self) -> None: ...
    def test_from_edgelist_multi_attr(self) -> None: ...
    def test_from_edgelist_multi_attr_incl_target(self) -> None: ...
    def test_from_edgelist_multidigraph_and_edge_attr(self) -> None: ...
    def test_from_edgelist_one_attr(self) -> None: ...
    def test_from_edgelist_int_attr_name(self) -> None: ...
    def test_from_edgelist_invalid_attr(self) -> None: ...
    def test_from_edgelist_no_attr(self) -> None: ...
    def test_from_edgelist(self) -> None: ...
    def test_from_adjacency(self) -> None: ...
    def test_roundtrip(self) -> None: ...
    def test_from_adjacency_named(self) -> None: ...
