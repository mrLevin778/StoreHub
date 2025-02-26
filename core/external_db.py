from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import Config


class ShopDatabase:
    """Class for working with external db (goods etc)"""

    def __init__(self):
        self.config = Config()
        self.engine = None
        self.Session = None

    def connect(self):
        """"""
        db_type = self.config.get('shop_db_type')
        db_path = self.config.get('shop_db_path')
        if db_type == 'sqlite':
            self.engine = create_engine(f'sqlite:///{db_path}')
        elif db_type == 'postgresql':
            pass  #logic for postgresql
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        """"""
        if self.Session is None:
            self.connect()
        return self.Session()

    def close_session(self, session):
        """"""
        session.close()
