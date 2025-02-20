from admin.user import User


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
            choice = input(
                '\n1. Enter'
                '\n2. Registration'
                '\n3. Check user role'
                '\n4. Change user role'
                '\n5. Exit'
                '\nChoice option: '
            )
            if choice == '1':
                user = AuthSystem.login()
                if user:
                    print('Access allowed')
                    break
            elif choice == '2':
                AuthSystem.register()
            elif choice == '3':
                username = input('\nEnter your username, if you want check your role: ')
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
                print('Exiting...')
                break
            else:
                print('Unknown command, please try again.')
