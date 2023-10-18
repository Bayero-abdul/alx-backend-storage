#!/usr/bin/env python3
"""Stores input in the redis client. """


import redis
import uuid
from typing import Union


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
        key = uuid.uuid1()
        self._redis.set(str(key), data)
        return str(key)
