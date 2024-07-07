#!/usr/bin/env python3
"""safe_first_element function definition"""
from typing import Optional, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """returns the first element otherwise None"""
    if lst:
        return lst[0]
    else:
        return None
