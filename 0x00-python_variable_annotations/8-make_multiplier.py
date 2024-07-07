#!/usr/bin/env python3
"""function make_multiplier definition"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a funtion that multiplies a float by multiplier"""
    def func(v: float) -> float:
        """the callable function definition"""
        return v * multiplier

    return func
