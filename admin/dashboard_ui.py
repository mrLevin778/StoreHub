import customtkinter as ctk
from core.config import Config


class DashboardUI(ctk.CTk):
    """Main dashboard window with tabs"""

    def __init__(self):
        super().__init__()
        self.config = Config()
        self._apply_settings()
        self.title('Dashboard')
        self.geometry('800x600')
        # creating tab view
        self.tab_view = ctk.CTkTabview(self)
        self.tab_view.pack(fill='both', expand=True, padx=10, pady=10)
        # adding tabs
        self.analytics_tab = self.tab_view.add('Analytics')
        self.sales_tab = self.tab_view.add('Sales')
        self.settings_tab = self.tab_view.add('Settings')
        # placeholder labels
        ctk.CTkLabel(self.analytics_tab, text='Analytics data here').pack(pady=20)
        ctk.CTkLabel(self.sales_tab, text='Sales data here').pack(pady=20)
        self._setup_settings_tab()

    def _apply_settings(self):
        """Apply user settings from config"""
        theme = self.config.get('appearance_mode')
        ctk.set_appearance_mode(theme)

    def _setup_settings_tab(self):
        """Create functional settings tab"""
        ctk.CTkLabel(self.settings_tab, text='Theme:').pack(pady=5)
        self.theme_var = ctk.StringVar(value=self.config.get('appearance_mode'))
        theme_dropdown = ctk.CTkComboBox(
            self.settings_tab, values=['dark', 'light', 'system'],
            variable=self.theme_var, command=self._change_theme
        )
        theme_dropdown.pack(pady=5)

    def _change_theme(self, new_theme):
        """Change and save theme"""
        ctk.set_appearance_mode(new_theme)
        self.config.set('appearance_mode', new_theme)
