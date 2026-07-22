#!/usr/bin/env python3
"""
This module contains a function to update the topics
of a school document based on its name
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name

    Args:
        mongo_collection: the pymongo collection object
        name (str): the school name to update
        topics (list): the list of topics approached in the school
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
