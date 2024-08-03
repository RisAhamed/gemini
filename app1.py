from dotenv import dotenv_values

dotenv_values = dotenv_values('.env')
GOOGLE_API_KEY = dotenv_values['GOOGLE_API_KEY']

import streamlit as st
import os ,sys
import sqlite3
import google.generativeai as gen

gen.configure(api_key=str(GOOGLE_API_KEY))

# Connect to SQLite database

def get_gemini_response(question,prompt):
    model= gen.GenerativeModel("gemini-pro")

    response= model.generate_content([prompt[0],question])
    return response.text


def execute_sql_query(sql, db_name):
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()

        # Execute the SQL query
        cursor.execute(sql)

        # Fetch all rows from the query
        rows = cursor.fetchall()
        connection.commit()
        connection.close()
        # Print the rows
        for row in rows:
            print(row)

        # Return the rows
        return rows

    except sqlite3.Error as error:
        print("Error while executing SQL query:", error)
        return "Error: " + str(error)

    finally:
        # Close the connection to the database
        if connection:
            connection.commit()
            connection.close()


prompt = [
    '''
    I am an SQL expert system. I can convert your English queries into SQL queries and execute them on the database.
    The database contains information about students with attributes: Name, Class, and Section.

    Please enter your English query. If the query is invalid, I will let you know.

    Examples:
    - English: How many students are in the database?
      SQL: SELECT COUNT(*) FROM student;
    - English: What are the names of students in Class AIDS?
      SQL: SELECT Name FROM student WHERE Class = 'AIDS';
    - English: What is the section of student named riswan?
      SQL: SELECT Section FROM student WHERE Name = 'riswan';
    - English: How many students are in Section A?
      SQL: SELECT COUNT(*) FROM student WHERE Section = 'A';
    - English: What are the classes of students named ajmal and rayan?
      SQL: SELECT Class FROM student WHERE Name IN ('ajmal', 'rayan');

    Enter your query:
    '''
]

st.set_page_config(page_title ="Student DB")
st.title("SQL Expert System")
st.header("gemini to sql retriver")
question = st.text_input("input -->>",key = "input")

submit = st.button("Submit")
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    result = execute_sql_query(response, 'student.db')
    
    if isinstance(result, str) and result.startswith("Error: "):
        st.error(result)
    elif result is not None:
        st.subheader("response")
        for row in result:
            st.write(row)
            st.write("\n")
    else:
        st.error("Unknown error occurred")