#!/usr/bin/env python3
"""
    doc
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        Asynchronous coroutine that waits for a random delay between 0
        and max_delay seconds.

        Args:
            max_delay: The maximum delay in seconds.

        Returns:
            The number of seconds waited.
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
