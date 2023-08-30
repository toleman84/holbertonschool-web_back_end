#!/usr/bin/env python3
"""
    doc
"""

import asyncio
import random


async def async_generator():
    """
        A coroutine called async_generator that takes no arguments

        Args:
            No arguments.

        Return:
            Nothing.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(1, 10)
