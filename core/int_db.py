from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import Config


class InternalDatabase:
    """Class for working with internal db (users etc)"""

    def __init__(self):
        self.config = Config()
        self.engine = None
        self.Session = None

    def connect(self):
        """Connect to internal db"""
        db_path = self.config.get('internal_db_path')
        self.engine = create_engine(f'sqlite:///{db_path}')
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        """Get session for internal db"""
        if self.Session is None:
            self.connect()
        return self.Session()

    def close_session(self, session):
        """Close session for internal db"""
        session.close()
