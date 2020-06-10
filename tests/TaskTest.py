from Task import Task
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="todo_db"
)

cursor = db.cursor()

task = Task()
task.set_task_due()
date = task.get_task_due()
print(date)

task1 = Task()
task1.create_new_task(db, cursor, 3)
task1.show_all_tasks_for_user(cursor, 3)
