#!/usr/bin/env python3
"""
a Module  that loops 10 times.
"""
from typing import Generator
import random
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """
    async generator that waits 1 second and yields a random number between 0-10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
