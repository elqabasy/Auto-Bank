import sys, os
from home import Home
from settings import Settings
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFontDatabase, QIcon, QPalette, QColor, Qt
from constants import REG_VALUES_APP_NAME, REG_VALUES_ORGANIZATION, BASE_DIR

def Main():
    App = QApplication([])

    # Style
    APP_SETTINGS = Settings("Mahros AL-Qabasy", "Auto-Bank")

    App.setApplicationVersion("1.0.0")
    App.setWindowIcon(QIcon(":/design/icons/.ico/app.ico"))
    App.setApplicationName(APP_SETTINGS.load_setting("Name", "Auto-Bank"))
    # App.setApplicationVersion(APP_SETTINGS.load_setting("Version", "1.0.0"))
    
    # fonts 
    fonts_dir = os.path.join(BASE_DIR, "design/fonts/")
    for font in os.listdir(fonts_dir):
        if font.endswith('.ttf'):
            font_path = os.path.join(fonts_dir, font)
            QFontDatabase.addApplicationFont(font_path)

    # show
    HOME = Home()
    HOME.showMaximized()

    # run
    sys.exit(App.exec())

if __name__ == "__main__":
    try:
        Main()
    except Exception as Error:
        print(Error)