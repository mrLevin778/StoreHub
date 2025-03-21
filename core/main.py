import sys
from PySide6.QtWidgets import QApplication, QDialog
from sqlalchemy.orm import Session
from core.router import Router
from core.login_ui import LoginUI
from core.ext_db import Database
from core.config import Config
import logging


class Core:
    """Main class of project (CORE)"""

    def __init__(self):
        super().__init__()
        self.config = Config()

    def run_app(self):
        app = QApplication([])
        logging.info('Created app.')
        login = LoginUI()
        logging.info('Created LoginUI.')
        result = login.exec()
        if result == QDialog.Accepted:
            logging.info('Login accepted.')
            role = login.authenticate()
            if role:
                router = Router()
                router.navigate_to(role)
                logging.info(f'Navigating to {role} window.')
                login.close()
            else:
                sys.exit(1)
        else:
            sys.exit(0)
        sys.exit(app.exec())
