#!/usr/bin/env python3
""" web.py module """


import requests
import redis
from typing import Callable
from functools import wraps


def url_access_count(method: Callable) -> Callable:
    """Tracks how many times a particular URL was accessed and
    cache the result with an expiration time. """
    @wraps(method)
    def wrapper(url):
        client = redis.Redis()
        key = f"count:{url}"

        client.incr(key)
        count = client.get(key)
        client.setex(key, 10, count.decode())

        return method(url)
    return wrapper


@url_access_count
def get_page(url: str) -> str:
    """obtain the HTML content of a particular URL and returns it.
    """

    response = requests.get(url)
    html_content = response.text

    return html_content
