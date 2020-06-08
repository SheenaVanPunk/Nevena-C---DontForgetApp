class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id;
        self.username = username
        self.password = password

    def set_username(self):
        self.username = input("Enter username:\n")
        return self.username

    def set_password(self):
        self.password = input("Enter password: \n")
        return self.password