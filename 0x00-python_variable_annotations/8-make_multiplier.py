#!/usr/bin/env python3

"""
Write a type-annotated function make_multiplier
takes a float multiplier as argument and returns a function
that multiplies a float by multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def inner_function(num_float: float) -> float:
        return multiplier * num_float
    return inner_function
