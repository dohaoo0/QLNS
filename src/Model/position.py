from app.Model.Base import Base


class Position(Base):
    def __init__(self, id_position, name_position):
        self.id_position = id_position
        self.name_position = name_position

    def create_table(create_table=None):
        # Tạo bảng employees
        create_table_query = """
            CREATE TABLE IF NOT EXISTS position
            (
                MAVT VARCHAR(20) NOT NULL,
                TENVT NVARCHAR(20) NOT NULL,
                PRIMARY KEY(MAVT)
            );
        """
        return create_table_query

    def insert_data(self):
        insert_query = f"INSERT INTO position VALUES ('{self.id_position}', '{self.name_position}');"
        return insert_query

    def update_data(self):
        update_query = f"UPDATE position SET MAVT = '{self.id_position}', TENVT = '{self.name_position}'"
        return update_query

    def delete_data(self, id_position_delete):
        delete_query = f"DELETE FROM position WHERE MAVT = '{id_position_delete}'"
        return delete_query

    def find_info(self, find_id=''):
        where = ';'
        if find_id != '':
            where = f"WHERE MaVT = '{find_id}';"
        show_position_query = f"SELECT * FROM position " + where
        return show_position_query
