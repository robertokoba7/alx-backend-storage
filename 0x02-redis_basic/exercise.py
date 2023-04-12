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
        key = str(uuid4())

        """Using the generated key and set(), we store the data in Redis"""
        self._redis.set(key, data)
        """returns generated key"""
        return key
    
    def get(self,
            key: str,
            fn: Optional[Callable] = None):
        """Extract a saved information from Redis"""
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Parametizes a value from Redis"""
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key:str) -> int:
        """Parametizes a value from redis"""
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
