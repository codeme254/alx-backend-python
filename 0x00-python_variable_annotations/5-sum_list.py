#!/usr/bin/env python3

"""
function sum_list which takes a list input_list of floats as argument
returns their sum as a float.
"""

import typing

def sum_list(input_list: typing.List[float]) -> float:
    """
    Takes a list of floats as an arguement and returns their sum as a float
    """
    final_sum = 0
    for val in input_list:
        final_sum += val
    
    return final_sum
