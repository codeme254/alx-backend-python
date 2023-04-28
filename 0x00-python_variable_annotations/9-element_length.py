#!/usr/bin/env python3

"""
Annotating a functions parameter and return values with appropriate types
"""
from typing import Iterable, Sequence, List, Union, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This is to be the expected output
    {'lst': typing.Iterable[typing.Sequence],
    'return': typing.List[typing.Tuple[typing.Sequence, int]]}
    So we are annotating the  code to return something of the sort
    """
    return [(i, len(i)) for i in lst]
