import mysql.connector
from sqlalchemy import create_engine
from tabulate import tabulate

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="todo_db"
)

cursor = db.cursor();
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
insert_new_user = "INSERT INTO users(username, password) VALUES({1}, {2})"
query = "SELECT user_id FROM users WHERE username = '{}'"

# input_username = input("Enter a unique username: \n")
# cursor.execute(query.format("nena"))
# user_id = cursor.fetchone()[0]
# print(user_id)
#     i = 0
# if(rows[i][2]) == input_username

# while input_username in username:
#     try:
#         my_cursor.execute(insert_new_user, (input_username,"vrlotajnalozinka"))
#         db.commit()
#     except mysql.connector.errors.IntegrityError as err:
#         print("This username exists.")
#         input_username = input("Enter a unique username: \n")
#         my_cursor.execute(insert_new_user, (input_username, "vrlotajnalozinka"))
#         db.commit()

fetch_all_tasks_for_user_query = "SELECT task_description, task_due, time_created " \
                                 "FROM tasks " \
                                 "JOIN users " \
                                 "ON tasks.user_id = users.user_id " \
                                 "WHERE tasks.user_id = {}"
this = fetch_all_tasks_for_user_query.format("1")
cursor.execute(this)
tasks = cursor.fetchall()
count = 1
for task in tasks:
    print("----------------")
    print("TASK #", count)
    print("task description: ", task[0])
    print("task due: ", task[1])
    print("task created on:", task[2])
    count += 1
