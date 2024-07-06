#!/usr/bin/env python3
"""function sum_mixed_list definition"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """returns the sum of a mixed list"""
    if mxd_list is None:
        return 0
    else:
        return sum(mxd_list)
