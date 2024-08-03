from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Select the database and collection
db = client['student_db']
collection = db['student']

# Fetch all documents from the collection
documents = collection.find()

# Print each document
for document in documents:
    print(document)

# Close the client
client.close()