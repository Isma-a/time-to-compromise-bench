# A QLineEdit with a show/hide button and clear button enabled

from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QLineEdit

from resources import resources_rc # import icons

class PasswordLineEdit(QLineEdit):

    def __init__(self, /, parent=None) ->None:

        super().__init__(parent)

        self.eyeOpenIcon: str = ':/icons/eye_view.png' # Show icon
        self.eyeCloseIcon: str = ':/icons/eye_hide.png' # Hide icon

        self.actPasswordVisibility = QAction(QIcon(self.eyeOpenIcon), '', self) # Create action for password visibility
        self.addAction(self.actPasswordVisibility, QLineEdit.ActionPosition.TrailingPosition) # Add the action to the QLineEdit

        self.actPasswordVisibility.triggered.connect(self.changePasswordVisibility) # Add connection

        self.setClearButtonEnabled(True) # Activate clear button from the QLineEdit

        self.changePasswordVisibility() # Set the password visibility off


    def changePasswordVisibility(self)->None:
        '''

        :return: 
        '''

        if self.echoMode() == QLineEdit.EchoMode.Normal:
            self.setEchoMode(QLineEdit.EchoMode.Password)
            self.actPasswordVisibility.setIcon(QIcon(self.eyeCloseIcon))
        else:
            self.setEchoMode(QLineEdit.EchoMode.Normal)
            self.actPasswordVisibility.setIcon(QIcon(self.eyeOpenIcon))