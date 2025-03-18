import logging

from PySide6.QtWidgets import QApplication, QMainWindow
from storage.wms_service import Wms
from core.ui_loader import UiLoader


class WmsUI(QMainWindow):
    """Main window for WMS with tabs(handlers)"""

    def __init__(self):
        super().__init__()
        logging.info('WmsUI window created.')
        self.wms_handler = Wms()
        self.ui = UiLoader.load_ui('ui/wms.ui', self)
        self.fullscreen_window()
        #self.import_excel_button.clicked.connect(self.wms.import_from_excel('tools/test_products.xlsx'))

    def fullscreen_window(self):
        screen = QApplication.primaryScreen().availableGeometry()
        self.setGeometry(0, 0, screen.width(), screen.height())
        self.ui.show()

    def import_excel(self):
        Wms.import_from_excel('tools/test_products.xlsx')
