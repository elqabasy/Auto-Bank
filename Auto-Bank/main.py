# External
import sys, os

# My Packages
from source.home import Home
from source.settings import Settings
from source.auth import authenticate, get_machine_uuid
# from .auth import get_machine_uuid
from source.constants import BASE_DIR
from source.package import showErrorMessage

# PySide6
from PySide6 import QtWidgets, QtGui

# method
def Main():
    # App
    App = QtWidgets.QApplication([])

    # Info
    App.setApplicationVersion("1.0.0")
    APP_SETTINGS = Settings("Mahros AL-Qabasy", "Auto-Bank")
    App.setWindowIcon(QtGui.QIcon(":/design/icons/.ico/app.ico"))
    App.setApplicationName(APP_SETTINGS.load_setting("Name", "Auto-Bank"))
    
    # fonts 
    fonts_dir = os.path.join(BASE_DIR, "design/fonts/")
    for font in os.listdir(fonts_dir):
        if font.endswith('.ttf'):
            font_path = os.path.join(fonts_dir, font)
            QtGui.QFontDatabase.addApplicationFont(font_path)

    # show
    HOME = Home()
    HOME.showMaximized()

    # run
    sys.exit(App.exec())

if __name__ == "__main__":
    try:
        if authenticate() == True:
            Main()
        else:
            showErrorMessage("هذا التطبيق غير مصر له بالعمل علي هذا الجهاز، يجب تفعيله من خلال المطور، لذا قم بالضغط علي نعم لنسخ الكود الذي سيتم ارياله للمطور.")
            # show_critical_error()

    except Exception as Error:
        print(Error)
        raise Error