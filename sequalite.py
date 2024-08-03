import sqlite3

connection = sqlite3.connect("test.db")
cursor = connection.cursor()
table_info = """
create table if not exists test(Name varchar(255), class varchar(255),
section varchar(255));
"""
cursor.execute(table_info)

insert = """insert into test(Name, class, section) values ('riswan', 'AIDS', 'B');"""
insert1 = """insert into test  (Name, class, section) values ('aslam', 'AIDS', 'A');"""
insert2 = """insert into  test (Name,class, section) values ('ajmal', 'ECE', 'A');"""
insert3 = """insert into test  (Name, class, section) values ('rayan', 'ECE', 'B');"""


cursor.execute(insert)
cursor.execute(insert1)
cursor.execute(insert2)
cursor.execute(insert3)

print("inserted")

data = cursor.execute("SELECT * FROM test")

for row in data:
    print(row)

connection.close()