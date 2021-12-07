#!/usr/bin/env python3
"""
Use an asynchronous generator in an asynchronous list comprehension
inside a coroutine
"""
from typing import List
import asyncio
import random

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Create an asynchronous list comprehension and return the list"""
    result = [i async for i in async_generator()]
    return result
