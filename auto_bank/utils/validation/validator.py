import sys
from PySide6.QtCore import QRegularExpression, Qt
from PySide6.QtWidgets import QApplication, QLineEdit
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression, QObject, QEvent
from PySide6.QtGui import QRegularExpressionValidator, QValidator




class ArabicValidator(QValidator):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Arabic Unicode range: U+0600 to U+06FF
        self.arabic_regex = QRegularExpression("[\u0600-\u06FF]+")

    def validate(self, input, pos):
        if self.arabic_regex.match(input).hasMatch():
            return QValidator.State.Acceptable, input, pos
        elif input == "":
            return QValidator.State.Intermediate, input, pos
        else:
            return QValidator.State.Invalid, input, pos

class AccountNumberValidator(QValidator):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Define the regular expression for the validator
        self.regex = QRegularExpression("\\d{1,16}")
        # self.regex = QRegularExpression("[0-9-]+")
        self.validator = QRegularExpressionValidator(self.regex, parent)


    # def validate_text(self):
    #     text = self.line_edit.text()
    #     state, _, _ = self.validator.validate(text, 0)
    #     if state != QValidator.Acceptable:
    #         self.line_edit.setText(self.default_value)        

    def validate(self, input, pos):
        return self.validator.validate(input, pos)

    def fixup(self, input):
        return self.validator.fixup(input)



def revalidateQLineEdit(self, lineEdit:QLineEdit):
    # Get the current text from the line edit
    text = lineEdit.text()
    # Perform validation
    state, _text, _pos = lineEdit.validator().validate(text, 0)
    if state != QValidator.State.Acceptable:
        lineEdit.validator().fixup(text)