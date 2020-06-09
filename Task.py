from datetime import datetime

from User import User


class Task:
    def __init__(self, description, task_due):
        self._description = description
        self._time_created = ""  # type datetime
        self._task_due = task_due  # type date
        self._user_id = ""

    def set_description(self, description):
        self._description = description

    def set_time_created(self):
        self._time_created = datetime.now()

    def get_task_due(self):
        self._task_due = input("When is the task due?\n")
        return self._task_due

    def set_task_due(self, task_due):
        self._task_due = task_due

    @staticmethod
    def show_all_tasks_for_user(cursor, user_id):
        query = "SELECT task_description, task_due, time_created " \
                "FROM tasks " \
                "JOIN users " \
                "ON tasks.user_id = users.user_id " \
                "WHERE tasks.user_id = {}"
        cursor.execute(query.format(user_id))
        tasks = cursor.fetchall()
        count = 1
        for task in tasks:
            print("-----------------------------")
            print("TASK #", count)
            print("task description: ", task[0])
            print("task due: ", task[1])
            print("task created on:", task[2])
            count += 1

    # def set_task(self, user_id):
    #     self.description = input("Enter task description");
    #     self.time_created = setTimeNow()
    # pull user details and populate them under the column
