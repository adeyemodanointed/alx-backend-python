#!/usr/bin/env python3
"""Async Generator"""
from random import uniform
import asyncio


async def async_generator():
    """coroutine will loop 10 times, each time asynchronously wait
    1 second, then yield a random number between 0 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield (uniform(0, 10))
