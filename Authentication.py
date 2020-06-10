import User
from User import User


class Authentication:

    def register_user(self, cursor, db, unique=False):
        user = User()
        print("Your username must be unique.")
        while not unique:
            user.set_username()
            unique = self.check_if_username_is_unique(user.get_username(), cursor)
        user.set_password()
        user_id = self._insert_new_user_to_db(user.get_username(), user.get_password(), cursor, db)
        return user_id

        # write new user details in the user table and give it an auto populated id

    def _insert_new_user_to_db(self, username, password, cursor, db):
        query = "INSERT INTO users(username, password) " \
                "VALUES(\'{0}\', \'{1}\')"
        full = query.format(username, password)
        cursor.execute(full)
        db.commit()
        print("You account is successfully registered, " + username + "!")
        return self._get_user_id_from_db(cursor, username, password)

    def _get_user_id_from_db(self, cursor, username, password):
        query = "SELECT user_id FROM users WHERE username = '{0}' AND password = '{1}'".format(username, password)
        cursor.execute(query)
        return cursor.fetchone()[0]

    def login_user(self, cursor):
        user = User()
        user.set_username()
        user.set_password()
        exists = self._check_if_account_exists(cursor, user, user.get_username(), user.get_password())
        if exists:
            user_id = self._get_user_id_from_db(cursor, user.get_username(), user.get_password())
            print("Nice to see you back, " + user.get_username().title() + "!")
            return user_id
        else:
            print("This account doesn't exist. Please register account.")

    def check_if_username_is_unique(self, username, cursor):
        query = "SELECT * FROM users WHERE username = '{}'".format(username)
        cursor.execute(query)
        result = cursor.fetchone()
        if result is None:
            return True
        elif result[1] == username:
            print("This username exist. Pick another one.")
            return False

    def _check_if_account_exists(self, cursor, user, username, password):
        query_username = "SELECT * FROM users WHERE username = '{}'"
        query_password = "SELECT * FROM users WHERE password = '{}'"

        cursor.execute(query_username.format(username))
        result_u = cursor.fetchall()

        cursor.execute(query_password.format(password))
        result_p = cursor.fetchall()

        if len(result_u) > 0 and len(result_p) > 0:
            if result_u[0] == result_p[0]:
                return True
            else:
                return False

        if len(result_u) == 0:
            return False

        if len(result_p) == 0:
            while len(result_p) == 0:
                print("Password incorrect. Enter your password again.")
                user.set_password()
                cursor.execute(query_password.format(user.get_password()))
                result_p = cursor.fetchall()
                if len(result_p) > 0 and result_p[0] == result_u[0]:
                    return True

        return False

