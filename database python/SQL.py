import sqlite3

connection = sqlite3.connect("stud.db")
crsr = connection.cursor()

crsr.execute("""CREATE TABLE student (
                studID INTEGER PRIMARY KEY,
                fname VARCHAR (50),
                lname VARCHAR (50),
                gender VARCHAR (6)
)""")

connection.commit()
connection.close()
