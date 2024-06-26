# Builtin
import datetime
import hashlib
import os
import platform
import sys
import tempfile
from ctypes import WinDLL

import num2words
import pyperclip
from keyboard import press, release

# PySide6
from PySide6.QtWidgets import QApplication, QMessageBox

# Me
from settings.settings import SC, Settings


class NumberScrapping:
    def numberToEgyptionCurrency(number):
        return str(
            num2words.num2words(
                number,
                False,
                lang=SC.get(Settings.Currency.Language.value, "ar"),
                to="currency",
                currency=SC.get(Settings.Currency.Code.value, "EGP"),
            )
        )


def MD5(text: str):
    return hashlib.md5(
        text.encode(SC.get(Settings.Currency.Code, "utf-8")), usedforsecurity=0
    ).hexdigest()


def showErrorMessage(text, title="Error", informative_text=""):
    app = QApplication([])
    Message = QMessageBox(
        QMessageBox.Icon.Critical,
        title,
        text,
        QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Yes,
    )
    Message.setInformativeText(informative_text)
    Message.exec_()
    if Message == QMessageBox.StandardButton.Yes:
        pyperclip.copy(str())
    sys.exit(app.exec())


def showInfoMessage(text: str, title: str = "Info", informative_text=""):
    app = QApplication([])
    Message = QMessageBox(
        QMessageBox.Icon.Information, title, text,
        QMessageBox.StandardButton.Ok
    )
    Message.setInformativeText(informative_text)
    Message.exec_()
    sys.exit(app.exec())


def showWarningMessage(text: str, title: str = "Warning", informative_text=""):
    app = QApplication([])
    Message = QMessageBox(
        QMessageBox.Icon.Warning, title, text, QMessageBox.StandardButton.Ok
    )
    Message.setInformativeText(informative_text)
    Message.exec_()
    sys.exit(app.exec())


def ShowOtherWindow(self, Window: object):
    try:
        self.NEWWindow = Window()
        self.NEWWindow.show()
    except Exception as Error:
        showErrorMessage(Error, "Show window")


def TakeScreenShot(self):
    try:
        temp_dir = tempfile.mkdtemp()
        filename = os.path.join(
            temp_dir,
            f"Backup_{datetime.datetime.today().strftime(
                '%d-%m-%Y %H_%M_%S'
                )}_screen.png",
        )
        filename = os.path.abspath(filename)
        self.grab().save(filename, "png", 100)
        if os.path.isfile(filename):
            os.startfile(filename)
    except Exception as Error:
        showErrorMessage(Error, "Screenshot Error")


def convert_to_english_numerals(hindi_arabic_numerals):
    # Mapping of Hindi-Arabic numerals to English
    numeral_mapping = {
        "\u0660": "0",
        "\u0661": "1",
        "\u0662": "2",
        "\u0663": "3",
        "\u0664": "4",
        "\u0665": "5",
        "\u0666": "6",
        "\u0667": "7",
        "\u0668": "8",
        "\u0669": "9",
    }
    return "".join(numeral_mapping.get(char, char) for char in
                   hindi_arabic_numerals)


def get_current_keyboard_language_code():
    # Load the user32 DLL
    user32 = WinDLL("user32", use_last_error=True)

    # Get the foreground window
    curr_window = user32.GetForegroundWindow()

    # Get the thread ID of the foreground window
    thread_id = user32.GetWindowThreadProcessId(curr_window, 0)

    # Get the keyboard layout ID
    klid = user32.GetKeyboardLayout(thread_id)

    # Extract the language ID from the keyboard layout ID
    language_id = klid & (2**16 - 1)

    # Convert the language ID from decimal to hexadecimal
    language_id_hex = hex(language_id)

    return language_id_hex


def changeLanguageToArabic():
    try:
        current = get_current_keyboard_language_code()
        list_ = Settings.PackageSettings.Keyboard.Layouts.Arabic.value
        if current not in list_:
            press("alt")
            press("shift")
            release("shift")
            release("alt")
    except Exception as Error:
        showErrorMessage(Error)


def isWindow11():
    version = platform.version()
    # Windows 11 typically starts with "10.0.22000" or higher
    if version < "10.0.22000":
        return True
    return False
