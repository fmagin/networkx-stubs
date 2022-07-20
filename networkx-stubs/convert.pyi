from typing import Dict, Iterable, Any, Union
from typing_extensions import TypeAlias

from networkx.classes.graph import EdgePlus, Graph, Node

import numpy  # type: ignore
import scipy  # type: ignore

Data = Union[
    Graph[Node],
    Dict[Node, Dict[Node, Dict[str, Any]]],
    Dict[Node, Iterable[Node]],
    Iterable[EdgePlus[Node]],
    numpy.ndarray,
    scipy.sparse.base.spmatrix,
]