import logging
from admin.user import User

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

    @staticmethod
    def start_terminal():
        """Starting menu(TERMINAL)"""
        while True:
            choice = input(
                '\n1. Enter'
                '\n2. Registration'
                '\n3. Check user role'
                '\n4. Change user role'
                '\n5. Exit'
                '\nChoice option: '
            )
            if choice == '1':
                username = input('Enter your username: ')
                password = input('Enter your password: ')
                if AuthSystem.login(username, password):
                    print('Access allowed')
                    break
            elif choice == '2':
                AuthSystem.register()
            elif choice == '3':
                username = input('\nEnter your username to check your role: ')
                result = User.user_role(username)
                if result is None:
                    print(f'Error: incorrect user')
                else:
                    print(f'Your role - {result}')
            elif choice == '4':
                username = input('\nEnter your username: ')
                role = input('\nEnter your new role: ')
                User.set_user_role(username, role)
            elif choice == '5':
                logging.info('Exiting...')
                break
            else:
                logging.error('Unknown command, please try again.')
