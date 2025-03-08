from PySide6.QtWidgets import QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


class UiLoader:
    """Class for load .ui files"""

    @staticmethod
    def load_ui(file_path: str, parent: QWidget = None):
        print(f'Load UI from {file_path}')
        ui_file = QFile(file_path)
        if not ui_file.exists():
            raise FileNotFoundError(f'{file_path} is not found.')
        if not ui_file.open(QFile.ReadOnly):
            raise IOError(f'{file_path} is not open.')
        loader = QUiLoader()
        widget = loader.load(ui_file, parent)
        ui_file.close()
        if widget is None:
            raise RuntimeError(f'Loading error with {file_path}')
        return widget
