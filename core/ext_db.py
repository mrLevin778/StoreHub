from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker, scoped_session
from core.config import Config
import logging
import os
import sys
from db.db_models import Base


class Database:
    """Class for working with external db (goods etc)"""

    def __init__(self):
        self.config = Config()
        self.engine = None
        self.Session = None

    async def connect(self):
        """Connect to DB, sqlite creating, if it not exist"""
        try:
            db_type = self.config.get('shop_db_type')
            db_path = self.config.get('shop_db_path')
            if db_type == 'sqlite':
                db_dir = os.path.dirname(db_path)
                if not os.path.exists(db_dir):
                    os.makedirs(db_dir, exist_ok=True)
                    logging.info(f'Directory {db_dir} created for SQLite database.')
                db_exists = os.path.exists(db_path)
                self.engine = create_async_engine(f'sqlite+aiosqlite:///{db_path}', echo=True)
                logging.info('Create async engine for sqlite')
                if not db_exists:
                    await self.create_database()
            elif db_type == 'postgresql':
                db_url = self.config.get('shop_db_url')
                self.engine = create_async_engine(db_url, echo=True)
                logging.info('Crete async engine for PostgreSQL')
            self.Session = async_sessionmaker(bind=self.engine, expire_on_commit=False)
        except SQLAlchemyError as e:
            logging.error(f'Error connecting to database: {e}')
            raise

    async def create_database(self):
        """Create DB, if it not exist"""
        try:
            logging.info('Creating new SQlite database schema...')
            if self.engine is None:
                await self.connect()
            async with self.engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
        except SQLAlchemyError as e:
            logging.error(f'Creating base error: {e}')
            raise
        logging.info('Database schema created successfully.')

    async def get_session(self) -> AsyncSession:
        """Return new database session"""
        if self.Session is None:
            await self.connect()
        return self.Session()

    async def close_session(self, session: AsyncSession):
        """Close given session"""
        try:
            await session.close()
            logging.info('Session closed')
        except SQLAlchemyError as e:
            logging.error(f'Closing session error: {e}')
