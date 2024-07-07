#!/usr/bin/env python3
"""function to_kv definition"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """returns a tuple"""
    return (k, v * v)
