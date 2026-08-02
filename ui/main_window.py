from PySide6.QtWidgets import QMainWindow

from .ui_files.UI_display import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self)->None:

        super().__init__()
        self.setupUi(self)

