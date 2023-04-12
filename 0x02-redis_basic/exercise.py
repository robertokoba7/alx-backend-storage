#!/usr/bin/env python3
"""write strings to Redis"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


class Cache:
        """Use of redis to cache frequently accesses data"""
    def __init__(self):
        """Create an instance of Redis client and store it in a privatevariablenamed _redis"""
        self._redis = redis.Redis()
        """Flush Redis instance using flushdb() method"""
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """use uuid.uuid4() to generate a random key"""
        key = str(uuid.uuid4())

        """Using the generated key and set(), we store the data in Redis"""
        self._redis.set(key, data)
        """returns generated key"""
        return key
