from _typeshed import Incomplete

def to_latex_raw(
    G,
    pos: str = "pos",
    tikz_options: str = "",
    default_node_options: str = "",
    node_options: str = "node_options",
    node_label: str = "label",
    default_edge_options: str = "",
    edge_options: str = "edge_options",
    edge_label: str = "label",
    edge_label_options: str = "edge_label_options",
): ...
def to_latex(
    Gbunch,
    pos: str = "pos",
    tikz_options: str = "",
    default_node_options: str = "",
    node_options: str = "node_options",
    node_label: str = "node_label",
    default_edge_options: str = "",
    edge_options: str = "edge_options",
    edge_label: str = "edge_label",
    edge_label_options: str = "edge_label_options",
    caption: str = "",
    latex_label: str = "",
    sub_captions: Incomplete | None = None,
    sub_labels: Incomplete | None = None,
    n_rows: int = 1,
    as_document: bool = True,
    document_wrapper="\\documentclass{{report}}\n\\usepackage{{tikz}}\n\\usepackage{{subcaption}}\n\n\\begin{{document}}\n{content}\n\\end{{document}}",
    figure_wrapper="\\begin{{figure}}\n{content}{caption}{label}\n\\end{{figure}}",
    subfigure_wrapper="  \\begin{{subfigure}}{{{size}\\textwidth}}\n{content}{caption}{label}\n  \\end{{subfigure}}",
): ...
def write_latex(Gbunch, path, **options) -> None: ...
