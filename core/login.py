import logging
import customtkinter as ctk
from tkinter import messagebox
from sale.pos_ui import PosUI
from storage.wms_ui import WmsUI
from admin.dashboard_ui import DashboardUI
from core.authsystem import AuthSystem
from core.config import Config
from admin.user import User

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Login(ctk.CTk):
    """Class for login form"""

    def __init__(self):
        super().__init__()
        self.auth_system = AuthSystem()
        self.config = Config()
        self.title('Authorisation Form')
        self.geometry('300x250')
        self.center_window()
        self._apply_settings()
        # label
        self.label = ctk.CTkLabel(self, text='Login to system', font=('Arial', 18))
        self.label.pack(pady=10)
        # login field
        self.username_entry = ctk.CTkEntry(self, placeholder_text='Login')
        self.username_entry.pack(pady=5)
        # password field
        self.password_entry = ctk.CTkEntry(self, placeholder_text='Password', show='*')
        self.password_entry.pack(pady=5)
        # submit button
        self.login_button = ctk.CTkButton(self, text='Submit', command=self.authenticate)
        self.login_button.pack(pady=10)
        # terminal button
        self.terminal_button = ctk.CTkButton(self, text='TERMINAL', command=self.open_terminal)
        self.terminal_button.pack(pady=5)

    def _apply_settings(self):
        """Apply settings from config file"""
        appearance_mode = self.config.get('appearance_mode')
        theme_color = self.config.get('theme_color')
        if appearance_mode:
            ctk.set_appearance_mode(appearance_mode)
        if theme_color:
            ctk.set_default_color_theme(theme_color)

    def center_window(self):
        """Centers the window on the screen"""
        self.update_idletasks()
        width, height = 300, 250
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry(f'{width}x{height}+{x}+{y}')

    def authenticate(self):
        """Authenticate user and handle success or failure"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.auth_system.login(username, password):
            self.on_login_success(username)
        else:
            messagebox.showerror('Error', 'Incorrect login or password')

    def on_login_success(self, username):
        """Handle successful login"""
        print(f'Access granted.')
        try:
            role = User.user_role(username)
            if role is None:
                raise KeyError(f'User {username} does not have an assigned role.')
            if role in ['admin', 'owner']:
                self.destroy()
                dashboard = DashboardUI()
                dashboard.mainloop()
            elif role == 'cashier':
                self.destroy()
                pos = PosUI()
                pos.mainloop()
            elif role == 'warehouse manager':
                self.destroy()
                wms = WmsUI()
                wms.mainloop()
            else:
                logging.warning(f'User {username} does not have any permissions!')
        except Exception as exc:
            logging.error(f'Unexpected error occurred: {exc}')

    def open_terminal(self):
        """Open terminal via Core"""
        self.destroy()  # close login window
        AuthSystem.start_terminal()
