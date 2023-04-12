#!/usr/bin/env python3
"""write strings to Redis"""


import redis
from uuid import uuid4
from typing import Union, Callable,Optional
functool import wraps


class Cache:
    def __init__(self):
    """Create an instance of Redis client and store it in a privatevariablenamed _redis"""
    self._redis = redis.Redis()
    
    """Flush Redis instance using flushdb() method"""
    self._redis.flushdb()

    def store(self, data: Union[str, bytes, float]) -> str:
        """use uuid.uuid4() to generate a random key"""
        key = str(uuid.uuid4())

        """Using the generated key and set(), we store the data in Redis"""
        self.-redis.set(key, data)
        return key
