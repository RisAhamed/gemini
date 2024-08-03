from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Create a new database
db = client['student_db']

# Create a new collection (equivalent to a table in SQL)
collection = db['student']

# Insert some sample data
data = [
    {'Name': 'John Doe', 'Class': 'A', 'Section': 'A'},
    {'Name': 'Jane Doe', 'Class': 'B', 'Section': 'B'},
    {'Name': 'Bob Smith', 'Class': 'A', 'Section': 'C'}
]

collection.insert_many(data)

# Close the client
client.close()