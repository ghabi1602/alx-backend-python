#!/usr/bin/env python3
"""wait_n coroutine definition"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> float:
    """return wait_random n times"""
    randlist = []
    for i in range(n):
        delay = await wait_random(max_delay)
        randlist.append(delay)

    return randlist
