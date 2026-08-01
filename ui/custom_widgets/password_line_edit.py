from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QLineEdit

from resources import resources_rc

class PasswordLineEdit(QLineEdit):

    def __init__(self, /, parent=None) ->None:

        super().__init__(parent)

        self.eyeOpenIcon: str = ':/icons/eye_view.png'
        self.eyeCloseIcon: str = ':/ressources/icons/eye_hide.png'

        self.changePasswordVisibility()

        self.actPasswordVisibility = QAction(QIcon(self.eyeOpenIcon), '', self)
        self.actClear = QAction(QIcon(), '', self)

        self.addAction(self.actPasswordVisibility, QLineEdit.ActionPosition.TrailingPosition)

        self.actPasswordVisibility.triggered.connect(self.changePasswordVisibility)

        self.setClearButtonEnabled(True)


    def changePasswordVisibility(self)->None:

        if self.echoMode() == QLineEdit.EchoMode.Normal:
            self.setEchoMode(QLineEdit.EchoMode.Password)
            self.actPasswordVisibility.setIcon(QIcon(self.eyeCloseIcon))
        else:
            self.setEchoMode(QLineEdit.EchoMode.Normal)
            self.actPasswordVisibility.setIcon(QIcon(self.eyeOpenIcon))