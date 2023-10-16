#!/usr/bin/env python3
"""list all documents in a collection.
"""

def list_all(mongo_collection):
    """Return lists of all documents."""
    return mongo_collection.find()
