from typing import Iterable

def add(a, b):
    return a + b

def my_sum(it: Iterable[int]) -> int:
    """Return some of all items in iterable."""
    return sum(it)

def my_div(a, b):
    """Divide two objects."""
    return a / b
