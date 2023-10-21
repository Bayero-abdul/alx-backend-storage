# 0x02. Redis basic

# Project Name
0x02. Redis Basic

## Project Overview
This project is part of the ALX curriculum, focusing on Redis and its basic operations. You will learn how to use Redis for caching and storage while implementing various functionalities, including writing and reading data from Redis, counting method calls, storing lists, retrieving method histories, and implementing an expiring web cache and tracker.

## Running the Tasks

### installation
Install Redis on Ubuntu 18.04
```
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```
### test
```python3 main.py ```

## Project Structure
The project directory structure is organized as follows:

- `exercise.py`: Contains the implementation of the `Cache` class, method decorators, and related functions for tasks 1 to 4.
- `web.py` (Advanced): A separate file for task 5, implementing an expiring web cache and tracker.
- `main.py`: Main file to run and test the tasks with example scenarios.
