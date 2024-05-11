# Builtin
from settings import Settings, SC

# PySide6
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QDialog, QMessageBox

# Me
from design import Ui_DialogSplash

# ProfileInfo
class SplashScreen(QDialog, Ui_DialogSplash):
    Message = QMessageBox
    def __init__(self):
        super(SplashScreen, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        