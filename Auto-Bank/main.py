# External
import sys, os

# PySide6
from PySide6.QtGui import QIcon, QFontDatabase
from PySide6.QtCore import Signal, QObject, QTimer
from PySide6.QtWidgets import QApplication, QProgressBar

# My Packages
from auth import authenticate
from settings import Settings, SC
from windows import Home, SplashScreen
from utils.package import showErrorMessage, changeLanguageToArabic

# Signals
class Signals(QObject):
    settingsLoaded = Signal()   # 50%
    homeLoaded = Signal()       # 50%
    finished = Signal()         # 100%

# method
def loadSettings(App:QApplication, signals:Signals):
    # LANGUAGE
    changeLanguageToArabic()

    # INFO
    App.setWindowIcon(QIcon(SC.get(Settings.App.Info.Icon.value)))
    App.setApplicationName(SC.get(Settings.App.Info.Name.value, "Auto-Bank"))
    App.setApplicationVersion(SC.get(Settings.App.Info.Version.value, "9.9.9"))

    # STYLE - ADD FONTS TO QFontDatabase
    [QFontDatabase.addApplicationFont(FontPath) for FontPath in [os.path.join(SC.get(Settings.Design.Fonts.Path.value, "design/fonts"), font) for font in os.listdir(SC.get(Settings.Design.Fonts.Path.value, "design/fonts")) if font.endswith(SC.get(Settings.Design.Fonts.Extension.value))]]

    # Emit signal when settings are loaded
    signals.settingsLoaded.emit()

def updateProgressBar(progressBar:QProgressBar, value):
    progressBar.setValue(value)

def Main():
    # APP
    App = QApplication([])
    
    # Signals
    signals = Signals()

    # SPLASH
    SPLASH = SplashScreen()
    SPLASH.show()

    # Progress Bar
    progressBar = SPLASH.progressBar
    progressBar.setValue(0)

    # Connect signals to slots
    signals.homeLoaded.connect(lambda: QTimer.singleShot(600, lambda: updateProgressBar(progressBar, 100)))
    signals.settingsLoaded.connect(lambda: QTimer.singleShot(600, lambda: updateProgressBar(progressBar, 60)))

    # Load settings
    loadSettings(App, signals)

    # SHOW
    HOME = Home()
    # if HOME.setupUi:
    QTimer.singleShot(600, signals.homeLoaded.emit)

    # Close splash and show HOME after a delay
    signals.homeLoaded.connect(lambda: QTimer.singleShot(1000, SPLASH.close))
    signals.homeLoaded.connect(lambda: QTimer.singleShot(1000, HOME.showMaximized))

    # RUN
    sys.exit(App.exec())

if __name__ == "__main__":
    try:
        if authenticate() == True:
            Main()
        else:
            showErrorMessage("هذا التطبيق غير مصر له بالعمل علي هذا الجهاز، يجب تفعيله من خلال المطور، لذا قم بالضغط علي نعم لنسخ الكود الذي سيتم ارياله للمطور.")
    except Exception as Error:
        showErrorMessage(Error)
