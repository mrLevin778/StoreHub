import logging
import sys
import asyncio

from PySide6.QtWidgets import QApplication, QDialog

from core.config import Config
from core.login_ui import LoginUI
from core.router import Router


class Core:
    """Main class of project (CORE)"""

    def __init__(self):
        super().__init__()
        self.config = Config()
        self.loop = None

    def run_app(self):
        app = QApplication([])
        logging.info('Created app.')
        self._setup_asyncio()
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

    def _setup_asyncio(self):
        """Ensure that an event loop is properly set up fro asyncio"""
        try:
            self.loop = asyncio.get_running_loop()
        except RuntimeError:
            self.loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self.loop)
