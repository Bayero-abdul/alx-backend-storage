#!/usr/bin/env python3
""" Main file """

import redis
import time
from web import get_page


client = redis.Redis()

url = 'http://slowwly.robertomurray.co.uk'

get_page(url)
print(client.get(f'count:{url}'))
print(client.get(f'cache:{url}'))

time.sleep(10)

print(client.get(f'count:{url}'))
print(client.get(f'cache:{url}'))
