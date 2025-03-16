import logging

from PySide6.QtWidgets import QWidget, QDialog, QMainWindow, QLayout
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QObject


class UiLoader:
    """Class for load .ui files"""

    @staticmethod
    def load_ui(file_path: str, parent: QWidget = None) -> QWidget:
        print(f'Load UI from {file_path}')
        ui_file = QFile(file_path)
        if not ui_file.exists():
            raise FileNotFoundError(f'{file_path} is not found.')
        if not ui_file.open(QFile.ReadOnly):
            raise IOError(f'{file_path} is not open.')
        loader = QUiLoader()
        widget = loader.load(ui_file, parent)
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
            if layout and isinstance(layout, QLayout):
                widget.setLayout(layout)
            else:
                print(f'QDialog not have layout')
        return widget
