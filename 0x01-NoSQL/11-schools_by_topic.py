#!/usr/bin/env python3
"""Find and  returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Use an aggregate to find documents"""
    return [i for i in mongo_collection.find({"topics": topic})]
