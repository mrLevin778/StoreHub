import logging
from PySide6.QtCore import QThread
from storage.order_edit_ui import OrderEditUI
from storage.order_edit_service import OrderEditService
from core.ext_db import Database
from db.workers.order_worker import OrderEditWorker


class OrderEditHandler:

    def __init__(self, parent=None, order_data=None):
        self.ui = OrderEditUI(parent, order_data)
        self.service = OrderEditService()
        self.db = Database()
        self.session = None
        self.thread = None
        self.worker = None
        self._connect_signals()
        if order_data:
            self.ui.set_order_details(order_data)
        else:
            generated_number = self.service.generate_order_number()
            self.ui.order_number.setText(generated_number)

    async def init_db(self):
        """Async database session init"""
        self.session = await self.db.get_session()

    def _connect_signals(self):
        self.ui.save_button.clicked.connect(self.save_order)
        self.ui.cancel_button.clicked.connect(self.cancel_order)

    def save_order(self):
        """Save order after validating"""
        order_details = self.ui.get_order_details()
        if self.service.validate_order(order_details):
            if not self.session:
                logging.warning('Session is None.........')
            self.thread = QThread()
            self.worker = OrderEditWorker('create_order', order_details)
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.on_order_saved)
            self.worker.error.connect(self.on_worker_error)
            self.thread.start()
        else:
            logging.error('Validating error, saving aborted.')

    def on_order_saved(self, result):
        """Handle order creating result"""
        logging.info(f'Order saved: {result}.')
        self.thread.quit()
        self.thread.wait()
        self.ui.close()

    def on_worker_error(self, error_message):
        """Handle error in worker"""
        logging.error(f'Error while saving order: {error_message}.')
        self.thread.quit()
        self.thread.wait()

    def cancel_order(self):
        logging.info('Order editing aborted.')
        self.ui.close()

    def show(self):
        self.ui.show()
