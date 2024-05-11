# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_DialogMe(object):
    def setupUi(self, DialogMe):
        if not DialogMe.objectName():
            DialogMe.setObjectName(u"DialogMe")
        DialogMe.setWindowModality(Qt.WindowModality.WindowModal)
        DialogMe.resize(400, 309)
        font = QFont()
        font.setFamilies([u"Cairo"])
        font.setPointSize(12)
        DialogMe.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/.png/icons8-info-96.png", QSize(), QIcon.Normal, QIcon.Off)
        DialogMe.setWindowIcon(icon)
        self.gridLayout = QGridLayout(DialogMe)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_11, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(8, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(8, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(DialogMe)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 35))
        font1 = QFont()
        font1.setFamilies([u"Cairo"])
        font1.setPointSize(22)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.line = QFrame(DialogMe)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(35, 16777215))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(DialogMe)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 35))

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_3 = QLabel(DialogMe)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 35))

        self.verticalLayout.addWidget(self.label_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_4 = QLabel(DialogMe)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 35))

        self.verticalLayout.addWidget(self.label_4)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.label_5 = QLabel(DialogMe)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 35))

        self.verticalLayout.addWidget(self.label_5)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.label_6 = QLabel(DialogMe)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 35))

        self.verticalLayout.addWidget(self.label_6)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_9)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEditVersion = QLineEdit(DialogMe)
        self.lineEditVersion.setObjectName(u"lineEditVersion")
        self.lineEditVersion.setMinimumSize(QSize(0, 35))
        self.lineEditVersion.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.lineEditVersion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEditVersion.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.lineEditVersion)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.lineEditAuthor = QLineEdit(DialogMe)
        self.lineEditAuthor.setObjectName(u"lineEditAuthor")
        self.lineEditAuthor.setMinimumSize(QSize(0, 35))
        self.lineEditAuthor.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEditAuthor.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.lineEditAuthor)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.lineEditEmail = QLineEdit(DialogMe)
        self.lineEditEmail.setObjectName(u"lineEditEmail")
        self.lineEditEmail.setMinimumSize(QSize(0, 35))
        self.lineEditEmail.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEditEmail.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.lineEditEmail)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.lineEditPhone = QLineEdit(DialogMe)
        self.lineEditPhone.setObjectName(u"lineEditPhone")
        self.lineEditPhone.setMinimumSize(QSize(0, 35))
        self.lineEditPhone.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEditPhone.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.lineEditPhone)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_8)

        self.lineEditGithub = QLineEdit(DialogMe)
        self.lineEditGithub.setObjectName(u"lineEditGithub")
        self.lineEditGithub.setMinimumSize(QSize(0, 35))
        self.lineEditGithub.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.lineEditGithub.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEditGithub.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.lineEditGithub)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_10)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout_3.setStretch(2, 5)

        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)


        self.retranslateUi(DialogMe)

        QMetaObject.connectSlotsByName(DialogMe)
    # setupUi

    def retranslateUi(self, DialogMe):
        DialogMe.setWindowTitle(QCoreApplication.translate("DialogMe", u"Info", None))
        self.label.setText(QCoreApplication.translate("DialogMe", u"Auto Bank", None))
        self.label_2.setText(QCoreApplication.translate("DialogMe", u"Version", None))
        self.label_3.setText(QCoreApplication.translate("DialogMe", u"Author", None))
        self.label_4.setText(QCoreApplication.translate("DialogMe", u"Email", None))
        self.label_5.setText(QCoreApplication.translate("DialogMe", u"Phone", None))
        self.label_6.setText(QCoreApplication.translate("DialogMe", u"Github", None))
        self.lineEditVersion.setText(QCoreApplication.translate("DialogMe", u"0.0.0", None))
        self.lineEditVersion.setPlaceholderText(QCoreApplication.translate("DialogMe", u"Version", None))
        self.lineEditAuthor.setText(QCoreApplication.translate("DialogMe", u"Mahros AL-Qabasy", None))
        self.lineEditAuthor.setPlaceholderText(QCoreApplication.translate("DialogMe", u"Author", None))
        self.lineEditEmail.setText(QCoreApplication.translate("DialogMe", u"mahros.elqabasy@hotmail.com", None))
        self.lineEditEmail.setPlaceholderText(QCoreApplication.translate("DialogMe", u"Email", None))
        self.lineEditPhone.setText(QCoreApplication.translate("DialogMe", u"+20 1015888272", None))
        self.lineEditPhone.setPlaceholderText(QCoreApplication.translate("DialogMe", u"Phone", None))
        self.lineEditGithub.setText(QCoreApplication.translate("DialogMe", u"https://github.com/elqabasy/Auto-Bank/releases/tag/Basic-Features", None))
        self.lineEditGithub.setPlaceholderText(QCoreApplication.translate("DialogMe", u"Github", None))
    # retranslateUi

