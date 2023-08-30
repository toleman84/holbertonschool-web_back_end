#!/usr/bin/env python3
"""
    doc
"""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
        Takes an integer max_delay and returns a asyncio.Task.

        Args:
            max_delay: The maximum delay in seconds.

        Returns:
            A asyncio.Task that waits for a random amount of time up
            to max_delay.
    """
    return asyncio.Task(wait_random(max_delay))
