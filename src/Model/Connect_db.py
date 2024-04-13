import mysql.connector as mc


class ConnectDB:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "123456"
        self.database = "qlns"
        self.connection = None
        self.cursors = None

    def connect(self):
        self.connection = mc.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursors = self.connection.cursor()
        print("Connect database successfully!")

    def execute_query(self, query, fetch=True):
        try:
            self.cursors.execute(query)
            if fetch:
                res = self.cursors.fetchall()
                return res
            self.connection.commit()
            print("Execute query successfully")
        except mc.Error as err:
            print(f"Error query: {err}")

    def disconnect(self):
        # Đóng kết nối
        if self.connection.is_connected():
            self.cursors.close()
            self.connection.close()
            print("Disconnection!")
