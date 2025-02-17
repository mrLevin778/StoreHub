from sale.pos import Pos
from storage.wms import Wms
from admin.dashboard import Dashboard
from web.expressapi import ExpressApi
from admin.user import User


class Core:
    """Main class of project (CORE)"""

    def __init__(self):
        self.pos = Pos()
        self.wms = Wms()
        self.dashboard = Dashboard()
        self.api = ExpressApi()

    @staticmethod
    def run_app():
        print('LOGIN FORM')
        AuthSystem.start()


class AuthSystem:
    """Class for login"""

    @staticmethod
    def login():
        """login form"""
        username = input('Enter your login: ')
        password = input('Enter your password: ')
        if User.authenticate_user(username, password):
            print(f'Congratulations, {username}!')
            return username
        else:
            print(f'Incorrect login or password!')
            return None

    @staticmethod
    def register():
        """register form"""
        username = input('Enter login: ')
        users = User.load_users()
        if username in users:
            print(f'User with this username is existing!')
            return None
        password = input('Enter password: ')
        hashed_password = User.hash_password(password)
        # adding new user
        users[username] = {'password': hashed_password, 'role': 'user'}
        User.save_users(users)
        print(f'User {username} is successfully registered!')

    @staticmethod
    def start():
        """Starting menu"""
        while True:
            choice = input('\n1. Enter\n2. Registration\n3. Exit\nChoice option: ')
            if choice == '1':
                user = AuthSystem.login()
                if user:
                    print('Access allowed')
                    break
            elif choice == '2':
                AuthSystem.register()
            elif choice == '3':
                print('Exiting...')
                break
            else:
                print('Unknown command, please try again.')
