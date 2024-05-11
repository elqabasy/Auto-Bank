# Builtin
from settings import Settings, SC

# PySide6
from PySide6 import QtGui
from PySide6.QtCore import QEvent, Qt
from PySide6.QtWidgets import QDialog, QMessageBox

# Me
from design.py.profile import Ui_DialogMe

# ProfileInfo
class ProfileInfo(QDialog, Ui_DialogMe):
    Message = QMessageBox
    def __init__(self):
        super(ProfileInfo, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, True)
        self.initUI()
    
    def initUI(self):
        self.lineEditGithub.setText(SC.get(Settings.App.Info.Repo.value, "github.com\\elqabasy\\Auto-Bank"))
        self.lineEditEmail.setText(SC.get(Settings.App.Author.Mail.value, "mahros.elqabasy@hotmail.com"))
        self.lineEditPhone.setText(SC.get(Settings.App.Author.Phone.value, "+20 1015888272"))
        self.lineEditAuthor.setText(SC.get(Settings.App.Author.Name.value, "Mahros AL-Qabasy"))
        self.lineEditVersion.setText(SC.get(Settings.App.Info.Version.value, "9.9.9"))

    def initDefaults(self):
        pass
    

    def closeEvent(self, event:QEvent):
        event.accept()

    def keyPressEvent(self, event:QtGui.QKeyEvent): 
        if event.key() == Qt.Key.Key_Escape or Qt.Key.Key_F1:
            self.close()