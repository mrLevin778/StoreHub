import logging
from storage.order_edit_ui import OrderEditUI
from storage.order_edit_service import OrderEditService


class OrderEditHandler:

    def __init__(self, parent=None, order_data=None):
        self.ui = OrderEditUI(parent, order_data)
        self.service = OrderEditService()
        self._connect_signals()
        if order_data:
            self.ui.set_order_details(order_data)
        else:
            generated_number = self.service.generate_order_number()
            self.ui.order_number.setText(generated_number)

    def _connect_signals(self):
        self.ui.save_button.clicked.connect(self.save_order)
        self.ui.cancel_button.clicked.connect(self.cancel_order)

    def save_order(self):
        """Save order after validating"""
        order_details = self.ui.get_order_details()
        if self.service.validate_order(order_details):
            self.service.save_order(order_details)
            logging.info('Order saved.')
            self.ui.close()
        else:
            logging.error('Validating error, saving aborted.')

    def cancel_order(self):
        logging.info('Order editing aborted.')
        self.ui.close()

    def show(self):
        self.ui.show()
