#!/usr/bin/env python3
"""
    doc
"""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
        Run time for four parallel comprehensions

        Args:
            No arguments.

        Return:
            Measure the total runtime and return it.
    """
    start_time = time.time()
    for _ in range(4):
        tasks = asyncio.create_task(async_comprehension())
    await asyncio.gather(tasks)
    total_time = time.time() - start_time

    return total_time
