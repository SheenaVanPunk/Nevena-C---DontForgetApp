import mysql.connector
from sqlalchemy import create_engine


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="todo_db"
)

my_cursor = db.cursor();
#
# test_data = my_cursor.execute("SELECT * FROM tasks")
# print(test_data)
create_table_query = "CREATE TABLE Person "
"(personID int PRIMARY KEY AUTO_INCREMENT, "
"name VARCHAR(50)"
")"

delete_table_query = "DROP TABLE Person"
describe_tasks_table = "DESCRIBE tasks"
select_all_users_query = "SELECT * FROM users"
tasks_join_users = "SELECT * FROM tasks JOIN users ON tasks.user_id = users.user_id"
insert_new_user = "INSERT INTO users(username, password) VALUES(%s, %s)"

input_username = input("Enter a unique username: \n")
my_cursor.execute(select_all_users_query)
for rows in my_cursor:
    i = 0
    if(rows[i][2]) == input_username

# while input_username in username:
#     try:
#         my_cursor.execute(insert_new_user, (input_username,"vrlotajnalozinka"))
#         db.commit()
#     except mysql.connector.errors.IntegrityError as err:
#         print("This username exists.")
#         input_username = input("Enter a unique username: \n")
#         my_cursor.execute(insert_new_user, (input_username, "vrlotajnalozinka"))
#         db.commit()


