#!/usr/bin/env python3
"""Stores input in the redis client. """


import redis
import uuid
from typing import Union, Callable


class Cache:
    """Caches data.

    Attributes:
        _redis: store an instance of the Redis client
    """

    def __init__(self):
        """Initializes a cache instance. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument and stores it in redis using
        a random key."""
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """retrieves and converts the data back to the desired format. """
        if key is None:
            return None

        data = self._redis.get(key)
        return fn(data) if fn else data if data else None

    def get_str(self, key: str) -> str:
        """retrieves and converts the data to string. """
        try:
            return str(self._redis.get(key))
        except Exception:
            return None

    def get_int(self, key: str) -> int:
        """retrieves and converts the data to int"""
        try:
            return int(self._redis.get(key))
        except Exception:
            return None
