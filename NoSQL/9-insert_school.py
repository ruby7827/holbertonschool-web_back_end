#!/usr/bin/env python3
"""
This module contains a function to insert a document
into a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs

    Args:
        mongo_collection: the pymongo collection object
        **kwargs: the fields and values for the new document

    Returns:
        the new document's _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
