

class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password

    def get_username(self):
        return self.username

    def set_username(self):
        self.username = input("Enter username: \n")
        return self.username

    def set_password(self):
        self.password = input("Enter password: \n")
        return self.password

    def register_user(self):
        username = self.set_username()
        password = self.set_password()


        # write new user details in the user table and give it an auto populated id


    def login_user(self):
    # make a connection with table users
