class Task:
    def __init__(self, description, time_created, user):
        self.description = description
        self.time_create = time_created
        self.user = user

    def setTask(self, description, time_created, user):
        self.description = input("Enter task description");
        self.time_created = Date