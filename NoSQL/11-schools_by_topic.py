#!/usr/bin/env python3
"""
This module contains a function to find schools by a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic

    Args:
        mongo_collection: the pymongo collection object
        topic (str): the topic to search for

    Returns:
        list: schools that have the given topic
    """
    return list(mongo_collection.find({"topics": topic}))
