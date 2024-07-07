#!/usr/bin/env python3
"""function to_kv definition"""
from typing import Tuple


def to_kv(k: str, v: float) -> Tuple[str, float]:
    """returns a tuple"""
    return (k, v * v)
