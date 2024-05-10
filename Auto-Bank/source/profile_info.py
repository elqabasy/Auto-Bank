from .settings import Settings
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QDialog, QMessageBox

from design.py.profile import Ui_DialogMe

class ProfileInfo(QDialog, Ui_DialogMe):
    Message = QMessageBox
    timer = QtCore.QTimer()
    _settings = Settings("Mahros AL-Qabasy", "Auto-Bank")
    def __init__(self):
        super(ProfileInfo,self).__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowType.WindowCloseButtonHint, True)

    def initDefaults(self):
        pass

    def closeEvent(self, event):
        pass

    def keyPressEvent(self, event:QtGui.QKeyEvent): 
        if event.key() == QtCore.Qt.Key.Key_Escape or QtCore.Qt.Key.Key_F1:
            self.close()