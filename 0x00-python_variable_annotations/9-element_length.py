#!/usr/bin/env python3
"""function element_lenght definition"""
from typing import Tuple, List


def element_length(lst: List) -> List[Tuple[str, int]]:
    """returns a list of tuples"""
    return [(i, len(i)) for i in lst]
