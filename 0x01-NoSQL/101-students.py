#!/usr/bin/env python3
"""101-students.py """


def top_students(mongo_collection):
    """Returns all students sorted by average score.

    """

    pipeline = [
        {
            "$project":
            {
                "_id": "$_id",
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort":
            {
                "averageScore": -1
            }
        }
    ]

    return mongo_collection.aggregate(pipeline)
