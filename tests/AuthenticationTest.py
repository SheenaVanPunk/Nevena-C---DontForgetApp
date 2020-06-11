from Authentication import Authentication
import mysql.connector

from User import User

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="todo_db"
)

cursor = db.cursor()
"""
new = Authentication()
user_id = new.register_user(db, cursor)
print(user_id)


# username exists, correct password
# "nairobi", "vrlotajnalozinka"
user1 = Authentication()
account_exists = user1.login_user(cursor)
print("Account exists:", account_exists)
print("Expected: correct user id")

#username doesn't exist, password exists
# "denver", "vrlotajnalozinka"
user2 = Authentication()
account_exists = user2.login_user(cursor)
print("Account exists:", account_exists)
print("Expected: None")


#username doesn't exists, password doesn't exists
#"denver", "opala"
user2 = Authentication()
account_exists = user2.login_user(cursor)
print("Account exists:", account_exists)
print("Expected: None")

# username exists, wrong password
# "nairobi", "opala"
user2 = Authentication()
account_exists = user2.login_user(cursor)
print("Account exists:", account_exists)
print("Expected: correct user id")

cursor.close()
db.close()
"""
user = User()
a = Authentication()
exists = a._check_if_account_exists(cursor, user)
print(exists)