# Built in
import os
from enum import Enum

# PySide6
from PySide6.QtCore import QSettings

# Me


class SettingsController:
    def __init__(self, organization, application):
        self.settings = QSettings(organization, application)

    def set(self, key, value):
        self.settings.setValue(key, value)

    def get(self, key, default_value=None):
        return self.settings.value(key, default_value)

    def remove_setting(self, key):
        self.settings.remove(key)


# INSTANCE.
SC: SettingsController = SettingsController("Mahros AL-Qabasy", "Auto-Bank")

# SETTINGS
BASE_DIRECTORY = os.path.curdir


class Settings:
    class App:
        class Info(Enum):
            Name = "App/Info/Name"
            Icon = "App/Info/Icon"
            Repo = "App/Info/Repo"
            Version = "App/Info/Version"
            Language = "App/Info/Version"
            Serial = "App/Info/Version"
            Encoding = "App/Info/Encoding"

        class Author(Enum):
            Name = "App/Author/Name"
            Mail = "App/Author/Mail"
            Phone = "App/Author/Phone"

    class Currency(Enum):
        Name = "Currency/Name"
        Code = "Currency/Code"
        Icon = "Currency/Icon"
        Language = "Currency/Language"

    class Defaults:
        class Transaction(Enum):
            CreditorName = "Defaults/Transaction/CreditorName"
            CreditorBankName = "Defaults/Transaction/CreditorBankName"
            CreditorBankCode = "Defaults/Transaction/CreditorBankCode"
            CreditorAccountNumber = "Defaults/Transaction/"
            "CreditorAccountNumber"

        class Session(Enum):
            Username = "Defaults/Session/Username"
            Password = "Defaults/Session/Password"

    class Database(Enum):
        Name = "Database/Name"
        Path = "Database/Path"

    class Design:
        class Fonts(Enum):
            Path = "Design/Fonts/Path"
            Extension = "Design/Fonts/Extension"

    class PackageSettings:
        class Keyboard:
            class Layouts(Enum):
                Arabic = {
                    # Arabic Layouts
                    "0x0401": "Arabic (101)",
                    "0x0c01": "Arabic (101) - Egypt",
                    "0x3c01": "Arabic (101) - Bahrain",
                    "0xc01": "Arabic (102) AZERTY - Egypt",
                    "0x1401": "Arabic (102) AZERTY - Algeria",
                }

                English = {
                    # English Layouts
                    "0x409": "English",
                    "0x419": "Russian",
                }
