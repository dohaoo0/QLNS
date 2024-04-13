from app.Model.Base import Base


class Department(Base):
    def __init__(self, id_department=None, name_department=None, phone_number_department=None, address_department=None):
        self.id_department = id_department
        self.name_department = name_department
        self.phone_number_department = phone_number_department
        self.address_department = address_department

    def create_table(create_table=None):
        create_table_query = """
            CREATE TABLE IF NOT EXIST department
            (
                MAPB CHAR(10) NOT NULL,
                TENPB NVARCHAR (50) NOT NULL,
                SDTPB CHAR(20) NOT NULL,
                DIACHI NVARCHAR(50) NOT NULL,
                PRIMARY KEY(MAPB)
            );
        """
        return create_table_query

    def insert_data(self):
        insert_query = f"INSERT INTO department VALUES\
                        ('{self.id_department}', '{self.name_department}',\
                        '{self.phone_number_department}', '{self.address_department}');"
        return insert_query

    def update_data(self):
        update_query = f"UPDATE department SET\
                        MAPB = '{self.id_department}', TENPB = '{self.name_department}',\
                        SDT = '{self.phone_number_department}', DIACHI = '{self.address_department}'"
        return update_query

    def delete_data(self, id_department_delete):
        delete_query = f"DELETE FROM department WHERE MAPB = '{id_department_delete}'"
        return delete_query

    def find_info(self, find_id='', find_name='', find_pn=''):
        where = ";"
        if find_id != '' or find_name != '' or find_pn != '':
            if find_id != '':
                where = f"WHERE MAPB = '{find_id}';"
            elif find_name != '':
                where = f"WHERE TENPB LIKE '{find_name}';"
            else:
                where = f"WHERE SDTPB = '{find_pn}';"
        show_department_query = f"SELECT * FROM department " + where
        return show_department_query
