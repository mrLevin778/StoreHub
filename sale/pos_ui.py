import customtkinter as ctk
from tkinter import ttk
from core.config import Config


class PosUI(ctk.CTk):
    """Main window for POS with tabs"""

    def __init__(self):
        super().__init__()
        self.config = Config()
        self._apply_settings()
        self.title('Point-Of-Sale')
        self.attributes('-fullscreen', True)
        #self.geometry('800x600')
        # creating tab view
        self.tab_view = ctk.CTkTabview(self)
        self.tab_view.pack(fill='both', expand=True, padx=10, pady=10)
        # adding tabs
        self.sales_tab = self.tab_view.add('Sales')
        self.history_tab = self.tab_view.add('Sales History')
        self.return_tab = self.tab_view.add('Return')
        self.customers_tab = self.tab_view.add('Customers')
        # creating sales tab
        self._create_sales_tab()
        # placeholder labels
        ctk.CTkLabel(self.history_tab, text='Sales history data here').pack(pady=20)
        ctk.CTkLabel(self.return_tab, text='Sales return here').pack(pady=20)
        ctk.CTkLabel(self.customers_tab, text='Customers here').pack(pady=20)

    def _create_sales_tab(self):
        """Creates the sales tab content"""
        self.sales_tab.grid_columnconfigure(1, weight=1)
        self.sales_tab.grid_rowconfigure(1, weight=1)
        # top panel
        self.top_frame = ctk.CTkFrame(self.sales_tab)
        self.top_frame.grid(row=0, column=0, columnspan=2, sticky='ew', padx=10, pady=10)
        self.barcode_entry = ctk.CTkEntry(self.top_frame, placeholder_text='Barcode')
        self.barcode_entry.pack(side='left', padx=10)
        self.cashier_label = ctk.CTkLabel(self.top_frame, text='Cashier: Bill Clinton')
        self.cashier_label.pack(side='right', padx=10)
        # left side (goods list)
        self.left_frame = ctk.CTkFrame(self.sales_tab)
        self.left_frame.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
        self.product_list = ttk.Treeview(self.left_frame, columns=('#', 'Product Name', 'Q-ty', 'Price per unit', 'Total price'), show='headings')
        self.product_list.pack(fill='both', expand=True)
        # set columns
        self.product_list.heading('#', text='#')
        self.product_list.heading('Product Name', text='Product Name')
        self.product_list.heading('Q-ty', text='Q-ty')
        self.product_list.heading('Price per unit', text='Price per unit')
        self.product_list.heading('Total price', text='Total price')
        # right side (pay)
        self.right_frame = ctk.CTkFrame(self.sales_tab)
        self.right_frame.grid(row=1, column=1, sticky='nsew', padx=10, pady=10)
        self.total_label = ctk.CTkLabel(self.right_frame, text='Total price: 0.00 $')
        self.total_label.pack(pady=10)
        self.cash_button = ctk.CTkButton(self.right_frame, text='Cash')
        self.cash_button.pack(pady=5)
        self.card_button = ctk.CTkButton(self.right_frame, text='Card')
        self.card_button.pack(pady=5)
        self.cancel_button = ctk.CTkButton(self.right_frame, text='Cancel sale', fg_color='red')
        self.cancel_button.pack(pady=10)
        # bottom side (print sale)
        self.bottom_frame = ctk.CTkFrame(self.sales_tab)
        self.bottom_frame.grid(row=2, column=0, columnspan=2, sticky='ew', padx=10, pady=10)
        self.print_button = ctk.CTkButton(self.bottom_frame, text='Print sale', fg_color='green')
        self.print_button.pack(side='right', padx=10)

    def _apply_settings(self):
        """Apply user settings from config"""
        theme = self.config.get('appearance_mode')
        ctk.set_appearance_mode(theme)
