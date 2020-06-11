class User:
    def __init__(self):
        self._user_id = 0
        self._username = ""
        self._password = ""

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_user_id(self):
        return self._user_id

    def set_username(self, username):
        self._username = username

    def set_password(self, password):
        self._password = password

    def set_user_id(self, user_id):
        self._user_id = user_id

    def input_username(self):
        self._username = input("Enter username: \n")
        if self._username == "":
            self.input_username()

    def input_password(self):
        self._password = input("Enter password: \n")
        if self._password == "":
            self.input_password()


