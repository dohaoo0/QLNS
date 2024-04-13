from app.Model.Base import Base
import datetime


class Employee(Base):
    def __init__(self, id_employee=None, name_employee=None, birthday=None, address=None, sex=None,
                 phone_number=None, id_position=None, id_department=None, id_salary=None):
        self.id_employee = id_employee
        self.name_employee = name_employee
        self.birthday = birthday
        self.sex = sex
        self.address = address
        self.phone_number = phone_number
        self.id_position = id_position
        self.id_department = id_department
        self.id_salary = id_salary

    def create_table(create_query=None):
        # Tạo bảng employees
        create_table_query = """
            CREATE TABLE IF NOT EXISTS employees 
            (
                MANV VARCHAR(10) NOT NULL,
                HOTEN NVARCHAR (50) NOT NULL ,
                NGAYSINH DATE NOT NULL ,
                GIOITINH NVARCHAR(5) NOT NULL,
                DIACHI NVARCHAR(50) NOT NULL,
                SDT CHAR(20) NOT NULL,
                MAVT VARCHAR(20) NOT NULL,
                MAPB CHAR(10) NOT NULL,
                MALUONG VARCHAR(10) NOT NULL,
                PRIMARY KEY(MANV)
            );
        """
        return create_table_query

    def insert_data(self):
        insert_query = f"\
            INSERT INTO employees (MANV, HOTEN,NGAYSINH, GIOITINH, DIACHI, SDT,MAVT, MAPB,MALUONG)\
            VALUES ('{self.id_employee}', '{self.name_employee}', '{self.birthday}','{self.sex}','{self.address}',\
                    '{self.phone_number}', '{self.id_position}','{self.id_department}',{self.id_salary});"
        return insert_query

    def delete_data(self, id_employee_delete):
        delete_query = f"DELETE FROM employees WHERE MANV = '{id_employee_delete}';"
        return delete_query

    def update_data(self):
        update_query = f"UPDATE employees SET\
                        MANV = '{self.id_employee}', HOTEN = '{self.name_employee}', NGAYSINH = '{self.birthday}',\
                        GIOITINH = '{self.sex}', DIACHI = '{self.address}', SDT = '{self.phone_number}',\
                        MAVT = '{self.id_position}', MAPB = '{self.id_department}', MALUONG = '{self.id_salary}';"
        return update_query

    def find_info(self, find_id='', find_name='', find_pn=''):
        where = ";"
        if find_id != '' or find_name != '' or find_pn != '':
            if find_id != '':
                where = f"WHERE MANV = '{find_id}';"
            elif find_name != '':
                where = f"WHERE HOTEN LIKE '{find_name}';"
            elif find_pn != '':
                where = f"WHERE SDT = '{find_pn}';"
        find_query = f"SELECT * FROM employees " + where
        return find_query
