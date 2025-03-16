import sys
from PySide6.QtWidgets import QApplication, QDialog
from sqlalchemy.orm import Session
from core.router import Router
from core.login_ui import LoginUI
from core.ext_db import ShopDatabase
from sale.pos_ui import PosUI
from storage.wms_ui import WmsUI
from admin.dashboard import Dashboard
from web.expressapi import ExpressApi
from core.authsystem import AuthSystem
from core.user import User
from core.config import Config
import logging


class Core:
    """Main class of project (CORE)"""

    def __init__(self):
        super().__init__()
        self.app = QApplication(sys.argv)
        self.config = Config()

    def run_app(self):
        login = LoginUI()
        login.ui.exec()
        if login.exec() == QDialog.Accepted:
            role = login.authenticate()
            router = Router()
            router.navigate_to(role)
            sys.exit(self.app.exec())
        else:
            sys.exit(0)

    def exit_app(self):
        """Method for correct exit"""
        self.config.save_user_config()
        logging.info('Saving user config...')
        self.shop_db.close_session(Session)
        logging.info('Closing database session...')
        logging.info('Closing application...')
        try:
            if self.login_form:
                self.login_form.quit()
        except Exception as e:
            logging.warning(f'Error quitting Tkinter mainloop: {e}')
        logging.info('Application closed.')



