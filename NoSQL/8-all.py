#!/usr/bin/env python3
"""
This module contains a function to list all documents in a collection
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection

    Args:
        mongo_collection: the pymongo collection object

    Returns:
        list: all documents in the collection,
        or an empty list if the collection is empty
    """
    documents = mongo_collection.find()
    return [doc for doc in documents]
