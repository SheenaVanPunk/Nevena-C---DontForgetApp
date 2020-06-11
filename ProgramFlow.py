from Authentication import Authentication
from Database import Database
from Task import Task


class ProgramFlow:

    def main(self):
        db = Database()
        print("Welcome to DontForget App!\nHere, you can save all the stuff you wouldn't like to forget "
              "and review them later.\n")
        user = Authentication()
        self.authenticate_user(db, user)
        self.show_user_menu(db, user)

    def authenticate_user(self, db, user):
        print("Start with logging in or signing up, if you are here for the first time.\n")
        flow = input("1) Log in\n2) Sign up\n")
        if flow == '1':
            user.login_user(db)
            if user.get_user_id() == "":
                self.authenticate_user(db, user)
        elif flow == '2':
            user.register_user(db)
        else:
            print("Invalid entry. Try again.")
            self.authenticate_user(db, user)

    def show_user_menu(self, db, user):
        print("* * * * * * * * * * * * * * * * * *")
        print("What would you like to do today?")
        task = Task()
        user_id = user.get_user_id()
        flow = input("1) See my upcoming tasks\n2) Save a new task\n3) Exit\n")
        if flow == '1':
            user_input = task.show_upcoming_tasks_for_user(db, user_id)
            if user_input == 'yes':
                task.create_new_task(db, user_id)
                self.show_user_menu(db, user)
            else:
                self.show_user_menu(db, user)
        elif flow == '2':
            task.create_new_task(db, user_id)
            self.show_user_menu(db, user)
        elif flow == '3':
            print("\nSad to see you go!")
        else:
            print("Invalid entry.")
            self.show_user_menu(db, user)
