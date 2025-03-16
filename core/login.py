import logging
import sys
from core.authsystem import AuthSystem
from core.config import Config
from core.user import User
from core.router import Router
from PySide6.QtWidgets import QApplication, QMessageBox, QDialog, QWidget

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Login:
    """Class for login form"""

    def __init__(self):
        super().__init__()
        self.auth_system = AuthSystem()

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
