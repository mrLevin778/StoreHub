from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from sale.pos_handler import PosHandler
from core.ui_loader import UiLoader


class PosUI(QMainWindow):
    """Main window for POS with tabs(handlers)"""

    def __init__(self):
        super().__init__()
        self.ui = UiLoader.load_ui('ui/pos.ui', self)
        self.fullscreen_window()
        self.pos_handler = PosHandler()
        #self.ui.card_pay_button = self.findChild(QPushButton, 'btnCard')
        #self.ui.cash_pay_button = self.findChild(QPushButton, 'btnCash')
        #  connect signals
        #self.card_pay_button.clicked.connect(self.handle_card_pay)
        #self.cash_pay_button.clicked.connect(self.handle_cash_pay)

    def fullscreen_window(self):
        screen = QApplication.primaryScreen().availableGeometry()
        self.setGeometry(0, 0, screen.width(), screen.height())

    def handle_card_pay(self):
        print('card pay')

    def handle_cash_pay(self):
        print('cash pay')
