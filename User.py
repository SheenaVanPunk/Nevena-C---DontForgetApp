
class User:
    def __init__(self, username, password):
        self._user_id = ""
        self._username = username
        self._password = password

    def get_username(self):
        self._username = input("Enter username: \n")
        return self._username

    def get_password(self):
        self._password = input("Enter password: \n")
        return self._password

    def set_username(self, username):
        self._username = username

    def set_password(self, password):
        self._password = password

    def get_user_id(self, cursor):
        query = "SELECT user_id FROM users WHERE username = '{}'".format(self._username)
        cursor.execute(query)
        self._user_id = cursor.fetchone()[0]
