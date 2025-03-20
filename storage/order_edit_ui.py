import logging

from PySide6.QtWidgets import QDialog, QPushButton, QLineEdit, QComboBox, QWidget, QVBoxLayout, QDateEdit, QTextEdit
from core.ui_loader import UiLoader


class OrderEditUI(QDialog):
    """Class for edit order window"""

    def __init__(self, parent=None, order_data=None):
        super().__init__(parent)
        self.content_widget = UiLoader.load_ui('ui/order_edit.ui', self)
        if not self.content_widget:
            raise RuntimeError("Not load UI")
        container = QWidget(self)
        container_layout = QVBoxLayout(container)
        container_layout.addWidget(self.content_widget)
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(container)
        self.setLayout(main_layout)
        self.order_data = order_data
        self._setup_order_edit()

    def _setup_order_edit(self):
        """Find child for elements, can be remove if UI compiled"""
        # save/cancel buttons
        self.save_button = self.findChild(QPushButton, 'save_order_btn')
        self.cancel_button = self.findChild(QPushButton, 'cancel_order_btn')
        # order elements
        self.order_number = self.findChild(QLineEdit, 'order_number')
        self.client_order_name = self.findChild(QLineEdit, 'client_order_name')
        self.order_status_cbx = self.findChild(QComboBox, 'order_status_cbx')
        self.order_date = self.findChild(QDateEdit, 'order_date')
        self.manager_name_cbx = self.findChild(QComboBox, 'manager_name_cbx')
        self.comment_order_txtedit = self.findChild(QTextEdit, 'comment_order_txtedit')
        self.payment_method_cbx = self.findChild(QComboBox, 'payment_method_cbx')
        self.complete_order_date = self.findChild(QDateEdit, 'complete_order_date')
        self.order_total_amount = self.findChild(QLineEdit, 'order_total_amount')
        # buttons for add or remove items in order
        self.add_product_btn = self.findChild(QPushButton, 'add_product_btn')
        self.remove_product_btn = self.findChild(QPushButton, 'remove_product_btn')

    def set_order_details(self, order_data):
        self.order_number.setText(self.order_data.get('number', ''))
        self.client_order_name.setText(self.order_data.get('client', ''))
        self.order_status_cbx.setCurrentText(self.order_data.get('status', ''))
        self.order_date.setDate(self.order_data.get('date', '')) ###
        self.manager_name_cbx.setCurrentText(self.order_data.get('manager', ''))
        self.comment_order_txtedit.setMarkdown(self.order_data.get('comment', '')) ###
        self.payment_method_cbx.setCurrentText(self.order_data.get('payment', ''))
        self.complete_order_date.SetDate(self.order_date.get('end_date', '')) ###
        self.order_total_amount.setText(self.order_data.get('total_amount', ''))

    def get_order_details(self):
        return {
            'number': self.order_number.text(),
            'client': self.client_order_name.text(),
            'status': self.order_status_cbx.currentText(),
            'date': self.order_date.date(),
            'manager': self.manager_name_cbx.currentText(),
            'comment': self.comment_order_txtedit.toMarkdown(),
            'payment': self.payment_method_cbx.currentText(),
            'end_date': self.complete_order_date.date(),
            'total_amount': self.order_total_amount.text()
        }

