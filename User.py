
class User:
    def __init__(self):
        self._user_id = 0
        self._username = ""
        self._password = ""

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def set_username(self):
        self._username = input("Enter username: \n")
        if self._username =="":
            self.set_username()

    def set_password(self):
        self._password = input("Enter password: \n")
        if self._password == "":
            self.set_password()


