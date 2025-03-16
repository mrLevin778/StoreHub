from admin.dashboard_ui import DashboardUI
from sale.pos_ui import PosUI
from storage.wms_ui import WmsUI
import logging
from PySide6.QtWidgets import QMessageBox


class Router:
    """Class for routing from login form to role UI"""

    def __init__(self):
        self.window = None

    def navigate_to(self, role: str):
        if self.window:
            self.window.close()
        try:
            if role is None:
                raise KeyError(f'User does not have an assigned role.')
            if role in ['admin', 'owner']:
                self.window = DashboardUI()
            elif role == 'cashier':
                self.window = PosUI()
            elif role == 'warehouse manager':
                self.window = WmsUI()
            else:
                logging.critical(f'Error! Incorrect role!')
            self.window.ui.show()
        except Exception as e:
            logging.critical(f'Unexpected error occured! Error: {e}')
