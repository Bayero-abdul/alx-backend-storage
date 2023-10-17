#!/usr/bin/env python3
"""12-log_stats.py """


from pymongo import MongoClient


def main():
    """provides some stats about Nginx logs
    stored in MongoDB."""

    db = MongoClient('mongodb://127.0.0.1:27017')

    logs = db.logs.nginx

    print(f"{logs.count_documents({})} logs")

    methods = {'GET': 0, 'POST': 0, 'PUT': 0, 'PATCH': 0, 'DELETE': 0}
    status_check = 0

    for doc in logs.find():
        method = doc.get('method')
        methods[method] = methods.get(method, 0) + 1
        if method == 'GET' and doc.get('path') == '/status':
            status_check += 1

    print('Methods:')
    for method in methods:
        if method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
            print(f'    method {method}: {methods.get(method)}')

    print(f'{status_check} status check')


if __name__ == "__main__":
    main()
