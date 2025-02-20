import os
import bcrypt
import json


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
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    @staticmethod
    def load_users():
        if not os.path.exists(User.FILE_PATH):
            os.makedirs(os.path.dirname(User.FILE_PATH), exist_ok=True)  # create directory
            with open(User.FILE_PATH, "w", encoding="UTF-8") as file:
                json.dump({}, file, indent=4)  # create empty json file
        try:
            with open(User.FILE_PATH, "r", encoding="UTF-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f'File {User.FILE_PATH} incorrect! Creating new file')
            with open(User.FILE_PATH, "w", encoding="UTF-8") as file:
                json.dump({}, file, indent=4)
            return {}

    @staticmethod
    def authenticate_user(username, password):
        users = User.load_users()
        if username not in users:
            return False  # user is not exist
        hashed_password = users[username]['password']
        return bcrypt.checkpw(password.encode(), hashed_password.encode())

    def create_user(self):
        users = self.load_users()
        if self.username in users:
            raise ValueError('User is existing!')
        users[self.username] = {'password': self.password, 'role': self.role}
        self.save_users(users)
        print(f'User {self.username} is created!')

    def save_users(users):
        os.makedirs(os.path.dirname(User.FILE_PATH), exist_ok=True)
        with open(User.FILE_PATH, "w", encoding="UTF-8") as file:
            json.dump(users, file, indent=4)

    def update_password(username, old_password, new_password):
        users = User.load_users()
        if username not in users:
            raise ValueError(f'User {username} not found')
        hashed_password = users[username]['password']
        # check old password:
        if not bcrypt.checkpw(old_password.encode(), hashed_password.encode()):
            raise ValueError('Wrong old password!')
        # update password:
        users[username]['password'] = User.hash_password(new_password)
        User.save_users(users)
        print(f'Password for {username} is updated!')

    def delete_user(username):
        users = User.load_users()
        if username not in users:
            raise ValueError(f'User {username} is not found!')
        del users[username]
        User.save_users(users)
        print(f'User {username} is deleted!')

    def user_role(username):
        """Getting user role"""
        users = User.load_users()
        return users.get(username, {}).get("role", None)

    def set_user_role(username, new_role):
        """Change user role"""
        users = User.load_users()
        if username not in users:
            print('Error: user is not found')
            return False
        if new_role not in User.ROLES:
            print('Error: unknown role')
            return False
        users[username]["role"] = new_role
        User.save_users(users)
        print(f'User role is changed for {username}. New role - {new_role}')
        return True

