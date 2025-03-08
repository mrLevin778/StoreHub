from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import Config
import logging
import os
from db.db_models import Base


class ShopDatabase:
    """Class for working with external db (goods etc)"""

    def __init__(self):
        self.config = Config()
        self.engine = None
        self.Session = None

    def connect(self):
        """Connect to DB, sqlite creating, if it not exist"""
        db_type = self.config.get('shop_db_type')
        db_path = self.config.get('shop_db_path')
        if db_type == 'sqlite':
            db_exists = os.path.exists(db_path)
            self.engine = create_engine(f'sqlite:///{db_path}', echo=True)
            logging.info('Create engine for sqlite')
            if not db_exists:
                self.create_database()
        elif db_type == 'postgresql':
            pass  # logic for connect to postgresql
        self.Session = sessionmaker(bind=self.engine)

    def create_database(self):
        """Create DB, if it not exist"""
        logging.info('Creating new SQlite database...')
        if self.engine is None:
            self.connect()
        Base.metadata.create_all(self.engine)

    def get_session(self):
        """"""
        if self.Session is None:
            self.connect()
        return self.Session()

    def close_session(self, session):
        """"""
        session.close()
