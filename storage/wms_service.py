from core.ext_db import Database
from db.db_models import Product
from core.config import Config
import pandas as pd


class WmsService:
    """Main class for Warehouse Management System in StoreHub"""

    def __init__(self):
        super().__init__()
        self.config = Config()
        self.db = Database()


    def import_from_excel(self, filepath):
        session = self.db.get_session()
        try:
            df = pd.read_excel(filepath)
            expected_columns = ['name', 'description', 'price', 'stock', 'barcode']
            if not all(col in df.columns for col in expected_columns):
                raise ValueError(f'ERROR: unexpected columns')
            products = [
                Product(
                    name=row['name'],
                    description=row['description'],
                    price=row['price'],
                    stock=row['stock'],
                    barcode=str(row['barcode'])
                )
                for _, row in df.iterrows()
            ]
            session.add_all(products)
            session.commit()
            print(f'Imported {len(products)} items to DB.')
        except Exception as e:
            session.rollback()
            print(f'Import error {e}')
        finally:
            session.close()
