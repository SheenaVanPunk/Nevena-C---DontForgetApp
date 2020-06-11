from datetime import datetime
from datetime import time
from datetime import date
import calendar


class Task:
    def __init__(self):
        self._description = ""
        self._due_date = ""  # MySql type DATE
        self._due_time = ""  # MySql type TIME

    def set_description(self):
        self._description = input("What would you like to be reminded of?\n")

    def get_description(self):
        return self._description

    def set_due_date(self):
        print("When is the task due? (format: YYYY MM DD)\n")
        year = int(input("Year: "))
        month = int(input("Month: "))  #accepts 2 different formatting: 06, 6, TODO should accept "June" as 3rd formating
        day = int(input("Day: "))
        self._due_date = date(year, month, day).strftime('%Y-%m-%d')

    def set_due_time(self):
        print("\nTime? (format: HH:MM)")
        h = int(input("Hour: "))
        m = int(input("Minutes: "))
        self._due_time = time(h, m).strftime('%H:%M')

    def get_due_date(self):
        return self._due_date

    def get_due_time(self):
        return self._due_time

    @staticmethod
    def show_upcoming_tasks_for_user(cursor, user_id):
        query = "SELECT task_description, due_date, due_time, time_created " \
                "FROM tasks " \
                "JOIN users " \
                "ON tasks.user_id = users.user_id " \
                "WHERE tasks.user_id = {} AND tasks.due_date > NOW()"
        cursor.execute(query.format(user_id))
        tasks = cursor.fetchall()
        if len(tasks) == 0:
            return input("You don't have any saved tasks yet. Would you like to create one now?\n"
                         "yes\nno\n")
        else:
            count = 1
            for task in tasks:
                print("-----------------------------")
                print("TASK #", count)
                print("task description:", task[0])
                print("due date:", calendar.day_name[task[1].weekday()], task[1])
                print("due_time:", task[2])
                # print("time until:", ... - datetime.now())
                print("task created on:", task[3])
                print(type(task[1]))
                print(type(task[2]))
                count += 1

    def create_new_task(self, db, cursor, user_id):
        query = "INSERT INTO tasks(user_id, task_description, due_date) " \
                "VALUES({0}, '{1}', '{2}')"

        print("To save a new task, you will have to enter task description and time when the task is due.")
        self.set_description()
        self.set_due_date()
        self.set_due_time()
        cursor.execute(query.format(user_id, self.get_description(), self.get_due_date()))
        db.commit()
        print("Task successfully saved.\n")

    # prints only the tasks which due_date is in past comparing to the current moment
    def show_historical_tasks_for_user(self, cursor, user_id):
        pass

