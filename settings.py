from PySide6.QtCore import QSettings

class Settings:
    def __init__(self, organization, application):
        self.settings = QSettings(organization, application)

    def save_setting(self, key, value):
        self.settings.setValue(key, value)

    def load_setting(self, key, default_value=None):
        return self.settings.value(key, default_value)

    def remove_setting(self, key):
        self.settings.remove(key)

# if __name__ == "__main__":
#     settings_manager = Settings('AL-Qabasy', 'Bank-Automation')
    # settings_manager.save_setting('username', 'user123')