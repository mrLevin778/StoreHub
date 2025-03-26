import asyncio
import logging
from PySide6.QtCore import QThread, QObject, Signal
from sqlalchemy.util import await_only

from storage.order_edit_ui import OrderEditUI
from storage.order_edit_service import OrderEditService
from core.ext_db import Database


class OrderEditHandler(QObject):
    """Handler for order editing"""
    order_saved = Signal(int)
    order_error = Signal(str)

    def __init__(self, parent=None, order_data=None):
        super().__init__()
        self.ui = OrderEditUI(parent, order_data)
        self.service = OrderEditService()
        self.db = Database()
        self.thread = QThread()
        self.session = None
        self._connect_signals()
        if order_data:
            self.ui.set_order_details(order_data)
        else:
            generated_number = self.service.generate_order_number()
            self.ui.order_number.setText(generated_number)
        self.start_async_setup()

    def start_async_setup(self):
        """Run DB init"""
        loop = asyncio.get_event_loop()
        if loop.is_running():
            asyncio.create_task(self.init_db())
        else:
            asyncio.run(self.init_db())

    async def init_db(self):
        """Async database session init"""
        self.session = await self.db.get_session()
        self.service.session = self.session
        logging.info('DB initializing......')

    def _connect_signals(self):
        self.ui.save_button.clicked.connect(self.on_save_order)
        self.ui.cancel_button.clicked.connect(self.cancel_order)

    def on_save_order(self):
        """Run save order in separate thread"""
        self.thread.started.connect(self.save_order_in_thread)
        self.thread.finished.connect(self.on_thread_finished)
        self.thread.start()

    def save_order_in_thread(self):
        """Save order after validating"""
        logging.info(f'Pushed button SAVE.')
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            order_details = self.ui.get_order_details()
            order_details['date'] = self.service.convert_qdate(order_details['date'])
            order_details['end_date'] = self.service.convert_qdate(order_details['end_date'])
            #loop.run_until_complete(self.init_db())
            new_order = loop.run_until_complete(self.service.save_order(order_details))
            if new_order:
                self.order_saved.emit(new_order.id)
                #self.ui.close()
            else:
                self.order_error.emit('Error saving order.')
        except Exception as e:
            logging.error(f'Error while saving order: {e}')
            if hasattr(self, 'order_error'):
                self.order_error.emit(str(e))
        finally:
            logging.info('Closing asyncio event loop......')
            loop.close()
            logging.info('Asyncio event loop is closed.')
            self.thread.quit()
            self.thread.wait()
            self.thread.deleteLater()

    def on_thread_finished(self):
        """Called when thread is finished"""
        logging.info('Thread finished.')
        self.thread.quit()
        self.thread.wait()
        self.thread.deleteLater()
        self.ui.close()
        if self.thread.isRunning():
            logging.warning('Thread is still running!')
        else:
            logging.info('Thread has successfully finished.')

    def cancel_order(self):
        """Cancel order editing"""
        logging.info(f'Pushed button CANCEL')
        logging.info('Order editing aborted.')
        self.ui.close()

    def show(self):
        """Show UI"""
        self.ui.show()
