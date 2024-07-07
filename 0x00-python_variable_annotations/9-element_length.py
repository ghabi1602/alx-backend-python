#!/usr/bin/env python3
"""function element_lenght definition"""
from typing import Tuple, List, Iterable


def element_length(lst: Iterable) -> List[Tuple[Iterable, int]]:
    """returns a list of tuples"""
    return [(i, len(i)) for i in lst]
