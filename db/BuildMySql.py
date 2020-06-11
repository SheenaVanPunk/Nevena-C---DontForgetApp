from db.Database import Database
## addition to the project - my database&tables were created manually in MySql workbench
# in next sprint, this class will be tested without previous setup and
# it will be integrated with the rest of the app TODO

class BuildMySql:
    def __init__(self):
        self._dbconn = Database()

    def create_database(self, name):
        sql = "CREATE DATABASE %s"
        self._dbconn.commit_to_db(sql, (name,))
        self._dbconn.close()

    def create_table_users(self):
        sql = """CREATE TABLE users(
                user_id INT PRIMARY KEY AUTO_INCREMENT,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(50) NOT NULL
                )"""
        self._dbconn.commit_to_db(sql)
        self._dbconn.close()

    def drop_table(self, name):
        sql = "DROP TABLE %s"
        self._dbconn.commit_to_db(sql, (name,))
        self._dbconn.close()

    def truncate_table(self, name):
        sql = "TRUNCATE TABLE %s"
        self._dbconn.commit_to_db(sql, (name,))
        self._dbconn.close()