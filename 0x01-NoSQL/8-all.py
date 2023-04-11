#!/usr/bin/env python3
""" pymongo collection object"""

import pymongo


def list_all(mongo_collection):
    """ lists all documents in a collection"""
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
