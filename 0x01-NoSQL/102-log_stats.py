#!/usr/bin/env python3
"""102-log_stats.py """


from pymongo import MongoClient


def main():
    """provides some stats about Nginx logs
    stored in MongoDB."""

    db = MongoClient('mongodb://127.0.0.1:27017')

    nginx_collection = db.logs.nginx

    n_logs = nginx_collection.count_documents({})
    print(f'{n_logs} logs')

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print('Methods:')
    for method in methods:
        count = nginx_collection.count_documents({'method': method})
        print(f'\tmethod {method}: {count}')

    status_check = nginx_collection.count_documents(
        {'method': 'GET', 'path': '/status'})
    print(f'{status_check} status check')

    pipeline = [
        {'$group': {'_id': '$ip', 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}},
        {'$limit': 10},
        {'$project': {'_id': 0, 'ip': '$_id', 'count': 1}}
    ]

    tops = nginx_collection.aggregate(pipeline)
    print('IPs:')
    for top in tops:
        ip = top.get('ip')
        count = top.get('count')
        print(f'\t{ip}: {count}')


if __name__ == "__main__":
    main()
