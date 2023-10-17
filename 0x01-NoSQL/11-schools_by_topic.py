#!/usr/bin/env python3
"""11-schools_by_topic """


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic.
    
    """
    
    try:
        result = mongo_collection.find({'topics': topic})
    except BaseException:
        print('Finding list of schools was unsuccessful.')

    return result

