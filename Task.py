from datetime import time
from datetime import date
import calendar

from db.Database import Database


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
        month = int(input("Month: "))  #accepts 2 different formatting: 06, 6, TODO should accept "June" as 3rd format
        day = int(input("Day: "))  # TODO: except ValueError for days, years and months
        self._due_date = date(year, month, day).strftime('%Y-%m-%d')

    def set_due_time(self):
        print("\nTime? (format: HH:MM)")
        h = int(input("Hour: "))
        m = int(input("Minutes: "))
        self._due_time = time(h, m).strftime('%H:%M:%S') # TODO: except ValueError: minute must be in 0..59 for both hours and minutes

    def get_due_date(self):
        return self._due_date

    def get_due_time(self):
        return self._due_time

    @staticmethod
    def show_upcoming_tasks_for_user(user_id):
        sql = "SELECT task_description, due_date, due_time, time_created " \
                "FROM tasks " \
                "JOIN users " \
                "ON tasks.user_id = users.user_id " \
                "WHERE tasks.user_id = %s AND tasks.due_date > NOW()"
        db = Database()
        tasks = db.fetchall_results(sql, (user_id,))

        if len(tasks) == 0:
            return input("You don't have any upcoming tasks. Would you like to create one now?\n"
                         "yes\nno\n")
        else:
            count = 1
            for task in tasks:
                print("------------------------------------")
                print("TASK #", count)
                print("task description:", task[0])
                print("due date:", calendar.day_name[task[1].weekday()], task[1])
                print("due_time:", task[2])
                # print("time until:", ... - datetime.now())   #  TODO feature... coming up in next sprint! :)
                print("task created on:", task[3])
                count += 1

    def create_new_task(self, user_id):
        sql = "INSERT INTO tasks(user_id, task_description, due_date, due_time) " \
                "VALUES(%s, %s, %s, %s)"

        print("To save a new task, you will have to enter its description and date and time when the task is due.")
        self.set_description()
        self.set_due_date()
        self.set_due_time()
        db = Database()
        values = (user_id, self.get_description(), self.get_due_date(), self.get_due_time())
        db.commit_to_db(sql, values)
        print("Task successfully saved.\n")

    # prints only the tasks which due_date is in past comparing to the current moment
    def show_historical_tasks_for_user(self, cursor, user_id):
        pass

    # doesn't allow user to save a duplicate of a task with the same descr, due date & time
    def check_if_task_is_a_duplicate(self, cursor, user_id):
        pass
