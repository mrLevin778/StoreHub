from time import sleep
from core.main import Core


class StoreHub:
    """Class for run project"""

    def __init__(self):
        self.core = Core()

    def run_store_hub(self):
        """Main loop"""
        while True:
            print('started')
            self.core.run_app()
            sleep(1)
            print('bye')
            break


if __name__ == '__main__':
    sh = StoreHub()
    sh.run_store_hub()
