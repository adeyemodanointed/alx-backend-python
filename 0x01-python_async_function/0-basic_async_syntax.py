#!/usr/bin/env python3
"""The basics of async"""
from random import uniform
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Function generates random float wait time and returns it"""
    sleep_time = uniform(0, max_delay)
    await asyncio.sleep(sleep_time)
    return sleep_time
