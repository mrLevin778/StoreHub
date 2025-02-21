import sys
from sale.pos import Pos
from storage.wms import Wms
from admin.dashboard import Dashboard
from web.expressapi import ExpressApi
from core.authsystem import AuthSystem
from core.login import Login


class Core:
    """Main class of project (CORE)"""

    def __init__(self):
        self.pos = Pos()
        self.wms = Wms()
        self.dashboard = Dashboard()
        self.api = ExpressApi()

    def run_app(self):
        print('LOGIN FORM')
        login_form = Login()
        login_form.protocol('WM_DELETE_WINDOW', self.on_close)
        login_form.mainloop()

    @staticmethod
    def on_close():
        print('Closing the app...')
        sys.exit(0)



