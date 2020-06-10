from Authentication import Authentication
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="todo_db"
)

cursor = db.cursor()

# new = Authentication()
# user_id = new.register_user(cursor, db)
# print(user_id)

# existing = Authentication()
# e_user_id = existing.login_user(cursor)
# print(e_user_id)

# usere = Authentication();
# exists = usere.check_if_username_is_unique("nairobi", cursor)
# print(exists)

# username exists, correct password
# "nairobi", "vrlotajnalozinka"
"""user1 = Authentication()
account_exists = user1.login_user(cursor)
print("Account exists:", account_exists)
print("Expected: True")

#username doesn't exist, password exists
# "denver", "vrlotajnalozinka"
user2 = Authentication()
account_exists = user2.login_user(cursor)
print("Account exists:", account_exists)
print("Expected: correct user id")


#username doesn't exists, password doesn't exists
#"denver", "opala"
user2 = Authentication()
account_exists = user2.login_user(cursor)
print("Account exists:", account_exists)
print("Expected: None")"""

# username exists, wrong password
# "nairobi", "opala"
user2 = Authentication()
account_exists = user2.login_user(cursor)
print("Account exists:", account_exists)
print("Expected: True - but password input needs to be repeated")

cursor.close()
db.close()
