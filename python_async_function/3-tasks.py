
#!/usr/bin/env python3
import asyncio
from typing import Callable


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return an asyncio.Task that waits for a random delay."""
    from random import uniform

    async def wait_random():
        delay = uniform(0, max_delay)
        await asyncio.sleep(delay)
        return delay

    return asyncio.create_task(wait_random())
