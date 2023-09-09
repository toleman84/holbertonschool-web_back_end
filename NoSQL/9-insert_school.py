#!/usr/bin/env python3
"""
    doc
"""


def insert_school(mongo_collection, **kwargs):
    """
        Inserts a new document in the collection based on the kwargs.

        Args:
            mongo_collection: The pymongo collection object.
            **kwargs: The keyword arguments to be used for the document.

        Returns:
            The new _id of the document.
    """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
