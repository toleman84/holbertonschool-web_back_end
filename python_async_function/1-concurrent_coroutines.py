#!/usr/bin/env python3
"""
    doc
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
        Spawn `wait_random` `n` times with the specified `max_delay`.
        Return the list of all the delays (float values).
        The list of the delays should be in ascending order
        without using `sort()` because of concurrency.
    """
    delays: List[float] = []
    tasks: List = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return sorted(delays)
