#!/usr/bin/env python3
"""
    doc
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        Run time for four parallel comprehensions

        Args:
            No arguments.

        Return:
            Measure the total runtime and return it.
    """
    start_time = time.time()
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*tasks)

    return time.time() - start_time
