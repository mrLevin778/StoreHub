import os.path
import bcrypt
import json


class User:
    """Class for creating user with some role"""
    FILE_PATH = "users.json"

    def __init__(self, username, password, role="user"):
        self.role = role
        self.username = username
        self.password = self._hash_password(password)

    @staticmethod
    def _hash_password(password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    @staticmethod
    def load_users():
        if not os.path.exists(User.FILE_PATH):
            with open(User.FILE_PATH, "w") as file:
                json.dump({}, file)  # create empty json file

        with open(User.FILE_PATH, "r") as file:
            return json.load(file)

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
        with open(User.FILE_PATH, "w") as file:
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
        users[username]['password'] = User._hash_password(new_password)
        User.save_users(users)
        print(f'Password for {username} is updated!')

    def delete_user(username):
        users = User.load_users()
        if username not in users:
            raise ValueError(f'User {username} is not found!')
        del users[username]
        User.save_users(users)
        print(f'User {username} is deleted!')

    def user_role(self):
        pass

# usage: new_user = User('user name', 'user password', 'user role (admin)')
# new_user.create_user()
