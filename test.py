import networkx



g = networkx.Graph([1,2,3,4]) # type: networkx.Graph[int]
reveal_type(g.nodes)
reveal_type(list(g.nodes.__iter__()))
reveal_type(list(g.nodes))