import os
import bcrypt
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class User:
    """Class for creating user with some role"""
    FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "users.json")
    ROLES = {
        "admin": "Full access",
        "owner": "Full access",
        "manager": "POS, statistics",
        "warehouse manager": "Warehouse",
        "cashier": "POS",
    }

    def __init__(self, username, password, role="user"):
        self.role = role
        self.username = username
        self.password = self.hash_password(password)

    @staticmethod
    def hash_password(password):
        """Hashes the password using bcrypt"""
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    @staticmethod
    def load_users():
        """Loads users from the users.json file"""
        if not os.path.exists(User.FILE_PATH):
            os.makedirs(os.path.dirname(User.FILE_PATH), exist_ok=True)  # create directory
            with open(User.FILE_PATH, "w", encoding="UTF-8") as file:
                json.dump({}, file, indent=4)  # create empty json file
        try:
            with open(User.FILE_PATH, "r", encoding="UTF-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            logging.error(f'File {User.FILE_PATH} incorrect! Creating new file')
            with open(User.FILE_PATH, "w", encoding="UTF-8") as file:
                json.dump({}, file, indent=4)
            return {}

    @staticmethod
    def authenticate_user(username, password):
        """Authenticate a user"""
        users = User.load_users()
        if username not in users:
            logging.warning(f'User {username} does not exist.')
            return False  # user does not exist
        hashed_password = users[username]['password']
        if bcrypt.checkpw(password.encode(), hashed_password.encode()):
            logging.info(f'User {username} authenticated successfully.')
            return True
        logging.warning(f'Incorrect password for user {username}.')
        return False

    def create_user(self):
        """Create a new user"""
        users = User.load_users()
        if self.username in users:
            logging.error(f'User {self.username} already exists!')
            raise ValueError('User already exist!')
        users[self.username] = {'password': self.password, 'role': self.role}
        self.save_users(users)
        logging.info(f'User {self.username} is created!')

    @staticmethod
    def save_users(users):
        """Saves the users to the JSON file"""
        os.makedirs(os.path.dirname(User.FILE_PATH), exist_ok=True)
        with open(User.FILE_PATH, "w", encoding="UTF-8") as file:
            json.dump(users, file, indent=4)

    @staticmethod
    def update_password(username, old_password, new_password):
        """Updates the password of a user"""
        users = User.load_users()
        if username not in users:
            logging.error(f'User {username} not found.')
            raise ValueError(f'User {username} not found')
        hashed_password = users[username]['password']
        # check old password:
        if not bcrypt.checkpw(old_password.encode(), hashed_password.encode()):
            logging.error(f'Incorrect old password for user {username}.')
            raise ValueError('Wrong old password!')
        # update password:
        users[username]['password'] = User.hash_password(new_password)
        User.save_users(users)
        logging.info(f'Password for user {username} is updated!')

    @staticmethod
    def delete_user(username):
        """Deletes a user"""
        users = User.load_users()
        if username not in users:
            logging.error(f'User {username} not found.')
            raise ValueError(f'User {username} is not found!')
        del users[username]
        User.save_users(users)
        logging.info(f'User {username} is deleted!')

    @staticmethod
    def user_role(username):
        """Getting user role"""
        users = User.load_users()
        role = users.get(username, {}).get("role", None)
        if role:
            logging.info(f'User {username} has role {role}.')
        else:
            logging.warning(f'User {username} not found.')
        return role

    @staticmethod
    def set_user_role(username, new_role):
        """Changes user role"""
        if new_role not in User.ROLES:
            logging.error(f'Unknown role {new_role}.')
            return False
        users = User.load_users()
        if username not in users:
            logging.error(f'User {username} not found.')
            return False
        users[username]["role"] = new_role
        User.save_users(users)
        logging.info(f'User {username} role is changed to {new_role}.')
        return True

