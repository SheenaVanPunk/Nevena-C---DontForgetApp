from Authentication import Authentication
import mysql.connector

from Database import Database
from User import User

db = Database()

# new = Authentication()
# new.register_user(db)
# print(new.get_user_id())


l = Authentication()
l.login_user(db)
print(l.get_user_id())
# hey = Authentication()
# user_id = hey._get_user_id_from_db(db, values=('kokica', 'kokica'))
# print(user_id)
# user = User()
# l1 = Authentication()
# result = l1._check_if_account_exists(db, user)
# print(result)
'''
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

user = User()
a = Authentication()
exists = a._check_if_account_exists(cursor, user)
print(exists)
'''