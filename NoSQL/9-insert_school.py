#!/usr/bin/env python3
"""doc"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """
        Inserts a new document in the collection based on the kwargs.

        Args:
            mongo_collection: The pymongo collection object.
            **kwargs: The keyword arguments to be used for the document.

        Returns:
            The new _id of the document.
    """
    document = {key: value for key, value in kwargs.items()}
    mongo_collection.insert_one(document)

    return document['_id']
