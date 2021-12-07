#!/usr/bin/env python3
"""
Run multiple async comprehensions and measure the time it takes
to run them
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Return the time it takes to run 4 asynchronous list comprehensions"""
    start = time.perf_counter()
    res = await asyncio.gather(*(async_comprehension() for n in range(4)))
    end = time.perf_counter()
    return (end - start)
