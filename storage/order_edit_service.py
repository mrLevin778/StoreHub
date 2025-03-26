import asyncio
import logging

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from db.db_models import Order
from datetime import date
from core.ext_db import Database


class OrderEditService:
    """Class for business-logic"""

    def __init__(self, session=None):
        self.db = Database()
        self.session = session

    async def create_order(self, order_data: dict):
        """Crate new order"""
        if self.session is None:
            logging.error(f'Database session is not initialized.')
            return None
        try:
            new_order = Order(**order_data)
            self.session.add(new_order)
            await self.session.commit()
            await self.session.refresh(new_order)
            return new_order
        except SQLAlchemyError as e:
            await self.session.rollback()
            logging.error(f'Creating order error: {e}')
            return None
        except Exception as e:
            logging.error(f'Unexpected error: {e}')
            return None

    async def get_order(self, order_id: int):
        """Get order with id"""
        try:
            result = await self.session.execute(select(Order).filter(Order.id == order_id))
            return result.scalars().first()
        except SQLAlchemyError as e:
            logging.error(f'Getting order error: {e}')
            return None

    async def update_order(self, order_id: int, update_data: dict):
        """Update order"""
        try:
            result = await self.session.execute(select(Order).filter(Order.id == order_id))
            order = result.scalars().first()
            if order:
                for key, value in update_data.items():
                    setattr(order, key, value)
                await self.session.commit()
                await self.session.refresh(order)
            return order
        except SQLAlchemyError as e:
            await self.session.rollback()
            logging.error(f'Updating order error: {e}')
            return None

    def generate_order_number(self) -> str:
        """Generate order number in format Sxxxxxxxxxx(S - fixed symbol, xxxxxxxxxx - 10-digit"""
        try:
            # for database
            #last_order = self.session.query(Order).order_by(Order.id.desc()).first()
            #if last_order and last_order.number.startwith('S'):
            #    last_number = int(last_order.number[1:])
            #else:
            #    last_number = 0
            #next_number = last_number + 1
            #return f'S{next_number:010d}'
            try:
                with open('last_order_number.txt', 'r') as f:
                    last_number = int(f.read().strip())
            except (FileNotFoundError, ValueError):
                last_number = 0
            next_number = last_number + 1
            with open('last_order_number.txt', 'w') as f:
                f.write(str(next_number))
            return f'S{next_number:010d}'
        except Exception as e:
            logging.error(f'Order number generation error: {e}')
            raise

    def validate_order(self, order_details: dict) -> bool:
        """Check, if valid data"""
        if not order_details.get('number'):
            logging.error('Order number can not be empty!')
            return False
        if not order_details.get('client'):
            logging.error('Client not set!')
            return False
        return True

    def convert_qdate(self, qdate):
        """Convert pyside6 QDate in datetime.date"""
        if isinstance(qdate, date):
            return qdate
        return date(qdate.year(), qdate.month(), qdate.day())

    async def save_order(self, order_details: dict):
        if self.validate_order(order_details):
            try:
                new_order = await self.create_order(order_details)
                if new_order:
                    logging.info(f'Order saved. ID: {new_order.id}')
                    return new_order
                else:
                    logging.error(f'Order save failed.')
                    return None
            except Exception as e:
                logging.error(f'Error while saving order: {e}')
                return None
        else:
            logging.error(f'Order validation failed.')
            return None
