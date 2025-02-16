from sale.pos import Pos
from storage.wms import Wms
from admin.dashboard import Dashboard
from web.expressapi import ExpressApi


class Core:
    """Main class of project (CORE)"""

    def __init__(self):
        self.pos = Pos()
        self.wms = Wms()
        self.dashboard = Dashboard()
        self.api = ExpressApi()

