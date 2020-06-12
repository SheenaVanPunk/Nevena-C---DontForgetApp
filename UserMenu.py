import calendar

from Task import Task
from db.Database import Database


class UserMenu:

    def __init__(self):
        self._task = Task()

    @staticmethod
    def show_upcoming_tasks_for_user(user_id):
        sql = "SELECT task_description, due_date, due_time, time_created " \
              "FROM tasks " \
              "JOIN users " \
              "ON tasks.user_id = users.user_id " \
              "WHERE tasks.user_id = %s AND tasks.due_date > NOW()"
        db = Database()
        tasks = db.fetchall_results(sql, (user_id,))
        db.close()

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
        self._task.set_description()
        self._task.set_due_date()
        self._task.set_due_time()
        db = Database()
        values = (user_id, self._task.get_description(), self._task.get_due_date(), self._task.get_due_time())
        db.commit_to_db(sql, values)
        print("Task successfully saved.\n")

    # prints only the tasks which due_date is in past comparing to the current moment
    def show_historical_tasks_for_user(self, cursor, user_id):
        pass

    # doesn't allow user to save a duplicate of a task with the same descr, due date & time
    def check_if_task_is_a_duplicate(self, cursor, user_id):
        pass

    # saves the timestamp when the task was edited
    def edit_existing_task(self):
        pass

    ## changes the boolean value task_completed from false (0) to true (1)
    # and prints another line "completed" when the task is printed on console
    def complete_a_task(self):
        pass
