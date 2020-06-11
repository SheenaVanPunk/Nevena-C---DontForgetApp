import mysql

from User import User
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="todo_db"
)

cursor = db.cursor()


user = User()
user.input_username()
username = user.get_username()
print("Username taken from the object: ", username)

user.input_password()

