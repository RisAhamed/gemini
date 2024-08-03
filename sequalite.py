import sqlite3

connection = sqlite3.connect("student.db")
cursor = connection.cursor()
table_info = """
create table if not exists student (Name varchar(255), class varchar(255),
section varchar(255));
"""
cursor.execute(table_info)

insert = """insert into student (Name, class, section) values ('riswan', 'AIDS', 'B');"""
insert1 = """insert into student (Name, class, section) values ('aslam', 'AIDS', 'A');"""
insert2 = """insert into student (Name, class, section) values ('ajmal', 'ECE', 'A');"""
insert3 = """insert into student (Name, class, section) values ('rayan', 'ECE', 'B');"""


cursor.execute(insert)
cursor.execute(insert1)
cursor.execute(insert2)
cursor.execute(insert3)

print("inserted")

data = cursor.execute("SELECT * FROM student")

for row in data:
    print(row)

connection.close()