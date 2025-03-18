import logging

from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox

from core.authsystem import AuthSystem
from core.router import Router
from core.system_entry import SystemEntry
from core.user import User
from ui.login_ui import Ui_Dialog


class LoginUI(QDialog, Ui_Dialog):
    """Start screen - login form(use compiled UI)"""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._center_window()
        self.system_entry = SystemEntry()
        self.auth_system = AuthSystem()
        self.router = Router()
        self.authenticated = False
        # connect signals
        self.loginButton.clicked.connect(self.authenticate)
        #self.system_button.clicked.connect(self.system_entry)

    def closeEvent(self, event: QCloseEvent):
        logging.info('Login window closed.')
        if not self.authenticated:
            self.reject()
        super().closeEvent(event)

    def _get_username(self):
        return self.usernameInput.text()

    def _get_password(self):
        return self.passwordInput.text()

    def authenticate(self):
        username = self._get_username()
        password = self._get_password()
        if not username or not password:
            QMessageBox.warning(self, 'Warning', 'Please enter username and password.')
            return
        try:
            if self.auth_system.login(username, password):
                self.authenticated = True
                logging.info(f'Access granted.')
                role = User.user_role(username)
                if not role:
                    logging.critical(f'User "{username}" does not have a role.')
                    QMessageBox.critical(self, 'Error', 'User does not have a role.')
                    self.reject()
                    return
                logging.info(f'User "{username}" has role "{role}".')
                self.accept()
                return role
            else:
                self.authenticated = False
                logging.warning(f'Incorrect login or password')
                QMessageBox.warning(self, 'Warning', 'Incorrect login or password.')
                self.passwordInput.clear()
            logging.info(f'Granted.')
        except Exception as e:
            logging.critical(f'An error occured: {e}')
            QMessageBox.critical(self, 'Error', f'An error occured: {e}')

    def _center_window(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

    def system_entry(self):
        self.system_entry.start_terminal()
