import mysql.connector

from Authentication import Authentication
from Task import Task


class ProgramFlow:
    _db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="todo_db"
    )
    _cursor = _db.cursor()


    def main(self, _db, _cursor):
        user_id = self.authenticate_user(_db, _cursor)
        self.show_user_menu(_db, _cursor, user_id)

    def authenticate_user(self, db, cursor):
        print("Welcome to DontForget App!\nHere, you can save all your important tasks and review them later.\n")
        print("Start with logging in or signing up, if you are here for the first time.\n")
        auth = Authentication()
        flow = input("1) Log in\n2) Sign up\n")
        if flow == '1':
            user_id = auth.login_user(cursor)
            return user_id
        elif flow == '2':
            user_id = auth.register_user(db, cursor)
            return user_id
        else:
            print("Invalid entry. Try again.")
            # while

    @staticmethod
    def show_user_menu(db, cursor, user_id):
        print("What would you like to do today?")
        task = Task()
        flow = input("1) See my upcoming tasks\n2) Save a new task\n")
        if flow == '1':
            task.show_all_tasks_for_user(cursor, user_id)
        elif flow == '2':
            task.create_new_task(db, cursor, user_id)
        else:
            print("Invalid entry.")
