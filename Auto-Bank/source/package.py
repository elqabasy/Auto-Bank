# packages
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QApplication
import hashlib, num2words, pyperclip, datetime, tempfile, os

# code
class NumberScrapping:
    def numberToEgyptionCurrency(number):
        return str(num2words.num2words(number, False, lang='ar', to="currency", currency="EGP"))
    
def MD5(text:str):
    text_bytes = text.encode('utf-8')
    hasher = hashlib.md5()
    hasher.update(text_bytes)
    return hasher.hexdigest()


def showErrorMessage(text:str, title:str="Error - Activation", informative_text:str=""):
    app = QApplication([])
    Message = QMessageBox(QMessageBox.Icon.Critical, title, text, QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Yes)
    Message.setInformativeText(informative_text)
    Message.exec_()
    if Message == QMessageBox.StandardButton.Yes:
        pyperclip.copy(str())
    app.exit()
    # sys.exit(app.exec())

def showInfoMessage(text:str, title:str="Info", informative_text:str=""):
    app = QApplication([])
    Message = QMessageBox(QMessageBox.Icon.Information, title, text, QMessageBox.StandardButton.Ok)
    Message.setInformativeText(informative_text)
    Message.exec_()
    app.exit()

def showWarningMessage(text:str, title:str="Warning", informative_text:str=""):
    app = QApplication([])
    Message = QMessageBox(QMessageBox.Icon.Warning, title, text, QMessageBox.StandardButton.Ok)
    Message.setInformativeText(informative_text)
    Message.exec_()
    app.exit()


def ShowOtherWindow(self, Window:object):
    try:
        self.NEWWindow = Window()
        self.NEWWindow.show()
    except Exception as Error:
        showErrorMessage(Error, "Show window")


def TakeScreenShot(self):
    try:
        temp_dir = tempfile.mkdtemp()
        filename = os.path.join(temp_dir, f"Backup_{datetime.datetime.today().strftime('%d-%m-%Y %H_%M_%S')}_screen.png")
        filename = os.path.abspath(filename)

        # temp_file = os.path.join(filename, 'screenshot.png')

        # path = temp_file
        self.grab().save(filename, "png", 100)
        if os.path.isfile(filename):
            os.startfile(filename)
    except Exception as Error:
        showErrorMessage(Error, "Screenshot Error")
    # Cleanup the temporary file when done
    # temp_dir.cleanup()

