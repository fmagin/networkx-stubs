# Stubs for networkx.classes.graphviews (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def generic_graph_view(G: Any, create_using: Any | None = ...) -> Any: ...
def subgraph_view(G: Any, filter_node: Any = ..., filter_edge: Any = ...) -> Any: ...
def reverse_view(G: Any) -> Any: ...
def ReverseView(G: Any) -> Any: ...
def SubGraph(G: Any, filter_node: Any = ..., filter_edge: Any = ...) -> Any: ...
def GraphView(G: Any) -> Any: ...
def DiGraphView(G: Any) -> Any: ...
def MultiGraphView(G: Any) -> Any: ...
def MultiDiGraphView(G: Any) -> Any: ...

MultiReverseView = ReverseView
SubMultiGraph = SubGraph
SubMultiDiGraph = SubGraph
SubDiGraph = SubGraph
