import logging

from PySide6.QtWidgets import QApplication, QMainWindow
from core.ui_loader import UiLoader


class DashboardUI(QMainWindow):
    """Main window for Dashboard with tabs(UI)"""

    def __init__(self):
        super().__init__()
        logging.info('DashboardUI window created.')
        self.ui = UiLoader.load_ui('ui/dashboard.ui', self)
        self.fullscreen_window()

    def fullscreen_window(self):
        screen = QApplication.primaryScreen().availableGeometry()
        self.setGeometry(0, 0, screen.width(), screen.height())
        self.ui.show()

