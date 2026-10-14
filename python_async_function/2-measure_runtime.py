#!/usr/bin/env python3
"""Module for measuring the execution time of wait_n."""

import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average execution time per coroutine."""
    start = time.time()
    asyncio_run = __import__('asyncio').run
    asyncio_run(wait_n(n, max_delay))
    end = time.time()

    total_time = end - start
    return total_time / n
