import sys
from sale.pos import Pos
from storage.wms import Wms
from admin.dashboard import Dashboard
from web.expressapi import ExpressApi
from core.authsystem import AuthSystem
from core.login import Login
from core.config import Config


class Core:
    """Main class of project (CORE)"""

    def __init__(self):
        self.pos = Pos()
        self.wms = Wms()
        self.dashboard = Dashboard()
        self.api = ExpressApi()
        self.login_form = Login()

    def run_app(self):
        print('LOGIN FORM')
        self.login_form.protocol('WM_DELETE_WINDOW', self.on_close)
        self.login_form.mainloop()

    @staticmethod
    def on_close():
        print('Closing the app...')
        sys.exit(0)



