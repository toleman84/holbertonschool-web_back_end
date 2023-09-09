#!/usr/bin/env python3
"""
    doc
"""

import pymongo


if __name__ == "__main__":
    # Connect to the MongoDB database
    client = pymongo.MongoClient()
    db = client['logs']
    collection = db['nginx']

    # Get the number of documents in the collection
    num_logs = collection.count_documents({})

    # Get the number of documents for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    n_docs_per_method = {}
    for method in methods:
        n_docs_per_method[method] = collection\
            .count_documents({'method': method})

    # Get the number of documents with method=GET and path=/status
    num_docs_with_get_and_status = collection\
        .count_documents({'method': 'GET', 'path': '/status'})

    # Print the stats
    print("{} logs".format(num_logs))
    print("Methods:")
    for method, num_docs in n_docs_per_method.items():
        print(f"\tmethod {method}: {num_docs}") #f'\tmethod {method}: {count_method}'
    print(f"{num_docs_with_get_and_status} status check")
