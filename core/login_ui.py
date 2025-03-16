import logging
import os.path
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QLineEdit, QPushButton, QMessageBox
from core.ui_loader import UiLoader
from core.login import Login
from core.router import Router
from core.authsystem import AuthSystem
from core.user import User


class LoginUI(QDialog):
    """Start screen - login form"""

    def __init__(self):
        super().__init__()
        self.center_window()
        self.login = Login()
        self.auth_system = AuthSystem()
        self.router = Router()
        self.ui = UiLoader.load_ui('ui/login.ui', self)
        self.ui.show()
        # access to elements inside QWidget
        self.username_input = self.findChild(QLineEdit, 'usernameInput')
        self.password_input = self.findChild(QLineEdit, 'passwordInput')
        self.login_button = self.findChild(QPushButton, 'loginButton')
        #self.system_button = self.ui.findChild(QPushButton, 'systemButton')
        # connect signals
        self.login_button.clicked.connect(self.authenticate)
        #self.system_button.clicked.connect(self.system_entry)

    def _get_username(self):
        return self.username_input.text()

    def _get_password(self):
        return self.password_input.text()

    def authenticate(self):
        username = self._get_username()
        password = self._get_password()
        try:
            if self.auth_system.login(username, password):
                logging.info(f'Access granted.')
                role = User.user_role(username)
                logging.info(f'User "{username}" has role "{role}".')
                self.router.navigate_to(role)
                self.close()
                self.accept()
                return role
            else:
                logging.critical(f'Incorrect login or password')
                self.reject()
            logging.info(f'Granted.')
        except Exception as e:
            logging.critical(f'An error occured: {e}')

    def center_window(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

    def system_entry(self):
        self.login.start_terminal()
