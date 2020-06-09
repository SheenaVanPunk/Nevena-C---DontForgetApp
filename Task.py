import datetime

class Task:
    def __init__(self, description, time_created, user):
        self.description = description
        self.time_created = time_created
        self.user = user

    def set_task(self, description, time_created, user):
        self.description = input("Enter task description");
        self.time_created = setTimeNow()
        #pull user details and populate them under the column


    def set_time_now(self):
        date = datetime.datetime.