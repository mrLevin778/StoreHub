import asyncio
import logging
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTableView
from PySide6.QtCore import QObject, QTimer

from storage.wms_handler import WmsHandler
from storage.wms_service import WmsService
from core.ui_loader import UiLoader
from storage.order_edit_handler import OrderEditHandler


class WmsUI(QMainWindow):
    """Main window for WMS with tabs(handlers)"""

    def __init__(self):
        super().__init__()
        self.order_handler = None
        self.new_order_btn = None
        self.orders_table = None
        logging.info('WmsUI window created.')
        self.wms_handler = WmsHandler()
        self.ui = UiLoader.load_ui('ui/wms.ui', self)
        self.fullscreen_window()
        self._setup_tabs()

    def fullscreen_window(self):
        screen = QApplication.primaryScreen().availableGeometry()
        self.setGeometry(0, 0, screen.width(), screen.height())
        self.ui.show()

    def _setup_tabs(self):
        self.setup_dashboard_tab()
        self.setup_orders_tab()
        self.setup_movings_tab()
        self.setup_returns_tab()
        self.setup_catalog_tab()
        self.setup_analytics_tab()
        self.setup_settings_tab()

    def setup_dashboard_tab(self):
        pass

    def setup_orders_tab(self):
        self.new_order_btn = self.ui.findChild(QPushButton, 'new_order_btn')
        # main table with orders
        self.orders_table = self.ui.findChild(QTableView, 'orders_table')

    def setup_movings_tab(self):
        pass

    def setup_returns_tab(self):
        pass

    def setup_catalog_tab(self):
        pass

    def setup_analytics_tab(self):
        pass

    def setup_settings_tab(self):
        pass

    def import_excel(self):
        pass
