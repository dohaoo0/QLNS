from app.Model.Connect_db import ConnectDB


class Admin:
    def __init__(self, input_user, input_password):
        self.input_username = input_user
        self.input_password = input_password

    @staticmethod
    def create_table_admin():
        create_table_admin_query = """CREATE TABLE IF NOT EXISTS admin 
        (USER VARCHAR(20) NOT NULL,PASSWORD VARCHAR(20) NOT NULL);"""
        return create_table_admin_query

    def check_login(self):
        # try:
        conn = ConnectDB()
        conn.connect()
        query_create_table = self.create_table_admin()
        conn.execute_query(query_create_table)

        data_admin = conn.execute_query("""SELECT * FROM admin;""")

        for data in data_admin:
            if self.input_username == data[0] and self.input_password == data[1]:
                return True
        return False
