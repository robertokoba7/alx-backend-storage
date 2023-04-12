#!/usr/bin/env python3
"""write strings to Redis"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """counts the number of times a function is called"""
    key = method.__qualname__
    
    @wraps(method)
    def wrapped(self, *args, **kwargs):
        """Additonal function behaviour to count_call"""
        self._redis.incr(key)
        return method(self, * args, **kwargs)
    return wrapped

    
def call_history(method: Callable) -> Callable:
    """inputs and outputs storage"""
    @wraps(method)
    def wrapped(self, *args, **kwargs):
        """Additonal function behaviour to count_call"""
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", inputs)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output
    return wrapped


def replay(fn: Callable):
    """call history"""
    r = redis.Redis()
    function_name = fn.__qualname__
    count = r.get(function_name)
    try:
        count = int(count.decode("utf-8"))
    except Exception:
        count = 0
    print(f'{functio_name} was called {count} times:')
    inputs = r.lrange(f"{function_name}:inputs", 0,-1)
    outputs = r.lrange(f"{function_name}:outputs", 0, -1)
    for one, two in zip(inputs, outputs):
        try:
            one = one.decode('utf-8')
        except Exception:
            one = ""
        try:
            two = two.decode('utf-8')
        except Exception:
            two = ""
        print(f"{function_name}(*{one}) -> {two}")


class Cache:
    """Use of redis to cache frequently accesses data"""
    def __init__(self):
        """Create an instance of Redis client and store it in a privatevariablenamed _redis"""
        self._redis = redis.Redis()
        """Flush Redis instance using flushdb() method"""
        self._redis.flushdb()
    
    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """use uuid.uuid4() to generate a random key"""
        key = str(uuid4())

        """Using the generated key and set(), we store the data in Redis"""
        self._redis.set(key, data)
        """returns generated key"""
        return key
    
    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
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

