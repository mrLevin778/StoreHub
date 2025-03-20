import logging


class OrderEditService:
    """Class for business-logic"""
    def __init__(self, session=None):
        self.session = session

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

    def save_order(self, order_details: dict) -> None:
        """Save order to database"""
        # database saving logic
        logging.info(f'Order saved: {order_details}')