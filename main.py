import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from ui.UI_display import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self)->None:

        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = MainWindow()
    myWindow.show()

    sys.exit(app.exec())

