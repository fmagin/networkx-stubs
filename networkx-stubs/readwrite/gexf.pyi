# Stubs for networkx.readwrite.gexf (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def write_gexf(G: Any, path: Any, encoding: str = ..., prettyprint: bool = ..., version: str = ...) -> None: ...
def generate_gexf(G: Any, encoding: str = ..., prettyprint: bool = ..., version: str = ...) -> None: ...
def read_gexf(path: Any, node_type: Any | None = ..., relabel: bool = ..., version: str = ...) -> Any: ...

class GEXF:
    versions: Any = ...
    d: Any = ...
    types: Any = ...
    xml_type: Any = ...
    python_type: Any = ...
    convert_bool: Any = ...
    NS_GEXF: Any = ...
    NS_VIZ: Any = ...
    NS_XSI: Any = ...
    SCHEMALOCATION: Any = ...
    VERSION: Any = ...
    version: Any = ...
    def set_version(self, version: Any) -> None: ...

class GEXFWriter(GEXF):
    prettyprint: Any = ...
    encoding: Any = ...
    xml: Any = ...
    edge_id: Any = ...
    attr_id: Any = ...
    all_edge_ids: Any = ...
    attr: Any = ...
    def __init__(self, graph: Any | None = ..., encoding: str = ..., prettyprint: bool = ..., version: str = ...) -> None: ...
    graph_element: Any = ...
    def add_graph(self, G: Any) -> None: ...
    def add_meta(self, G: Any, graph_element: Any) -> None: ...
    def add_nodes(self, G: Any, graph_element: Any) -> None: ...
    def add_edges(self, G: Any, graph_element: Any) -> None: ...
    def add_attributes(self, node_or_edge: Any, xml_obj: Any, data: Any, default: Any) -> Any: ...
    def get_attr_id(self, title: Any, attr_type: Any, edge_or_node: Any, default: Any, mode: Any) -> Any: ...
    def add_viz(self, element: Any, node_data: Any) -> Any: ...
    def add_parents(self, node_element: Any, node_data: Any) -> Any: ...
    def add_slices(self, node_or_edge_element: Any, node_or_edge_data: Any) -> Any: ...
    def add_spells(self, node_or_edge_element: Any, node_or_edge_data: Any) -> Any: ...
    def alter_graph_mode_timeformat(self, start_or_end: Any) -> None: ...
    def write(self, fh: Any) -> None: ...
    def indent(self, elem: Any, level: int = ...) -> None: ...

class GEXFReader(GEXF):
    node_type: Any = ...
    simple_graph: bool = ...
    def __init__(self, node_type: Any | None = ..., version: str = ...) -> None: ...
    xml: Any = ...
    def __call__(self, stream: Any) -> Any: ...
    timeformat: Any = ...
    def make_graph(self, graph_xml: Any) -> Any: ...
    def add_node(self, G: Any, node_xml: Any, node_attr: Any, node_pid: Any | None = ...) -> None: ...
    def add_start_end(self, data: Any, xml: Any) -> Any: ...
    def add_viz(self, data: Any, node_xml: Any) -> Any: ...
    def add_parents(self, data: Any, node_xml: Any) -> Any: ...
    def add_slices(self, data: Any, node_or_edge_xml: Any) -> Any: ...
    def add_spells(self, data: Any, node_or_edge_xml: Any) -> Any: ...
    def add_edge(self, G: Any, edge_element: Any, edge_attr: Any) -> None: ...
    def decode_attr_elements(self, gexf_keys: Any, obj_xml: Any) -> Any: ...
    def find_gexf_attributes(self, attributes_element: Any) -> Any: ...

def relabel_gexf_graph(G: Any) -> Any: ...
