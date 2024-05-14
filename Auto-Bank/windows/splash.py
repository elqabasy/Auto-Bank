# Builtin

# PySide6
# Me
from design import Ui_DialogSplash
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QMessageBox


# ProfileInfo
class SplashScreen(QDialog, Ui_DialogSplash):
    Message = QMessageBox

    def __init__(self):
        super(SplashScreen, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
