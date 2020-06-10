import mysql.connector

from ProgramFlow import ProgramFlow

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="todo_db"
)

cursor = db.cursor()


program1 = ProgramFlow()
user_id = program1.main(db, cursor)

