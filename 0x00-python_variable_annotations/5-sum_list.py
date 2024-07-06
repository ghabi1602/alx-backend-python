#!/usr/bin/env python3
"""funtion sum_list definition"""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """sum_list that returns the sum of list values"""
    if input_list is None:
        return 0
    else:
        return sum(input_list)
