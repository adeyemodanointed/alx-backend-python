#!/usr/bin/env python3
"""Async Generator"""
from random import uniform
import asyncio
from typing import List


async def async_generator() -> List[float]:
    """coroutine will loop 10 times, each time asynchronously wait """
    for i in range(10):
        await asyncio.sleep(1)
        yield (uniform(0, 10))
