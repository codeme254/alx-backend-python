#!/usr/bin/env python3

"""
Write a type-annotated function make_multiplier
takes a float multiplier as argument and returns a function
that multiplies a float by multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Outer type-annotated function that will return a function
    """
    def inner_function(num_float: float) -> float:
        """
        Inner function that takes in a float as an arguement
        Multiplies the float with multiplier
        Returns the result as a float
        """
        return multiplier * num_float
    return inner_function
