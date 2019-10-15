import networkx


from typing import Generic, TypeVar



g = networkx.DiGraph([(1,2), (2,3)])  # type: networkx.DiGraph[int]
h = networkx.DiGraph([('a','b'), ('b','c')])  # type: networkx.DiGraph[str]

reveal_type(g)
reveal_type(h)

j = networkx.compose(g, h)

reveal_type(j)


