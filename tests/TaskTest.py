from db.Database import Database
from Task import Task

db = Database()

# task = Task()
# task.set_due_date()
# date = task.get_due_date()
# print(date)
#
task1 = Task()
task1.create_new_task(db, 3)
task1.show_upcoming_tasks_for_user(db, 3)

# task2 = Task()
# task2.set_due_time()
# t = task2.get_due_time()

# task3 = Task()
# task3.set_due_date();
# date = task3.get_due_date()
# print(date)
"""
t = Task()
t.create_new_task(db, 1)

tasks4 = Task()
tasks4.show_upcoming_tasks_for_user(db, 1)"""