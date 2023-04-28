#!/usr/bin/env python3

"""
a type-annotated function sum_mixed_list
takes a list mxd_lst of integers and floats and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    takes a list that is made up of floats and integers
    Returns the sum as a float
    """
    final_sum = 0
    for val in mxd_lst:
        final_sum += val
    return final_sum
