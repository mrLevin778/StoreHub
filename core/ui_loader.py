import logging

from PySide6.QtWidgets import QWidget, QDialog, QMainWindow, QLayout
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


class UiLoader:
    """Class for load .ui files"""

    @staticmethod
    def load_ui(file_path: str, parent: QWidget = None) -> None | QDialog | QMainWindow | QWidget:
        logging.info(f'Load UI from {file_path}')
        ui_file = QFile(file_path)
        if not ui_file.exists():
            raise FileNotFoundError(f'{file_path} is not found.')
        if not ui_file.open(QFile.ReadOnly):
            raise IOError(f'{file_path} is not open.')
        loader = QUiLoader()
        try:
            widget = loader.load(ui_file, parent)
        except Exception as e:
            logging.error(f'Error loading file {file_path}: {e}')
            raise RuntimeError
        finally:
            ui_file.close()
        if not widget:
            raise RuntimeError(f'Loading error with {file_path}')
        if isinstance(widget, QMainWindow):
            central_widget = widget.findChild(QWidget, 'centralWidget')
            if central_widget:
                widget.setCentralWidget(central_widget)
            else:
                raise ValueError('centralWidget not found in QMainWindow.')
        elif isinstance(widget, QDialog):
            layout = widget.layout()
            if not layout or not isinstance(layout, QLayout):
                raise ValueError
            widget.setLayout(layout)
        return widget
