import _tkinter
import sys
from tkinter import TclError
from PySide6.QtWidgets import QApplication
from sqlalchemy.orm import Session

from core.external_db import ShopDatabase
from sale.pos_ui import PosUI
from storage.wms_ui_old import WmsUI
from admin.dashboard import Dashboard
from web.expressapi import ExpressApi
from core.authsystem import AuthSystem
from core.login import Login
from core.config import Config
import logging


class Core:
    """Main class of project (CORE)"""

    def __init__(self):
        self.api = ExpressApi()
        self.login_form = Login()
        self.config = Config()
        self.shop_db = ShopDatabase()

    def run_app(self):
        self.shop_db.connect()
        logging.info('Connected to DATABASE.')
        self.config.load_default_config()
        logging.info('Loaded default config.')
        #self.login_form.protocol('WM_DELETE_WINDOW', self.on_close)
        self.login_form.wm_protocol('WM_DELETE_WINDOW', self.on_close)
        self.login_form.mainloop()

    def on_close(self):
        """Close login window correct"""
        logging.info('Closing login window...')
        self.login_form.destroy()
        self.exit_app()

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
        sys.exit(0)



