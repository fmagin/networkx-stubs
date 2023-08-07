from typing import Any
from collections.abc import Iterable

import numpy
import scipy
from networkx.classes.graph import EdgePlus, Graph, Node

Data = Graph[Node] | dict[Node, dict[Node, dict[str, Any]]] | dict[Node, Iterable[Node]] | Iterable[EdgePlus[Node]] | numpy.ndarray[Node, Any] | scipy.sparse.base.spmatrix
