#!/usr/bin/env python3
"""
A non-async function that returns an async.io task
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    A non-async function that returns an async.io task
    """
    return asyncio.create_task(wait_random(max_delay))
