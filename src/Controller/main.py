from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox, QHeaderView
from PyQt6.QtCore import pyqtSlot

from app.Model.Connect_db import ConnectDB
from app.Model.employee import Employee
from app.Model.salary import Salary
from app.Model.department import Department
from app.Model.position import Position
from app.Model.tablemodel import TableModel


class MainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        self.ui = uic.loadUi(r"..\View\main.ui", self)
        self.conn = ConnectDB()
        self.conn.connect()
        self.model = None

        # Lấy input từ giao diện Nhân viên
        self.input_id_employee = self.findChild(QtWidgets.QLineEdit, "input_id_employee")
        self.input_name_employee = self.findChild(QtWidgets.QLineEdit, "input_name_employee")
        self.input_birthday_employee = self.findChild(QtWidgets.QLineEdit, "input_birthday_employee")
        self.input_sex_employee = self.findChild(QtWidgets.QLineEdit, "input_sex_employee")
        self.input_address_employee = self.findChild(QtWidgets.QLineEdit, "input_address_employee")
        self.input_id_salary_employee = self.findChild(QtWidgets.QLineEdit, "input_id_salary_employee")
        self.input_pn_employee = self.findChild(QtWidgets.QLineEdit, "input_pn_employee")
        self.input_id_position_employee = self.findChild(QtWidgets.QLineEdit, "input_id_position_employee")
        self.input_id_department_employee = self.findChild(QtWidgets.QLineEdit, "input_id_department_employee")
        self.table_employee_view = self.findChild(QtWidgets.QTableView, 'table_employee_view')

        self.button_insert_employee = self.findChild(QtWidgets.QPushButton, 'button_insert_employee')
        self.button_insert_employee.clicked.connect(lambda: self.on_button_insert_employee_clicked)

        self.button_delete_employee = self.findChild(QtWidgets.QPushButton, 'button_delete_employee')
        self.button_delete_employee.clicked.connect(lambda: self.on_button_delete_employee_clicked)

        self.button_update_employee = self.findChild(QtWidgets.QPushButton, 'button_update_employee')
        self.button_update_employee.clicked.connect(lambda: self.on_button_update_employee_clicked)

        self.button_find_employee = self.findChild(QtWidgets.QPushButton, 'button_find_employee')
        self.button_find_employee.clicked.connect(lambda: self.on_button_find_employee_clicked)

        # Lấy input từ giao diện phòng ban
        self.input_id_department = self.findChild(QtWidgets.QLineEdit, "input_id_department")
        self.input_name_department = self.findChild(QtWidgets.QLineEdit, "input_name_department")
        self.input_pn_department = self.findChild(QtWidgets.QLineEdit, "input_pn_department")
        self.input_address_department = self.findChild(QtWidgets.QLineEdit, "input_address_department")
        self.table_department_view = self.findChild(QtWidgets.QTableView, 'table_department_view')

        self.button_insert_department = self.findChild(QtWidgets.QPushButton, 'button_insert_department')
        self.button_insert_department.clicked.connect(lambda: self.on_button_insert_department_clicked)

        self.button_update_department = self.findChild(QtWidgets.QPushButton, 'button_update_department')
        self.button_update_department.clicked.connect(lambda: self.on_button_update_department_clicked)

        self.button_delete_department = self.findChild(QtWidgets.QPushButton, 'button_delete_department')
        self.button_delete_department.clicked.connect(lambda: self.on_button_delete_department_clicked)

        self.button_find_department = self.findChild(QtWidgets.QPushButton, 'button_find_department')
        self.button_find_department.clicked.connect(lambda: self.on_button_find_department_clicked)

        # Lấy input từ giao diện Lương
        self.input_id_salary = self.findChild(QtWidgets.QLineEdit, "input_id_salary")
        self.input_basic_salary = self.findChild(QtWidgets.QLineEdit, "input_basic_salary")
        self.input_salary_coefficients = self.findChild(QtWidgets.QSpinBox, "input_salary_coefficients")
        self.input_allowance_coefficient = self.findChild(QtWidgets.QSpinBox, "input_allowance_coefficient")
        self.input_allowance = self.findChild(QtWidgets.QLineEdit, "input_allowance")
        self.input_work_hours = self.findChild(QtWidgets.QLineEdit, "input_work_hours")
        self.input_overtime = self.findChild(QtWidgets.QLineEdit, "input_overtime")
        self.table_salary_view = self.findChild(QtWidgets.QTableView, 'table_salary_view')

        self.button_insert_salary = self.findChild(QtWidgets.QPushButton, 'button_insert_salary')
        self.button_insert_salary.clicked.connect(lambda: self.on_button_insert_salary_clicked)

        self.button_update_salary = self.findChild(QtWidgets.QPushButton, 'button_update_salary')
        self.button_update_salary.clicked.connect(lambda: self.on_button_update_salary_clicked)

        self.button_delete_salary = self.findChild(QtWidgets.QPushButton, 'button_delete_salary')  # Find the button
        self.button_delete_salary.clicked.connect(lambda: self.on_button_delete_salary_clicked)

        self.button_find_salary = self.findChild(QtWidgets.QPushButton, 'button_find_salary')  # Find the button
        self.button_find_salary.clicked.connect(lambda: self.on_button_find_salary_clicked)

        # Lấy input từ giao diện vị trí
        self.input_id_position = self.findChild(QtWidgets.QLineEdit, "input_id_position")
        self.input_name_position = self.findChild(QtWidgets.QLineEdit, "input_name_position")
        self.table_position_view = self.findChild(QtWidgets.QTableView, 'table_position__view')

        self.button_insert_position = self.findChild(QtWidgets.QPushButton, 'button_insert_position')
        self.button_insert_position.clicked.connect(lambda: self.on_button_insert_position_clicked)

        self.button_update_position = self.findChild(QtWidgets.QPushButton, 'button_update_position')
        self.button_update_position.clicked.connect(lambda: self.on_button_update_position_clicked)

        self.button_delete_position = self.findChild(QtWidgets.QPushButton, 'button_delete_position')
        self.button_delete_position.clicked.connect(lambda: self.on_button_delete_position_clicked)

        self.button_find_position = self.findChild(QtWidgets.QPushButton, 'button_find_position')
        self.button_find_position.clicked.connect(lambda: self.on_button_find_position_clicked)

    # Xử lý thông tin các nút ở bảng Nhân viên
    def get_data_input_employee(self):
        input_id_employee = self.input_id_employee.text().strip()
        input_name_employee = self.input_name_employee.text().strip()
        input_birthday_employee = self.input_birthday_employee.text().strip()
        input_sex_employee = self.input_sex_employee.text().strip()
        input_address_employee = self.input_address_employee.text().strip()
        input_pn_employee = self.input_pn_employee.text().strip()
        input_id_position_employee = self.input_id_position_employee.text().strip()
        input_id_department_employee = self.input_id_department_employee.text().strip()
        input_id_salary_employee = self.input_id_salary_employee.text().strip()

        employee = Employee(input_id_employee,
                            input_name_employee,
                            input_birthday_employee,
                            input_sex_employee,
                            input_address_employee,
                            input_pn_employee,
                            input_id_position_employee,
                            input_id_department_employee,
                            input_id_salary_employee)
        return employee

    @pyqtSlot()
    def on_button_insert_employee_clicked(self):
        employee = self.get_data_input_employee()
        create_table_employee = employee.create_table()

        self.conn.execute_query(create_table_employee, fetch=False)

        insert_table_employee = employee.insert_data()
        self.conn.execute_query(insert_table_employee, fetch=False)

        title = "Thông báo!"
        log = "Đã thêm thông tin nhân viên thành công."
        self.show_log(title, log)

    @pyqtSlot()
    def on_button_update_employee_clicked(self):
        employee = self.get_data_input_employee()

        update_employee = employee.update_data()
        self.conn.execute_query(update_employee, fetch=False)

        title = "Thông báo!"
        log = "Đã sửa thông tin thành công."
        self.show_log(title, log)

    @pyqtSlot()
    def on_button_delete_employee_clicked(self):
        employee = self.get_data_input_employee()

        delete_employee = employee.delete_data(employee.id_employee)
        self.conn.execute_query(delete_employee, fetch=False)

        title = "Thông báo!"
        log = "Đã xóa thành công."
        self.show_log(title, log)

    @pyqtSlot()
    def on_button_find_employee_clicked(self):
        employee = self.get_data_input_employee()

        find_employee = employee.find_info(employee.id_employee, employee.name_employee, employee.phone_number)
        table_employee = self.conn.execute_query(find_employee)
        if len(table_employee) > 0:
            self.model = None
            header = ['Mã nhân viên', 'Họ Tên', 'Ngày sinh', 'Giới tính',
                      "Địa chỉ", "Số điện thoại", 'Mã vị trí', 'Mã phòng ban', 'Mã lương']
            self.model = TableModel(table_employee, header)

            # Đặt chế độ thay đổi kích thước cho tất cả các cột thành chế độ kéo giãn
            self.table_employee_view.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

            # Đặt cột cuối cùng thành cột kéo giãn ưu tiên
            self.table_employee_view.horizontalHeader().setStretchLastSection(True)
            self.table_employee_view.setModel(self.model)
        else:
            title = "Thông báo"
            log = "Không tìm thấy"
            self.show_log(title, log)

    # Xử lý thông tin các nút ở bảng Phòng ban
    def get_data_input_department(self):
        input_id_department = self.input_id_department.text().strip()
        input_name_department = self.input_name_department.text().strip()
        input_pn_department = self.input_pn_department.text().strip()
        input_address_department = self.input_address_department.text().strip()
        department = Department(input_id_department,
                                input_name_department,
                                input_pn_department,
                                input_address_department)
        return department

    @pyqtSlot()
    def on_button_insert_department_clicked(self):
        department = self.get_data_input_department()
        create_table_department = department.create_table()
        self.conn.execute_query(create_table_department, fetch=False)

        insert_table_department = department.insert_data()
        self.conn.execute_query(insert_table_department, fetch=False)

        title = "Thông báo!"
        log = "Đã thêm thông tin phòng ban thành công."
        self.show_log(title, log)

    @pyqtSlot()
    def on_button_update_department_clicked(self):
        department = self.get_data_input_department()

        update_department = department.update_data()
        self.conn.execute_query(update_department, fetch=False)

        title = "Thông báo!"
        log = "Đã sửa thông tin thành công."
        self.show_log(title, log)

    @pyqtSlot()
    def on_button_delete_department_clicked(self):
        department = self.get_data_input_department()

        delete_department = department.delete_data(department.id_department)
        self.conn.execute_query(delete_department, fetch=False)

        title = "Thông báo!"
        log = "Đã xóa thành công."
        self.show_log(title, log)

    @pyqtSlot()
    def on_button_find_department_clicked(self):
        department = self.get_data_input_department()

        find_department = department.find_info(department.id_department, department.name_department,
                                               department.phone_number_department)
        table_department = self.conn.execute_query(find_department)
        if len(table_department) > 0:
            self.model = None
            header = ['Mã phòng ban', 'Tên phòng ban', 'Số điện thoại', 'Địa chỉ']
            self.model = TableModel(table_department, header)
            self.table_department_view.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.table_department_view.horizontalHeader().setStretchLastSection(True)
            self.table_department_view.setModel(self.model)
        else:
            title = "Thông báo"
            log = "Không tìm thấy"
            self.show_log(title, log)

    # Xử lý thông tin các nút ở bảng Lương
    def get_data_input_salary(self):
        input_id_salary = self.input_id_salary.text().strip()
        input_basic_salary = self.input_basic_salary.text().strip()
        input_salary_coefficients = self.input_salary_coefficients.text().strip()
        input_allowance_coefficient = self.input_allowance_coefficient.text().strip()
        input_allowance = self.input_allowance.text().strip()
        input_work_hours = self.input_work_hours.text().strip()
        input_overtime = self.input_overtime.text().strip()
        if input_basic_salary == '':
            input_basic_salary = 0
            input_salary_coefficients = 0
            input_allowance_coefficient = 0
            input_allowance = 0
            input_work_hours = 0
            input_overtime = 0

        salary = Salary(input_id_salary,
                        input_basic_salary,
                        input_salary_coefficients,
                        input_allowance_coefficient,
                        input_allowance,
                        input_work_hours,
                        input_overtime)
        return salary

    # Xử lý thông tin từ các nút ở bảng Lương
    @pyqtSlot()
    def on_button_insert_salary_clicked(self):
        salary = self.get_data_input_salary()
        create_table_salary = salary.create_table()

        self.conn.execute_query(create_table_salary, fetch=False)

        insert_table_salary = salary.insert_data()
        self.conn.execute_query(insert_table_salary, fetch=False)

        title = "Thông báo!"
        log = "Đã thêm bảng lương thành công."
        self.show_log(title, log)

    @pyqtSlot()
    def on_button_update_salary_clicked(self):
        salary = self.get_data_input_salary()

        update_salary = salary.update_data()
        self.conn.execute_query(update_salary, fetch=False)

        title = "Thông báo!"
        log = "Đã sửa thành công."
        self.show_log(title, log)

    @pyqtSlot()
    def on_button_delete_salary_clicked(self):
        salary = self.get_data_input_salary()

        delete_salary = salary.delete_data(salary.id_salary)
        self.conn.execute_query(delete_salary, fetch=False)

        title = "Thông báo!"
        log = "Đã xóa thành công."
        self.show_log(title, log)

    @pyqtSlot()
    def on_button_find_salary_clicked(self):
        salary = self.get_data_input_salary()
        find_salary = salary.find_info(salary.id_salary)

        # Thực hiện truy vấn cơ sở dữ liệu
        table_salary = self.conn.execute_query(find_salary)
        if len(table_salary) > 0:
            self.model = None
            header = ['Mã lương', 'Lương cơ bản', 'Hệ số lương', 'Hệ số phụ cấp',
                      'Tiền phụ cấp', 'Giờ làm', 'Tăng ca', 'Tổng lương']
            self.model = TableModel(table_salary, header)
            self.table_salary_view.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.table_salary_view.horizontalHeader().setStretchLastSection(True)
            self.table_salary_view.setModel(self.model)
        else:
            title = "Thông báo"
            log = "Không tìm thấy"
            self.show_log(title, log)

    # Xử lý thông tin các nút ở bảng Vị trí
    def get_data_input_position(self):
        input_id_position = self.input_id_position.text().strip()
        input_name_position = self.input_name_position.text().strip()
        position = Position(input_id_position, input_name_position)
        return position

    @pyqtSlot()
    def on_button_insert_position_clicked(self):
        position = self.get_data_input_position()
        create_table = position.create_table()

        self.conn.execute_query(create_table, fetch=False)

        insert_table_position = position.insert_data()
        self.conn.execute_query(insert_table_position, fetch=False)

        title = "Thông báo!"
        log = "Đã thêm thông tin vị trí thành công!"
        self.show_log(title, log)

    @pyqtSlot()
    def on_button_update_position_clicked(self):
        position = self.get_data_input_position()

        update_position = position.update_data()
        self.conn.execute_query(update_position, fetch=False)

        title = "Thông báo!"
        log = "Đã sửa thành công"
        self.show_log(title, log)

    @pyqtSlot()
    def on_button_delete_position_clicked(self):
        position = self.get_data_input_position()

        delete_position = position.delete_data(position.id_position)
        self.conn.execute_query(delete_position, fetch=False)

        title = "Thông báo!"
        log = "Đã xóa thành công"
        self.show_log(title, log)

    @pyqtSlot()
    def on_button_find_position_clicked(self):
        position = self.get_data_input_position()

        find_position = position.find_info(position.id_position)
        table_position = self.conn.execute_query(find_position)
        if len(table_position) > 0:
            header = ['Mã vị trí', 'Tên vị trí']
            self.model = None
            self.model = TableModel(table_position, header)
            self.table_position_view.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.table_position_view.horizontalHeader().setStretchLastSection(True)
            self.table_position_view.setModel(self.model)
        else:
            title = "Thông báo"
            log = "Không tìm thấy"
            self.show_log(title, log)

    @staticmethod
    def show_log(title, log):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setInformativeText(log)
        msg.setIcon(QMessageBox.Icon.Information)

        # Hiển thị hộp thông báo
        msg.exec()

    def closeEvent(self, event):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Thông báo")
        msg_box.setText("<font color = red >Bạn có muốn thoát ứng dụng? </font >")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        msg_box.setStyleSheet("background-color: rgb(241, 241, 241);")
        ret = msg_box.exec()
        if ret == QtWidgets.QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
