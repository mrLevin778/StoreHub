import sys
from sale.pos_ui import PosUI
from storage.wms_ui import WmsUI
from admin.dashboard import Dashboard
from web.expressapi import ExpressApi
from core.authsystem import AuthSystem
from core.login import Login
from core.config import Config


class Core:
    """Main class of project (CORE)"""

    def __init__(self):
        #self.pos_ui = PosUI()
        #self.wms_ui = WmsUI()
        #self.dashboard = Dashboard()
        self.api = ExpressApi()
        self.login_form = Login()
        self.config = Config()

    def run_app(self):
        self.config.load_default_config()
        if hasattr(self, 'login_form') and self.login_form.winfo_exists():
            self.login_form.protocol('WM_DELETE_WINDOW', self.on_close)
        self.login_form.mainloop()

    def on_close(self):
        """Close login window correct"""
        self.login_form.destroy()
        sys.exit(0)



