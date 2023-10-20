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
        client.incr(f"count:{url}")

        content = client.get(f"cache:{url}")
        if content:
            return content

        content = method(url)
        client.setex(f"cache:{url}", 10, content)

        return content
    return wrapper


@url_access_count
def get_page(url: str) -> str:
    """obtain the HTML content of a particular URL and returns it.
    """

    response = requests.get(url)
    html_content = response.text

    return html_content
