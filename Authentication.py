import User
from User import User


class Authentication:

    def __init__(self):
        self._user_id = ""

    def get_user_id(self):
        return self._user_id

    def register_user(self, db, cursor, unique=False):
        user = User()
        print("Your username must be unique.")
        existing_usernames = self._get_all_usernames_from_db(cursor)
        while not unique:
            user.input_username()
            unique = self._check_if_username_is_unique(user.get_username(), existing_usernames)
        user.input_password()
        self._user_id = self._insert_new_user_to_db(user.get_username(), user.get_password(), cursor, db)

    def login_user(self, cursor):
        user = User()
        user.input_username()
        user.input_password()
        exists = self._check_if_account_exists(cursor, user)
        if exists:
            self._user_id = self._get_user_id_from_db(cursor, user.get_username(), user.get_password())
            print("Nice to see you back, " + user.get_username().title() + "!")
        else:
            print("This account doesn't exist. Please sign up.")

    def _insert_new_user_to_db(self, username, password, cursor, db):
        query = "INSERT INTO users(username, password) " \
                "VALUES(\'{0}\', \'{1}\')"
        full = query.format(username, password)
        cursor.execute(full)
        db.commit()
        print("You account is successfully registered, " + username.title() + "!")
        return self._get_user_id_from_db(cursor, username, password)

    @staticmethod
    def _get_user_id_from_db(cursor, username, password):
        query = "SELECT user_id FROM users WHERE username = '{0}' AND password = '{1}'".format(username, password)
        cursor.execute(query)
        return cursor.fetchone()[0]

    @staticmethod
    def _check_if_username_is_unique(username, usernames_db):
        for existing_username in usernames_db:
            if username.lower() == existing_username.lower():
                print("This username already exist. Pick another one.")
                return False

        print("This username is available :-)")
        return True

    @staticmethod
    def _get_all_usernames_from_db(cursor):
        query = "SELECT username FROM users"
        cursor.execute(query)
        list_of_tuples = cursor.fetchall()
        return ["".join(i) for i in list_of_tuples]

    def _check_if_account_exists(self, cursor, user):
        # looking for a username-password match
        query_username = "SELECT username, password FROM users WHERE username = '{}'"
        query_password = "SELECT username, password FROM users WHERE password = '{}'"

        cursor.execute(query_username.format(user.get_username()))
        results_u = cursor.fetchall()

        cursor.execute(query_password.format(user.get_password()))
        results_p = cursor.fetchall()

        if len(results_u) > 0 and len(results_p) > 0:
            match = [(a, b) for (a, b) in results_u for (c, d) in results_p if (a == c) and (b == d)]
            if len(match) == 1:
                return True
            else:
                return False

        if len(results_u) == 0:
            return False

        if len(results_p) == 0:
            while len(result_p) == 0:
                print("Password incorrect. Try again.")
                user.input_password()
                cursor.execute(query_password.format(user.get_password()))
                result_p = cursor.fetchall()
                if len(results_p) > 0 and result_p[0] == results_u[0]:
                    return True
        return False

    @staticmethod
    def _convert_tuple_list_to_user_object_list(tuples_list):
        objects_list = []
        for i in tuples_list:
            user = User()
            user.set_user_id(i[0])
            user.set_username(i[1])
            user.set_password(i[2])
            objects_list.append(user)
        return objects_list


