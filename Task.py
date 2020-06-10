from datetime import datetime

from User import User


class Task:
    def __init__(self):
        self._description = ""
        # self._time_created = ""  # type datetime
        self._task_due = ""  # type date
        self._user_id = ""

    def set_description(self):
        self._description = input("Enter task description:\n")

    def get_description(self):
        return self._description

    def set_task_due(self):
        print("When is the task due?\n")
        year = int(input("Year: "))
        month = int(input("Month: "))
        day = int(input("Day: "))
        self._task_due = datetime(year, month, day).date().strftime('%Y-%m-%d')

    def get_task_due(self):
        return self._task_due

    def set_user_id(self, user_id):
        self._user_id = user_id

    def get_time_created(self, cursor, task_id):
        query = "SELECT time_created FROM tasks WHERE task_id = {}";
        cursor.execute(query.format(task_id))
        time_created = cursor.fetchone()[0]
        return time_created

    def show_all_tasks_for_user(self, cursor, user_id):
        query = "SELECT task_description, task_due, time_created " \
                "FROM tasks " \
                "JOIN users " \
                "ON tasks.user_id = users.user_id " \
                "WHERE tasks.user_id = {}"
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
                print("task description: ", task[0])
                print("task due: ", task[1])
                print("task created on:", task[2])
                count += 1

    def create_new_task(self, db, cursor, user_id):
        query = "INSERT INTO tasks(user_id, task_description, task_due) " \
                "VALUES({0}, '{1}', '{2}')"

        print("To save a new task, you will have to enter task description and time when the task is due.")
        self.set_description()
        self.set_task_due()
        cursor.execute(query.format(user_id, self.get_description(), self.get_task_due()))
        db.commit()
        print("Task successfully saved.\n")