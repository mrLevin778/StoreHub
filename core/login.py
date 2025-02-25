import customtkinter as ctk
from tkinter import messagebox
from core.authsystem import AuthSystem


class Login(ctk.CTk):
    """Class for login form"""

    def __init__(self):
        super().__init__()
        self.auth_system = AuthSystem()
        self.title('Authorisation Form')
        self.geometry('300x250')
        self.center_window(300, 250)
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('blue')
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

    def center_window(self, width, height):
        """Centers the window on the screen"""
        self.update_idletasks()
        width = self.winfo_width() or 300
        height = self.winfo_height() or 250
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry(f'{width}x{height}+{x}+{y}')

    def authenticate(self):
        """Authenticate user and handle success or failure"""
        if self.auth_system.login(self.username_entry.get(), self.password_entry.get()):
            self.on_login_success()
        else:
            messagebox.showerror('Error', 'Incorrect login or password')

    def on_login_success(self):
        """Handle successful login"""
        messagebox.showinfo('Success', 'Access granted!')
        self.destroy()
        # place for calling menu or other display

    def open_terminal(self):
        """Open terminal via Core"""
        self.destroy()  # close login window
        AuthSystem.start_terminal()
            
    
        
        
