from Task import Task
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="todo_db"
)

cursor = db.cursor()

# task = Task()
# task.set_due_date()
# date = task.get_due_date()
# print(date)
#
# task1 = Task()
# task1.create_new_task(db, cursor, 3)
# task1.show_all_tasks_for_user(cursor, 3)

task2 = Task()
task2.set_due_time()
t = task2.get_due_time()

# task3 = Task()
# task3.set_due_date();
# date = task3.get_due_date()
# print(date)


tasks4 = Task()
tasks4.show_upcoming_tasks_for_user(cursor, 3)