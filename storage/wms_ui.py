import customtkinter as ctk
from core.config import Config


class WmsUI(ctk.CTk):
    """Main window for WMS with tabs"""

    def __init__(self):
        super().__init__()
        self.config = Config()
        self._apply_settings()
        self.title('Warehouse Management System')
        self.geometry('800x600')
        # creating tab view
        self.tab_view = ctk.CTkTabview(self)
        self.tab_view.pack(fill='both', expand=True, padx=10, pady=10)
        # adding tabs
        self.store_tab = self.tab_view.add('Storage')
        self.receipt_tab = self.tab_view.add('Receipts')
        self.shipment_tab = self.tab_view.add('Shipments')
        self.inventory_tab = self.tab_view.add('Inventory')
        # placeholder labels
        ctk.CTkLabel(self.store_tab, text='Storage here').pack(pady=20)
        ctk.CTkLabel(self.receipt_tab, text='Receipts here').pack(pady=20)
        ctk.CTkLabel(self.shipment_tab, text='Shipments here').pack(pady=20)
        ctk.CTkLabel(self.inventory_tab, text='Inventory here').pack(pady=20)

    def _apply_settings(self):
        """Apply user settings from config"""
        theme = self.config.get('appearance_mode')
        ctk.set_appearance_mode(theme)