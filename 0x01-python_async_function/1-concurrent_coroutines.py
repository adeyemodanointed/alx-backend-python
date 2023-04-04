#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
from typing import List, Callable
import asyncio
wait_random: Callable = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    res: List = await asyncio.gather(
                      *(wait_random(max_delay) for _ in range(n)))
    return sorted(res)
