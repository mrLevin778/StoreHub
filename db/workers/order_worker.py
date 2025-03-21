import logging

from PySide6.QtCore import QThread, QObject, Signal
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from db.db_models import Order
from core.ext_db import Database
from storage.order_edit_service import OrderEditService


class OrderEditWorker(QObject):
    """Class for async work with database"""
    finished = Signal(object)
    error = Signal(str)

    def __init__(self, operation, order_data):
        super().__init__()
        self.operation = operation
        self.order_data = order_data
        self.db = Database()

    def run(self):
        """Run async operation in other thread"""
        try:
            asyncio.run(self._async_run())
            #elif self.method == 'get_order':
            #    result = loop.run_until_complete(OrderEditService.get_order(self.session, self.data))
            #elif self.method == 'update_order':
            #    result = loop.run_until_complete(OrderEditService.update_order(self.session, self.data))
        except Exception as e:
            self.error.emit(str(e))
            logging.error(f'Async operation error: {e}')

    async def _async_run(self):
        """Async method for working with db"""
        async for session in self.db.get_session():
            try:
                if self.operation == 'create_order':
                    new_order = Order(**self.order_data)
                    session.add(new_order)
                    await session.commit()
                    self.finished.emit(new_order.id)
                else:
                    raise ValueError(f'Unknown operation: {self.operation}')
            except Exception as e:
                logging.error(f'Error while saving order: {e}')
                self.error.emit(str(e))
            finally:
                await session.close()
