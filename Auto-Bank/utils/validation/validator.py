# Builtin

# PySide6
from PySide6 import QtCore, QtGui


# ArabicValidator
class ArabicValidator(QtGui.QValidator):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Arabic Unicode range: U+0600 to U+06FF
        self.arabic_regex = QtCore.QRegularExpression("[\u0600-\u06FF]+")

    def validate(self, input, pos):
        if self.arabic_regex.match(input).hasMatch():
            return QtGui.QValidator.State.Acceptable, input, pos
        elif input == "":
            return QtGui.QValidator.State.Intermediate, input, pos
        else:
            return QtGui.QValidator.State.Invalid, input, pos


# AccountNumberValidator
class AccountNumberValidator(QtGui.QValidator):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Define the regular expression for the validator
        self.regex = QtCore.QRegularExpression("\\d{1,16}")
        # self.regex = QtCore.QRegularExpression("[0-9-]+")
        self.validator = QtGui.QRegularExpressionValidator(self.regex, parent)

    def validate(self, input, pos):
        return self.validator.validate(input, pos)

    def fixup(self, input):
        return self.validator.fixup(input)
