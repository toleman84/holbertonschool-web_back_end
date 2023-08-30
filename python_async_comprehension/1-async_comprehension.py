#!/usr/bin/env python3
"""
    doc
"""

import asyncio
import time


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
        collect 10 random numbers using an async comprehensing
        over async_generator

        Args:
            No arguments.

        Return:
            The 10 random numbers.
    """
    return [num async for num in async_generator()if num % 2 == 0][:10]
