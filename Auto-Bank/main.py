# External
import sys, os

# PySide6
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon, QFontDatabase

# My Packages
from windows import Home
from auth import authenticate
from settings import Settings, SC
from utils.package import showErrorMessage, changeLanguageToArabic

# method
def Main():
    
    # LANGUAGE
    changeLanguageToArabic()

    # APP
    App = QApplication([])

    # # INFO
    App.setWindowIcon(QIcon(SC.get(Settings.App.Info.Icon.value)))
    App.setApplicationName(SC.get(Settings.App.Info.Name.value, "Auto-Bank"))
    App.setApplicationVersion(SC.get(Settings.App.Info.Version.value, "9.9.9"))

    # STYLE - ADD FONTS TO QFontDatabase
    [QFontDatabase.addApplicationFont(FontPath) for FontPath in [os.path.join(SC.get(Settings.Design.Fonts.Path.value, "design/fonts"), font) for font in os.listdir(SC.get(Settings.Design.Fonts.Path.value, "design/fonts")) if font.endswith(SC.get(Settings.Design.Fonts.Extension.value))]]

    # SHOW
    HOME = Home()
    HOME.showMaximized()

    # RUN
    sys.exit(App.exec())

if __name__ == "__main__":
    try:
        if authenticate() == True:
            Main()
        else:
            showErrorMessage("هذا التطبيق غير مصر له بالعمل علي هذا الجهاز، يجب تفعيله من خلال المطور، لذا قم بالضغط علي نعم لنسخ الكود الذي سيتم ارياله للمطور.")
    except Exception as Error:
        pass