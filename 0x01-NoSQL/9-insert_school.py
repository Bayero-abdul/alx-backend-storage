#!/usr/bin/env python3
""" 9-insert_school.py """


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection 
    based on kwargs.
    
    returns: new _id 
    """

    try:
        id = mongo_collection.insert(kwargs)
    except:
        print('new document was not inserted')

    return id.inserted_id

