# functions.py
from typeguard import typechecked

@typechecked
def sum(x: int, y: int) -> int:
    """Computes the sum of two integers."""
    return x + y