from sqlalchemy import create_engine
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

    def connect(self):
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
                self.engine = create_engine(f'sqlite:///{db_path}', echo=True)
                logging.info('Create engine for sqlite')
                if not db_exists:
                    self.create_database()
            elif db_type == 'postgresql':
                pass  # logic for connect to postgresql
            self.Session = scoped_session(sessionmaker(bind=self.engine))
        except Exception as e:
            logging.error(f'Error connecting to database: {e}')
            sys.exit(1)

    def create_database(self):
        """Create DB, if it not exist"""
        logging.info('Creating new SQlite database schema...')
        if self.engine is None:
            self.connect()
        try:
            Base.metadata.create_all(self.engine)
            logging.info('Database schema created successfully.')
        except Exception as e:
            logging.error(f'Error creating database schema: {e}')
            sys.exit(1)

    def get_session(self):
        """Return new database session"""
        if self.Session is None:
            self.connect()
        return self.Session()

    def close_session(self, session):
        """Close given session"""
        session.close()
