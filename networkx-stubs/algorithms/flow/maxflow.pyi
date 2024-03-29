from _typeshed import Incomplete

from .preflowpush import preflow_push

default_flow_func = preflow_push

def maximum_flow(
    flowG,
    _s,
    _t,
    capacity: str = "capacity",
    flow_func: Incomplete | None = None,
    **kwargs
): ...
def maximum_flow_value(
    flowG,
    _s,
    _t,
    capacity: str = "capacity",
    flow_func: Incomplete | None = None,
    **kwargs
): ...
def minimum_cut(
    flowG,
    _s,
    _t,
    capacity: str = "capacity",
    flow_func: Incomplete | None = None,
    **kwargs
): ...
def minimum_cut_value(
    flowG,
    _s,
    _t,
    capacity: str = "capacity",
    flow_func: Incomplete | None = None,
    **kwargs
): ...
