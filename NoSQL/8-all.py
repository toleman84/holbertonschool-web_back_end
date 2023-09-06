#!/usr/bin/env python3
"""doc"""

import pymongo


def list_all(mongo_collection) -> list:
    """
        Lists all documents in a collection.

        Args:
            mongo_collection: The pymongo collection object.

        Returns:
            A list of all documents in the collection.
    """
    list_all_collection: list = []
    for collection in mongo_collection.find():
        list_all_collection.append(collection)

    return list_all_collection
