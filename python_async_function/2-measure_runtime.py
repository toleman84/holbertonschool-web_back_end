#!/usr/bin/env python3
"""
    doc
"""

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        Measures the total execution time for wait_n(n, max_delay).

        Args:
            n: The number of times to call wait_n.
            max_delay: The maximum delay in seconds for each call to wait_n.

        Returns:
            A float representing the average execution time per call to wait_n.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time

    return total_time / n
