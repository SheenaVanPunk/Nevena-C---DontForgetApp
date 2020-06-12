import User
from db.Database import Database
from User import User


class UserAuthenticated:

    def __init__(self):
        self._user_id = 0

    def get_user_id(self):
        return self._user_id

    def register_user(self, unique=False):
        user = User()
        print("Your username must be unique.")
        existing_usernames = self._get_all_usernames_from_db()
        while not unique:
            user.input_username()
            unique = self._check_if_username_is_unique(user.get_username(), existing_usernames)
        user.input_password()
        self._user_id = self._insert_new_user_to_db(user)

    def login_user(self):
        user = User()
        user.input_username()
        user.input_password()
        values = (user.get_username(), user.get_password())

        exists = self._check_if_account_exists(user)
        if exists:
            self._user_id = self._get_user_id_from_db(user)
            print("Nice to see you back, " + values[0].title() + "!")
        else:
            print("This account doesn't exist. Please sign up.")

    def _insert_new_user_to_db(self, user):
        sql = "INSERT INTO users(username, password) VALUES(%s, %s)"
        values = (user.get_username(), user.get_password())

        db = Database()
        db.commit_to_db(sql, values)
        print("You account is successfully registered, " + user.get_username().title() + "!")
        return self._get_user_id_from_db(user)

    @staticmethod
    def _get_user_id_from_db(user):
        sql = "SELECT user_id FROM users WHERE username = %s AND password = %s"
        values = (user.get_username(), user.get_password())
        db = Database()
        results = db.fetchone_result(sql, values)
        return results[0]

    @staticmethod
    def _check_if_username_is_unique(username, usernames_db):
        for existing_username in usernames_db:
            if username.lower() == existing_username.lower():
                print("This username already exist. Pick another one.")
                return False

        print("This username is available :-)")
        return True

    @staticmethod
    def _get_all_usernames_from_db():
        sql = "SELECT username FROM users"
        db = Database()
        list_of_tuples = db.query_db(sql, )
        return ["".join(i) for i in list_of_tuples]

    def _check_if_account_exists(self, user):
        # searching for a username-password match
        sql_username = "SELECT username, password FROM users WHERE username = %s"
        sql_password = "SELECT username, password FROM users WHERE password = %s"
        values = (user.get_username(), user.get_password())

        db = Database()
        results_u = db.fetchall_results(sql_username, (values[0],))
        results_p = db.fetchall_results(sql_password, (values[1],))
        db.close()
        # bug: ignoring the letter case with this list comprehension
        match = [(a, b) for (a, b) in results_u for (c, d) in results_p if (a == c) and (b == d)]

        if len(results_u) == 0:  # username doesn't exists
            return False
        elif len(match) == 1:  # username - password match
            return True
        elif len(match) == 0:  # username-password mis-match: password either doesn't exist in db
            while len(match) == 0:  # or it doesn't match the entered username
                print("Password incorrect. Try again.")
                user.input_password()
                pw_value = user.get_password()
                db = Database()
                results_p = db.fetchall_results(sql_password, (pw_value,))
                match = [(a, b) for (a, b) in results_u for (c, d) in results_p if (a == c) and (b == d)]
                if len(match) == 1:
                    return True

