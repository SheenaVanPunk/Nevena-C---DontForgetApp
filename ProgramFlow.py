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
        auth = Authentication()
        self.authenticate_user(_db, _cursor, auth)
        self.show_user_menu(_db, _cursor, auth)

    def authenticate_user(self, db, cursor, auth):
        print("Welcome to DontForget App!\nHere, you can save all your important tasks and review them later.\n")
        print("Start with logging in or signing up, if you are here for the first time.\n")
        flow = input("1) Log in\n2) Sign up\n")
        if flow == '1':
            auth.login_user(cursor)
        elif flow == '2':
            auth.register_user(db, cursor)
        else:
            print("Invalid entry. Try again.")

    def show_user_menu(self, db, cursor, auth):
        print("What would you like to do today?")
        task = Task()
        user_id = auth.get_user_id()
        flow = input("1) See my upcoming tasks\n2) Save a new task\n")
        if flow == '1':
            user_input = task.show_all_tasks_for_user(cursor, user_id)
            if user_input == 'yes':
                task.create_new_task(db, cursor, user_id)
            else:
                print("\nSad to see you go!")
        elif flow == '2':
            task.create_new_task(db, cursor, user_id)
        else:
            print("Invalid entry.")
