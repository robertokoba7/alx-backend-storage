#!/usr/bin/env python3
"""MongoDB update"""


def update_topics(mongo_collection, name, topics):
    """Update a document based on name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
