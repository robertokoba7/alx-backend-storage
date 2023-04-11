#!/usr/bin/env python3
"""Connect to MongoDB"""


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["logs"]
collection = db["nginx"]

# Get total number of documents in the collection
total_logs = collection.count_documents({})

# Get number of documents with each HTTP method
http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_logs = {}
for method in http_methods:
    method_logs[method] = collection.count_documents({"method": method})

# Get number of documents with method=GET and path=/status
status_logs = collection.count_documents({"method": "GET", "path": "/status"})

# Print the stats
print(f"{total_logs} logs where {total_logs} is the number of documents in this collection")
print("Methods:")
for method in http_methods:
    print(f"\t{method}: {method_logs[method]}")
print(f"GET /status: {status_logs}")
