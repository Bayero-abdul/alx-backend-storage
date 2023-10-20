#!/usr/bin/env python3
""" Main file """

import redis
from web import get_page


client = redis.Redis()

url = 'http://slowwly.robertomurray.co.uk'

get_page(url)
print(client.get(f'count:{url}'))


get_page(url)
get_page(url)
print(client.get(f'count:{url}'))
