#!/usr/bin/env python3
"""doc"""

import pymongo


def schools_by_topic(mongo_collection, topic):
    """
        Returns the list of schools having a specific topic.

        Args:
            mongo_collection: The pymongo collection object.
            topic (string): The topic to be searched.

        Returns:
            A list of school documents.
    """

    query = {'topics': topic}
    schools = mongo_collection.find(query)

    return schools
