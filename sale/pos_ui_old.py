import platform
import customtkinter as ctk
from core.config import Config


class PosUI(ctk.CTk):
    """Main window for POS with tabs"""

    def __init__(self):
        super().__init__()
        self.config = Config()
        self._apply_settings()
        self.title('Point-Of-Sale')
        #self.attributes('-fullscreen', True)
        self._set_fullscreen_without_taskbar()  # set fullscreen mode
        self.resizable(False, False)  # not resizable
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

    def _set_fullscreen_without_taskbar(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        if platform.system() == 'Windows':
            taskbar_height = 40
            self.geometry(f'{screen_width}x{screen_height - taskbar_height}')
        elif platform.system() == 'Darwin':  # MacOS
            menu_bar_height = 22
            self.geometry(f'{screen_width}x{screen_height - menu_bar_height}')
        else:
            self.attributes('-fullscreen', True)  # for other systems


    def _create_sales_tab(self):
        """Creates the sales tab content"""
        # top panel
        self.top_frame = ctk.CTkFrame(self.sales_tab)
        self.top_frame.pack(side='top', fill='x', padx=10, pady=10)
        self.barcode_entry = ctk.CTkEntry(self.top_frame, placeholder_text='Barcode')
        self.barcode_entry.pack(side='left', padx=10, expand=True)
        self.search_entry = ctk.CTkEntry(self.top_frame, placeholder_text='Search for name')
        self.search_entry.pack(side='left', padx=10, expand=True)
        self.cashier_label = ctk.CTkLabel(self.top_frame, text='Cashier: Bill Clinton')
        self.cashier_label.pack(side='right', padx=10)
        # left side (goods list)
        self.left_frame = ctk.CTkFrame(self.sales_tab)
        self.left_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        # goods frame
        self.goods_frame = ctk.CTkFrame(self.left_frame, height=200)
        self.goods_frame.pack(side='top', fill='both', expand=True)
        # canvas for scrollable content
        self.canvas = ctk.CTkCanvas(self.goods_frame)
        self.canvas.pack(side='left', fill='both', expand=True)
        # scrollbar
        self.scrollbar = ctk.CTkScrollbar(self.goods_frame, command=self.canvas.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox('all')))
        # frame inside canvas
        self.scrollable_frame = ctk.CTkFrame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor='nw')
        # add headers
        headers = ['№', 'Product Name', 'Q-ty', 'Price per unit', 'Total price']
        for i, header in enumerate(headers):
            header_label = ctk.CTkLabel(self.scrollable_frame, text=header)
            header_label.grid(row=0, column=i, padx=5, pady=5)
        # add items (example)
        items = [
            [1, 'Coca-Cola Classic, 1.75L, Some Description', 2, 10.0, 20.0],
            [2, 'Product 2', 1, 15.0, 15.0],
            [3, 'Product 1', 3, 5.0, 15.0],
        ]
        for row, item in enumerate(items):
            for col, value in enumerate(item):
                item_label = ctk.CTkLabel(self.scrollable_frame, text=str(value))
                item_label.grid(row=row + 1, column=col, padx=5, pady=5)
        # add total price
        total_price_row = len(items) + 1  # next available row
        total_price_label = ctk.CTkLabel(self.scrollable_frame, text='500.00')  # set this to real value!!!
        total_price_label.grid(row=total_price_row, column=4, padx=5, pady=5)
        # right side (pay)
        self.right_frame = ctk.CTkFrame(self.sales_tab)
        self.right_frame.pack(side='right', fill='both', padx=10, pady=10)
        self.cash_button = ctk.CTkButton(self.right_frame, text='Cash')
        self.cash_button.pack(pady=5)
        self.card_button = ctk.CTkButton(self.right_frame, text='Card')
        self.card_button.pack(pady=5)
        self.cancel_button = ctk.CTkButton(self.right_frame, text='Cancel sale', fg_color='red')
        self.cancel_button.pack(pady=10)
        # bottom side (print sale)
        self.bottom_frame = ctk.CTkFrame(self.sales_tab)
        self.bottom_frame.pack(side='bottom', fill='x', padx=10, pady=10)
        self.print_button = ctk.CTkButton(self.bottom_frame, text='Print sale', fg_color='green')
        self.print_button.pack(side='left', padx=10)

    def _apply_settings(self):
        """Apply user settings from config"""
        theme = self.config.get('appearance_mode')
        ctk.set_appearance_mode(theme)
