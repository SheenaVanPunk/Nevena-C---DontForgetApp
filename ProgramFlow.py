from Authentication import Authentication


class ProgramFlow:

    def main(self):
        ProgramFlow.authenticate_user()
        ProgramFlow.show_user_menu()

    def authenticate_user(self):
        print("Welcome to DontForget App!\nHere, you can save all your important tasks and review them later.\n")
        print("Start with logging in or signing up if you are here for the first time.\n")
        flow = input("1) Log in\n2) Sign up")
        if flow == 1:
            user_id = Authentication.login_user()
            print("Nice to see you back, " + username + "!")
        elif flow == 2:
            print("Your username must be unique.")
            user_id = Authentication.register_user()
            print("New user account has been saved.")
        else:
            print("Invalid entry.")

    @staticmethod
    def show_user_menu():
        print("What would you like to do today?")
        flow = input("1) See my upcoming tasks\n2) Save a new task")
        if flow == 1:
            pass
        elif flow == 2:
            pass
        else:
            print("Invalid entry.")
