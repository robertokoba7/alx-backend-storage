#!/usr/bin/env python3   
"""Print nginx logs"""
from pymongo import MongoClient


if __name__ == "__main__":
    """check collection's elements"""
    client = MongoClient('mongodb://localhost:27017')
    collection = client.logs.nginx


    print(f"{collection.estimate_document_count()}logs")


    print("Methods:")
    for method in ["GET", "POST", "PUT", "DELETE"]:
        method_count = collection.count_documents({'method': method})
        print(f"\tmethod {method}: {method_count}")


        check_get = collection.count_documents(
                {'method': 'GET', 'path': "/status"})
        print(f"{check_get} status check")
