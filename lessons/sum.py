"""Summing the elements of a list using different loops."""
__author__ = "730668208"


def w_sum(vals: list[float]) -> float:
    """Adds all of the numbers in a list using while loop."""
    i = 0
    result = 0.0
    if len(vals) == 0:
        result = 0.0
        return result
    while i < len(vals):
        result += vals[i]
        i += 1
    return result


def f_sum(vals: list[float]) -> float:
    """Adds all of the numbers in a list using for loop."""
    result = 0.0
    if len(vals) == 0:
        result = 0.0
        return result
    for elem in vals:
        result += elem
    return result


def f_range_sum(vals: list[float]) -> float:
    """Adds all of the numbers in a list using for in range loop."""
    result = 0.0
    if len(vals) == 0:
        result = 0.0
        return result
    for idx in range(0, len(vals)):
        elem = float(vals[idx])
        result += elem
    return result

turtle = "hi"