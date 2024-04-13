from PyQt6 import QtWidgets, uic
import sys
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import pyqtSlot

from app.Model.admin import Admin
from app.Controller.main import MainUI


class LoginUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginUi, self).__init__()
        self.ui = uic.loadUi(r"..\View\login.ui", self)
        self.button_login = self.findChild(QtWidgets.QPushButton, 'button_login')
        self.button_login.clicked.connect(lambda: self.on_button_login_clicked)
        self.input_user = self.findChild(QtWidgets.QLineEdit, 'input_user')
        self.input_password = self.findChild(QtWidgets.QLineEdit, 'input_password')

    @pyqtSlot()
    def on_button_login_clicked(self):
        input_user = self.input_user.text().strip()
        input_password = self.input_password.text().strip()

        admin = Admin(input_user, input_password)
        res_login = admin.check_login()
        if not res_login:
            title = "Đăng nhập không thành công."
            log = "Vui lòng kiểm tra lại tài khoản và mật khẩu."
            self.show_log(title, log)
        else:
            self.hide()
            window_main = MainUI()
            window_main.show()

    @staticmethod
    def show_log(title, log):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(log)
        msg.setIcon(QMessageBox.Icon.Question)

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

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LoginUi()
    window.show()
    app.exec()
