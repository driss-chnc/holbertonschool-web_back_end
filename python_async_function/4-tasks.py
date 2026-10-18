#!/usr/bin/env python3
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay):
    tasks = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
