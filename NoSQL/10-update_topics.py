#!/usr/bin/env python3
"""
    doc
"""

import pymongo


def update_topics(mongo_collection, name, topics):
    """
        Updates the topics of a school document based on the name.

        Args:
            mongo_collection: The pymongo collection object.
            name (string): The school name to update.
            topics (list of strings): The list of topics to be updated.
        Returns:
            None.
    """
    query = {"name": name}
    update_data = {"$set": {"topics": topics}}

    mongo_collection.update_many(query, update_data)
