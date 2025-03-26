from storage.wms_service import WmsService
from storage.wms_ui import WmsUI
from PySide6.QtCore import QObject


class WmsHandler(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = WmsUI()
        self.service = WmsService()