# External
import os
import sys

# PySide6
from PySide6.QtGui import QIcon, QFontDatabase
from PySide6.QtCore import Signal, QObject, QTimer
from PySide6.QtWidgets import QApplication, QProgressBar

# My Packages
# from auth import authenticate
from windows.home import Home
from windows.splash import SplashScreen
from settings.settings import Settings, SC
from utils.package import showErrorMessage, isWindow11


class Signals(QObject):
    settingsLoaded = Signal()   # 50%
    homeLoaded = Signal()       # 50%
    finished = Signal()         # 100%


def loadSettings(App: QApplication, signals: Signals):
    # LANGUAGE
    # changeLanguageToArabic()

    # INFO
    App.setWindowIcon(QIcon(SC.get(Settings.App.Info.Icon.value)))
    App.setApplicationName(SC.get(Settings.App.Info.Name.value, "Auto-Bank"))
    App.setApplicationVersion(SC.get(Settings.App.Info.Version.value, "9.9.9"))

    # STYLE - ADD FONTS TO QFontDatabase
    FONTS_DIR = os.path.abspath(
        os.path.join(
            os.path.curdir,
            SC.get(Settings.Design.Fonts.Path.value, "design/fonts")
            )
        )
    for font in os.listdir(FONTS_DIR):
        if font.endswith(".ttf"):
            FontPath = os.path.join(FONTS_DIR, font)
            QFontDatabase.addApplicationFont(FontPath)

    # Emit signal when settings are loaded
    signals.settingsLoaded.emit()


def updateProgressBar(progressBar: QProgressBar, value):
    progressBar.setValue(value)


def Main():
    # APP
    App = QApplication([])

    if not isWindow11():
        pass
        # App.setPalette(create_beautiful_dark_palette())

    # Signals
    signals = Signals()

    # SPLASH
    SPLASH = SplashScreen()
    SPLASH.show()

    # Progress Bar
    progressBar = SPLASH.progressBar
    progressBar.setValue(0)

    # Connect signals to slots
    signals.homeLoaded.connect(
        lambda: QTimer.singleShot(
            600,
            lambda: updateProgressBar(progressBar, 100)
            )
        )
    signals.settingsLoaded.connect(
        lambda: QTimer.singleShot(
            600,
            lambda: updateProgressBar(progressBar, 60)
            )
        )

    # Load settings
    loadSettings(App, signals)

    # SHOW
    HOME = Home()
    # if HOME.setupUi:
    QTimer.singleShot(600, signals.homeLoaded.emit)

    # Close splash and show HOME after a delay
    signals.homeLoaded.connect(
        lambda: QTimer.singleShot(
            1000,
            SPLASH.close
            )
        )
    signals.homeLoaded.connect(
        lambda: QTimer.singleShot(
            1000,
            HOME.showMaximized
            )
        )

    # RUN
    sys.exit(App.exec())


if __name__ == "__main__":
    try:
        Main()
    except Exception as Error:
        showErrorMessage(Error)
