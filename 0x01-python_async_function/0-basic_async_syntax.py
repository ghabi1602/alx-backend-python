#!/usr/bin/env python3
"""wait_random coroutine definition"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """gets a random delay then returns it"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
