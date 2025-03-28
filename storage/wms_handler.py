from storage.wms_service import WmsService
from storage.order_edit_handler import OrderEditHandler
from storage.wms_ui import WmsUI
from PySide6.QtCore import QObject


class WmsHandler(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = WmsUI()
        self.service = WmsService()
        self._set_signals_orders_tab()
        self.orders_table = self.ui.orders_table

    def _set_signals_orders_tab(self):
        self.ui.new_order_btn.clicked.connect(lambda: self.open_order_editor())

    def open_order_editor(self, order_data=None):
        """Open window for editing order"""
        order_handler = OrderEditHandler(self, order_data)
        order_handler.show()
