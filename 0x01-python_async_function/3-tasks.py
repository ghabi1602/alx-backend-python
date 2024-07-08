#!/usr/bin/env python3
"""task_wait_random function definition"""
import asyncio


wait_random = __import__('0-basic_async_syntax')


def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns an asyncio task"""
    return asyncio.create_task(wait_random(max_delay))
