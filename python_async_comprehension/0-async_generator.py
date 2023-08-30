#!/usr/bin/env python3
"""
    doc
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
        A coroutine called async_generator that takes no arguments

        Args:
            No arguments.

        Return:
            Nothing.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
