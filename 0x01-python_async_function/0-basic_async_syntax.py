#!/usr/bin/env python3
"""
asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random
that waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it.
"""

# import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random time between 0 and max_delay
    Return that time that it waited for
    """
    random_wait_time: float = random.uniform(0, max_delay)
    return random_wait_time
