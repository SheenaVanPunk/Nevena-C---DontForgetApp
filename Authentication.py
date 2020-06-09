import User
from db_connection.DBConnection import cursor


class Authentication:
    def __init__(self):
        self._user = User()

    def register_user(self):
        username = self._user.set_username()
        password = self._user.set_password()
        return User.get_user_id(cursor)

        # write new user details in the user table and give it an auto populated id

    def login_user(self):
    # make a connection with table users
        return User.get_user_id()
