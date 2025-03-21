import logging

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from storage.wms_service import WmsService
from core.ui_loader import UiLoader
from storage.order_edit_handler import OrderEditHandler


class WmsUI(QMainWindow):
    """Main window for WMS with tabs(handlers)"""

    def __init__(self):
        super().__init__()
        self.order_handler = None
        self.new_order_btn = None
        logging.info('WmsUI window created.')
        self.wms_handler = WmsService()
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
        self._set_signals_orders_tab()

    def setup_dashboard_tab(self):
        pass

    def setup_orders_tab(self):
        self.new_order_btn = self.ui.findChild(QPushButton, 'new_order_btn')

    def _set_signals_orders_tab(self):
        self.new_order_btn.clicked.connect(lambda: self.open_order_editor())

    def open_order_editor(self, order_data=None):
        """Open window for editing order"""
        self.order_handler = OrderEditHandler(self, order_data)
        self.order_handler.show()

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
        Wms.import_from_excel('tools/test_products.xlsx')
