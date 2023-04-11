#!/usr/bin/env python3
"""Insertion of Document"""


def insert_school(mongo_collection, **kwargs):
    """function that inserts a new document in a collection based on kwargs"""
    if len(kwags) == 0:
        return None
    return mongo_collection.insert(kwargs)
