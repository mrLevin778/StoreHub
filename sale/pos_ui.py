from PySide6.QtWidgets import QMainWindow

from core.ui_loader import UiLoader


class PosUI(QMainWindow):
    """Main window for POS with tabs"""

    def __init__(self):
        super().__init__()
        self.ui = UiLoader.load_ui('ui/pos.ui', self.centralWidget())
        self.setCentralWidget(self.ui.centralWidget())
        self.setFixedSize(self.ui.size())
        #  connect signals
        self.ui.pushButton.clicked.connect(self.action_button)

    def action_button(self):
        print('ITS WORK.')