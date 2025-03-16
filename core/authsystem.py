import logging
from core.user import User

logging.basicConfig(level=logging.INFO)


class AuthSystem:
    """Class for login"""

    @staticmethod
    def login(username: str, password: str):
        """login form"""
        if User.authenticate_user(username, password):
            logging.info('Successfully logged in')
            return True
        logging.warning('Incorrect login of password')
        return False

    @staticmethod
    def register():
        """register form"""
        username = input('Enter login: ')
        users = User.load_users()
        if username in users:
            logging.warning(f'User with username "{username}" already exist!')
            return None
        password = input('Enter password: ')
        hashed_password = User.hash_password(password)
        # add new user
        users[username] = {'password': hashed_password, 'role': 'user'}
        User.save_users(users)
        logging.info(f'User {username} is successfully registered!')