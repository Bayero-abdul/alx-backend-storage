#!/usr/bin/env python3
"""101-students.py """


def top_students(mongo_collection):
    """Returns all students sorted by average score.

    """

    pipeline = [
        {"$match": {}},
        {"$group": {"_id": "$_id", "averageScore": {"$sum": "$topics.score"}}}
    ]

    return mongo_collection.aggregate(pipeline)
