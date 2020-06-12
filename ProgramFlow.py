from AuthenticationMenu import UserAuthenticated
from Task import Task
from UserMenu import UserMenu


class ProgramFlow:
    def __init__(self):
        print("start")

    def main(self):
        print("Welcome to DontForget App!\nHere, you can save all the stuff you wouldn't like to forget "
              "and review them later.\n")
        user = UserAuthenticated()
        self.authenticate_user(user)
        self.show_user_menu(user)

    def authenticate_user(self, user):
        print("Start with logging in or signing up, if you are here for the first time.\n")
        flow = input("1) Log in\n2) Sign up\n")
        if flow == '1':
            user.login_user()
            if user.get_user_id() == 0:
                self.authenticate_user(user)
        elif flow == '2':
            user.register_user()
        else:
            print("Invalid entry. Try again.")
            self.authenticate_user(user)

    def show_user_menu(self, user):
        print("* * * * * * * * * * * * * * * * * *")
        print("What would you like to do today?")
        menu = UserMenu()
        user_id = user.get_user_id()
        flow = input("1) See my upcoming tasks\n2) Save a new task\n3) Exit\n")
        if flow == '1':
            user_input = menu.show_upcoming_tasks_for_user(user_id)
            if user_input == 'yes':
                menu.create_new_task(user_id)
                self.show_user_menu(user)
            else:
                self.show_user_menu(user)
        elif flow == '2':
            menu.create_new_task(user_id)
            self.show_user_menu(user)
        elif flow == '3':
            print("\nSad to see you go!")
        else:
            print("Invalid entry.")
            self.show_user_menu(user)

