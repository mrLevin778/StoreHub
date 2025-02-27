from core.main import Core


class StoreHub:
    """Class for run project"""

    def __init__(self):
        self.core = Core()

    def run_store_hub(self):
        """Main loop"""
        while True:
            self.core.run_app()


if __name__ == '__main__':
    sh = StoreHub()
    sh.run_store_hub()
