# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QProgressBar, QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_DialogSplash(object):
    def setupUi(self, DialogSplash):
        if not DialogSplash.objectName():
            DialogSplash.setObjectName(u"DialogSplash")
        DialogSplash.resize(425, 132)
        DialogSplash.setMinimumSize(QSize(425, 132))
        DialogSplash.setMaximumSize(QSize(425, 132))
        font = QFont()
        font.setFamilies([u"Cairo"])
        font.setPointSize(10)
        font.setBold(True)
        DialogSplash.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/.ico/app.ico", QSize(), QIcon.Normal, QIcon.Off)
        DialogSplash.setWindowIcon(icon)
        DialogSplash.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gridLayout = QGridLayout(DialogSplash)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(15, -1, 15, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelTitle = QLabel(DialogSplash)
        self.labelTitle.setObjectName(u"labelTitle")
        font1 = QFont()
        font1.setFamilies([u"Cairo"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.labelTitle.setFont(font1)
        self.labelTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelTitle)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, -1, 15, -1)
        self.progressBar = QProgressBar(DialogSplash)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setFont(font)
        self.progressBar.setValue(90)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.verticalLayout.addWidget(self.progressBar)

        self.label = QLabel(DialogSplash)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2.setStretch(0, 5)

        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(DialogSplash)

        QMetaObject.connectSlotsByName(DialogSplash)
    # setupUi

    def retranslateUi(self, DialogSplash):
        DialogSplash.setWindowTitle(QCoreApplication.translate("DialogSplash", u"Loading...", None))
        self.labelTitle.setText(QCoreApplication.translate("DialogSplash", u"\u0628\u0631\u0646\u0627\u0645\u062c \u0627\u0644\u0628\u0646\u0643 .. \u062c\u0627\u0631\u064a \u0627\u0644\u062a\u062d\u0645\u064a\u0644", None))
        self.label.setText(QCoreApplication.translate("DialogSplash", u"\u064a\u062a\u0645 \u062a\u062d\u0645\u064a\u0644 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0627\u0644\u0627\u0646\u060c \u0627\u0646\u062a\u0638\u0631 \u0642\u0644\u064a\u0644\u0627", None))
    # retranslateUi

