# from dotenv import dotenv_values
# import os
# dotenv_values = dotenv_values('.env')
# GOOGLE_API_KEY = dotenv_values['GOOGLE_API_KEY']

# print(GOOGLE_API_KEY)
# print(dotenv_values)

import sqlite3
from pathlib import Path

# Define the path to the SQLite database
path = Path("C:\\Users\\riswa\\Desktop\\AI\\gemini\\test.db")

# Connect to the SQLite database
connection = sqlite3.connect(path)

# Create a cursor object
cursor = connection.cursor()

# SQL query to retrieve student names
query = "SELECT Name FROM test"  # Corrected table name

try:
    # Execute the SQL query
    cursor.execute(query)

    # Fetch all rows from the query
    rows = cursor.fetchall()
    print(rows)
    cursor.close()
    # Print the student names
    for row in rows:
        print(row[0])  # Access the first column (Name)

except sqlite3.Error as error:
    print("Error while executing SQL query:", error)

finally:
    # Close the connection to the database
    if connection:
        connection.close()  # No need to commit if you're only reading data