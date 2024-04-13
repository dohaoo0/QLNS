from app.Model.Base import Base


class Salary(Base):
    def __init__(self, id_salary=None, basic_salary=0, salary_coefficients=0,
                 allowance_coefficient=0, allowance=0, work_hours=0.0, overtime=0.0):
        self.id_salary = id_salary
        self.basic_salary = float(basic_salary)
        self.salary_coefficients = float(salary_coefficients)
        self.allowance_coefficient = float(allowance_coefficient)
        self.allowance = float(allowance)
        self.work_hours = float(work_hours)
        self.overtime = float(overtime)
        self.total = self.calculate_salary()

    def create_table(create_query=None):
        create_table_query = """
            CREATE TABLE IF NOT EXISTS salary 
            (
                MALUONG VARCHAR(20) NOT NULL UNIQUE,
                LCB FLOAT NOT NULL,
                HSL FLOAT NOT NULL,
                HSPC FLOAT NOT NULL,
                TIENPC FLOAT NOT NULL,
                GIOLAM FLOAT NOT NULL,
                TANGCA FLOAT,
                TONGLUONG FLOAT,
                PRIMARY KEY (MALUONG)
            )
        """
        return create_table_query

    def calculate_salary(self):
        hard_salary = (self.work_hours * 1 + self.overtime * 1.5) * self.basic_salary * self.salary_coefficients
        soft_salary = self.allowance * self.allowance_coefficient
        total = hard_salary + soft_salary
        return float(total)

    def insert_data(self):
        insert_query = f"\
            INSERT INTO salary (MALUONG, LCB, HSL, HSPC, TIENPC, GIOLAM, TANGCA, TONGLUONG)\
            VALUES ('{self.id_salary}', {self.basic_salary}, {self.salary_coefficients},{self.allowance_coefficient},\
                    {self.allowance}, {self.work_hours}, {self.overtime}, {self.total});"
        return insert_query

    def update_data(self):
        self.total = self.caculate_salary()
        update_query = f"UPDATE salary SET\
                        MALUONG = '{self.id_salary}', LCB = '{self.basic_salary}', HSL = '{self.salary_coefficients}',\
                        HSPC = '{self.allowance_coefficient}',TIENPC = '{self.allowance}', GIOLAM = '{self.work_hours}',\
                        TANGCA = '{self.overtime}', TONGLUONG = '{self.total}'\
                        WHERE MALUONG = '{self.id_salary}';"
        return update_query

    def delete_data(self, id_salary_delete):
        delete_query = f"DELETE FROM salary WHERE MALUONG = '{id_salary_delete}';"
        return delete_query

    def find_info(self, find_id=''):
        where = ";"
        if find_id != '':
            where = f" WHERE MALUONG = '{find_id}';"
        find_salary_query = f"SELECT * FROM salary" + where
        return find_salary_query
