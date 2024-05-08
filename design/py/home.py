# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QComboBox,
    QDateEdit, QDateTimeEdit, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QSplitter, QStackedWidget, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindowHome(object):
    def setupUi(self, MainWindowHome):
        if not MainWindowHome.objectName():
            MainWindowHome.setObjectName(u"MainWindowHome")
        MainWindowHome.setWindowModality(Qt.WindowModality.ApplicationModal)
        MainWindowHome.resize(900, 637)
        icon = QIcon()
        icon.addFile(u":/icons/.ico/app.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindowHome.setWindowIcon(icon)
        MainWindowHome.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.centralwidget = QWidget(MainWindowHome)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_10 = QGridLayout(self.centralwidget)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 9, 9, 0)
        self.radioButtonAccountStatus = QRadioButton(self.centralwidget)
        self.radioButtonAccountStatus.setObjectName(u"radioButtonAccountStatus")
        self.radioButtonAccountStatus.setEnabled(True)
        font = QFont()
        font.setFamilies([u"Cairo"])
        font.setPointSize(9)
        font.setBold(False)
        self.radioButtonAccountStatus.setFont(font)
        self.radioButtonAccountStatus.setCheckable(True)
        self.radioButtonAccountStatus.setChecked(False)

        self.horizontalLayout.addWidget(self.radioButtonAccountStatus)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.labelHomeTitle = QLabel(self.centralwidget)
        self.labelHomeTitle.setObjectName(u"labelHomeTitle")
        font1 = QFont()
        font1.setFamilies([u"Cairo"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelHomeTitle.setFont(font1)

        self.horizontalLayout.addWidget(self.labelHomeTitle)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButtonRefresh = QPushButton(self.centralwidget)
        self.pushButtonRefresh.setObjectName(u"pushButtonRefresh")
        font2 = QFont()
        font2.setFamilies([u"Cairo"])
        font2.setPointSize(9)
        font2.setItalic(True)
        self.pushButtonRefresh.setFont(font2)
        icon1 = QIcon(QIcon.fromTheme(u"emblem-synchronized"))
        self.pushButtonRefresh.setIcon(icon1)

        self.horizontalLayout.addWidget(self.pushButtonRefresh)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font3 = QFont()
        font3.setFamilies([u"Cairo"])
        font3.setPointSize(9)
        self.stackedWidget.setFont(font3)
        self.stackedWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.stackedWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.stackedWidget.setLineWidth(1)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidgetHome = QTabWidget(self.page)
        self.tabWidgetHome.setObjectName(u"tabWidgetHome")
        self.tabWidgetHome.setEnabled(True)
        self.tabWidgetHome.setFont(font3)
        self.tabWidgetHome.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.tabWidgetHome.setDocumentMode(False)
        self.tabWidgetHome.setTabBarAutoHide(False)
        self.tabData = QWidget()
        self.tabData.setObjectName(u"tabData")
        self.gridLayout_11 = QGridLayout(self.tabData)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.groupBox_4 = QGroupBox(self.tabData)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font3)
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.splitter = QSplitter(self.groupBox_4)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setHandleWidth(2)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.horizontalLayout_15 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_15.setSpacing(11)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.pushButtonAdd = QPushButton(self.layoutWidget)
        self.pushButtonAdd.setObjectName(u"pushButtonAdd")
        self.pushButtonAdd.setMinimumSize(QSize(0, 35))
        self.pushButtonAdd.setFont(font3)
        self.pushButtonAdd.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon2 = QIcon(QIcon.fromTheme(u"list-add"))
        self.pushButtonAdd.setIcon(icon2)

        self.horizontalLayout_15.addWidget(self.pushButtonAdd)

        self.pushButtonDelete = QPushButton(self.layoutWidget)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")
        self.pushButtonDelete.setMinimumSize(QSize(0, 35))
        self.pushButtonDelete.setFont(font3)
        self.pushButtonDelete.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon3 = QIcon(QIcon.fromTheme(u"list-remove"))
        self.pushButtonDelete.setIcon(icon3)

        self.horizontalLayout_15.addWidget(self.pushButtonDelete)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget2 = QWidget(self.splitter)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.horizontalLayout_14 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_14.setSpacing(9)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(5, 0, 5, 0)
        self.labelMoney = QLabel(self.layoutWidget2)
        self.labelMoney.setObjectName(u"labelMoney")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMoney.sizePolicy().hasHeightForWidth())
        self.labelMoney.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamilies([u"Cairo"])
        font4.setPointSize(9)
        font4.setBold(True)
        self.labelMoney.setFont(font4)
        self.labelMoney.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelMoney.setWordWrap(True)

        self.horizontalLayout_14.addWidget(self.labelMoney)

        self.spinBoxTransactionAmount = QSpinBox(self.layoutWidget2)
        self.spinBoxTransactionAmount.setObjectName(u"spinBoxTransactionAmount")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.spinBoxTransactionAmount.sizePolicy().hasHeightForWidth())
        self.spinBoxTransactionAmount.setSizePolicy(sizePolicy1)
        self.spinBoxTransactionAmount.setMinimumSize(QSize(0, 35))
        self.spinBoxTransactionAmount.setFont(font3)
        self.spinBoxTransactionAmount.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.spinBoxTransactionAmount.setAccelerated(True)
        self.spinBoxTransactionAmount.setMinimum(0)
        self.spinBoxTransactionAmount.setMaximum(1500000)
        self.spinBoxTransactionAmount.setSingleStep(1000)
        self.spinBoxTransactionAmount.setValue(0)
        self.spinBoxTransactionAmount.setDisplayIntegerBase(10)

        self.horizontalLayout_14.addWidget(self.spinBoxTransactionAmount)

        self.label_10 = QLabel(self.layoutWidget2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setFont(font3)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_10)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 1)
        self.splitter.addWidget(self.layoutWidget2)
        self.layoutWidget3 = QWidget(self.splitter)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.horizontalLayout_13 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.comboBoxBankNumber = QComboBox(self.layoutWidget3)
        self.comboBoxBankNumber.setObjectName(u"comboBoxBankNumber")
        self.comboBoxBankNumber.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.comboBoxBankNumber.sizePolicy().hasHeightForWidth())
        self.comboBoxBankNumber.setSizePolicy(sizePolicy1)
        self.comboBoxBankNumber.setMinimumSize(QSize(0, 35))
        self.comboBoxBankNumber.setMaximumSize(QSize(108, 16777215))
        self.comboBoxBankNumber.setFont(font3)
        self.comboBoxBankNumber.setEditable(False)

        self.horizontalLayout_13.addWidget(self.comboBoxBankNumber)

        self.comboBoxBankName = QComboBox(self.layoutWidget3)
        self.comboBoxBankName.setObjectName(u"comboBoxBankName")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBoxBankName.sizePolicy().hasHeightForWidth())
        self.comboBoxBankName.setSizePolicy(sizePolicy2)
        self.comboBoxBankName.setMinimumSize(QSize(0, 35))
        self.comboBoxBankName.setFont(font3)
        self.comboBoxBankName.setEditable(False)

        self.horizontalLayout_13.addWidget(self.comboBoxBankName)

        self.splitter.addWidget(self.layoutWidget3)
        self.layoutWidget4 = QWidget(self.splitter)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.horizontalLayout_12 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lineEditAccountCreatorAccountNumber = QLineEdit(self.layoutWidget4)
        self.lineEditAccountCreatorAccountNumber.setObjectName(u"lineEditAccountCreatorAccountNumber")
        sizePolicy1.setHeightForWidth(self.lineEditAccountCreatorAccountNumber.sizePolicy().hasHeightForWidth())
        self.lineEditAccountCreatorAccountNumber.setSizePolicy(sizePolicy1)
        self.lineEditAccountCreatorAccountNumber.setMinimumSize(QSize(0, 35))
        self.lineEditAccountCreatorAccountNumber.setFont(font3)

        self.horizontalLayout_12.addWidget(self.lineEditAccountCreatorAccountNumber)

        self.lineEditCreatorName = QLineEdit(self.layoutWidget4)
        self.lineEditCreatorName.setObjectName(u"lineEditCreatorName")
        sizePolicy1.setHeightForWidth(self.lineEditCreatorName.sizePolicy().hasHeightForWidth())
        self.lineEditCreatorName.setSizePolicy(sizePolicy1)
        self.lineEditCreatorName.setMinimumSize(QSize(0, 35))
        self.lineEditCreatorName.setFont(font3)

        self.horizontalLayout_12.addWidget(self.lineEditCreatorName)

        self.splitter.addWidget(self.layoutWidget4)

        self.gridLayout_4.addWidget(self.splitter, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.tabData)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setFont(font3)
        self.gridLayout_9 = QGridLayout(self.groupBox_5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.tableWidgetData = QTableWidget(self.groupBox_5)
        if (self.tableWidgetData.columnCount() < 5):
            self.tableWidgetData.setColumnCount(5)
        font5 = QFont()
        font5.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font5);
        self.tableWidgetData.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font5);
        self.tableWidgetData.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font5);
        self.tableWidgetData.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font5);
        self.tableWidgetData.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.tableWidgetData.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidgetData.setObjectName(u"tableWidgetData")
        self.tableWidgetData.setEnabled(True)
        self.tableWidgetData.setFont(font3)
        self.tableWidgetData.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidgetData.setAlternatingRowColors(True)
        self.tableWidgetData.setRowCount(0)
        self.tableWidgetData.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetData.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidgetData.horizontalHeader().setDefaultSectionSize(350)
        self.tableWidgetData.horizontalHeader().setHighlightSections(True)
        self.tableWidgetData.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidgetData.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetData.verticalHeader().setDefaultSectionSize(50)

        self.gridLayout_9.addWidget(self.tableWidgetData, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_5, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButtonNextLevel = QPushButton(self.tabData)
        self.pushButtonNextLevel.setObjectName(u"pushButtonNextLevel")
        self.pushButtonNextLevel.setEnabled(True)
        self.pushButtonNextLevel.setFont(font3)
        self.pushButtonNextLevel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon4 = QIcon(QIcon.fromTheme(u"go-next"))
        self.pushButtonNextLevel.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.pushButtonNextLevel)


        self.gridLayout_11.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.tabWidgetHome.addTab(self.tabData, "")
        self.tabUploadData = QWidget()
        self.tabUploadData.setObjectName(u"tabUploadData")
        self.gridLayout_15 = QGridLayout(self.tabUploadData)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label = QLabel(self.tabUploadData)
        self.label.setObjectName(u"label")
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color:red")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_19.addWidget(self.label)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.groupBox_10 = QGroupBox(self.tabUploadData)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_3 = QGridLayout(self.groupBox_10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widgetWebPage = QWebEngineView(self.groupBox_10)
        self.widgetWebPage.setObjectName(u"widgetWebPage")
        self.widgetWebPage.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout_3.addWidget(self.widgetWebPage, 0, 0, 1, 1)

        self.labelWebsiteLoadPrpgress = QLabel(self.groupBox_10)
        self.labelWebsiteLoadPrpgress.setObjectName(u"labelWebsiteLoadPrpgress")
        font6 = QFont()
        font6.setFamilies([u"Cairo"])
        font6.setPointSize(12)
        font6.setBold(True)
        self.labelWebsiteLoadPrpgress.setFont(font6)
        self.labelWebsiteLoadPrpgress.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.labelWebsiteLoadPrpgress, 1, 0, 1, 1)


        self.horizontalLayout_10.addWidget(self.groupBox_10)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.groupBox_12 = QGroupBox(self.tabUploadData)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout = QGridLayout(self.groupBox_12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_14 = QLabel(self.groupBox_12)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignTop)
        self.label_14.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.label_14)

        self.line = QFrame(self.groupBox_12)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(12)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_19 = QLabel(self.groupBox_12)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_12.addWidget(self.label_19)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_12)

        self.label_18 = QLabel(self.groupBox_12)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFrameShape(QFrame.Shape.NoFrame)
        self.label_18.setScaledContents(False)

        self.verticalLayout_12.addWidget(self.label_18)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_13)

        self.label_20 = QLabel(self.groupBox_12)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_12.addWidget(self.label_20)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_14)

        self.label_21 = QLabel(self.groupBox_12)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_12.addWidget(self.label_21)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_15)

        self.label_22 = QLabel(self.groupBox_12)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_12.addWidget(self.label_22)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_16)

        self.label_6 = QLabel(self.groupBox_12)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_12.addWidget(self.label_6)


        self.horizontalLayout_7.addLayout(self.verticalLayout_12)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.lineEditUsername = QLineEdit(self.groupBox_12)
        self.lineEditUsername.setObjectName(u"lineEditUsername")
        self.lineEditUsername.setMinimumSize(QSize(0, 32))
        self.lineEditUsername.setFrame(False)
        self.lineEditUsername.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.lineEditUsername)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer)

        self.lineEditPassword = QLineEdit(self.groupBox_12)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setMinimumSize(QSize(0, 32))
        self.lineEditPassword.setMaxLength(32767)
        self.lineEditPassword.setFrame(False)
        self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEditPassword.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEditPassword.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)
        self.lineEditPassword.setClearButtonEnabled(False)

        self.verticalLayout_15.addWidget(self.lineEditPassword)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_3)

        self.lineEditDefaultAccountNumber = QLineEdit(self.groupBox_12)
        self.lineEditDefaultAccountNumber.setObjectName(u"lineEditDefaultAccountNumber")
        self.lineEditDefaultAccountNumber.setMinimumSize(QSize(0, 32))
        self.lineEditDefaultAccountNumber.setFrame(False)
        self.lineEditDefaultAccountNumber.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.lineEditDefaultAccountNumber)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_4)

        self.lineEditDefaultBankCode = QLineEdit(self.groupBox_12)
        self.lineEditDefaultBankCode.setObjectName(u"lineEditDefaultBankCode")
        self.lineEditDefaultBankCode.setMinimumSize(QSize(0, 32))
        self.lineEditDefaultBankCode.setFrame(False)
        self.lineEditDefaultBankCode.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.lineEditDefaultBankCode)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_5)

        self.lineEditDefaultCustomerName = QLineEdit(self.groupBox_12)
        self.lineEditDefaultCustomerName.setObjectName(u"lineEditDefaultCustomerName")
        self.lineEditDefaultCustomerName.setMinimumSize(QSize(0, 32))
        self.lineEditDefaultCustomerName.setFrame(False)
        self.lineEditDefaultCustomerName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.lineEditDefaultCustomerName)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_6)

        self.lineEditXLSXPath = QLineEdit(self.groupBox_12)
        self.lineEditXLSXPath.setObjectName(u"lineEditXLSXPath")
        self.lineEditXLSXPath.setMinimumSize(QSize(0, 35))
        self.lineEditXLSXPath.setFont(font)
        self.lineEditXLSXPath.setFrame(False)
        self.lineEditXLSXPath.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEditXLSXPath.setReadOnly(True)
        self.lineEditXLSXPath.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)

        self.verticalLayout_15.addWidget(self.lineEditXLSXPath)


        self.horizontalLayout_7.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.pushButtonCopyUsername = QPushButton(self.groupBox_12)
        self.pushButtonCopyUsername.setObjectName(u"pushButtonCopyUsername")
        self.pushButtonCopyUsername.setFont(font)
        icon5 = QIcon(QIcon.fromTheme(u"edit-copy"))
        self.pushButtonCopyUsername.setIcon(icon5)

        self.verticalLayout_16.addWidget(self.pushButtonCopyUsername)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_7)

        self.pushButtonCopyPassword = QPushButton(self.groupBox_12)
        self.pushButtonCopyPassword.setObjectName(u"pushButtonCopyPassword")
        self.pushButtonCopyPassword.setFont(font)
        self.pushButtonCopyPassword.setIcon(icon5)

        self.verticalLayout_16.addWidget(self.pushButtonCopyPassword)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_8)

        self.pushButtonCopyAccountNumber = QPushButton(self.groupBox_12)
        self.pushButtonCopyAccountNumber.setObjectName(u"pushButtonCopyAccountNumber")
        self.pushButtonCopyAccountNumber.setFont(font)
        self.pushButtonCopyAccountNumber.setIcon(icon5)

        self.verticalLayout_16.addWidget(self.pushButtonCopyAccountNumber)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_9)

        self.pushButtonCopyBankCode = QPushButton(self.groupBox_12)
        self.pushButtonCopyBankCode.setObjectName(u"pushButtonCopyBankCode")
        self.pushButtonCopyBankCode.setFont(font)
        self.pushButtonCopyBankCode.setIcon(icon5)

        self.verticalLayout_16.addWidget(self.pushButtonCopyBankCode)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_10)

        self.pushButtonCopyCustomerName = QPushButton(self.groupBox_12)
        self.pushButtonCopyCustomerName.setObjectName(u"pushButtonCopyCustomerName")
        self.pushButtonCopyCustomerName.setFont(font)
        self.pushButtonCopyCustomerName.setIcon(icon5)

        self.verticalLayout_16.addWidget(self.pushButtonCopyCustomerName)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_11)

        self.pushButtonCopyPath = QPushButton(self.groupBox_12)
        self.pushButtonCopyPath.setObjectName(u"pushButtonCopyPath")
        self.pushButtonCopyPath.setFont(font)
        self.pushButtonCopyPath.setIcon(icon5)

        self.verticalLayout_16.addWidget(self.pushButtonCopyPath)


        self.horizontalLayout_7.addLayout(self.verticalLayout_16)


        self.verticalLayout_13.addLayout(self.horizontalLayout_7)

        self.verticalLayout_13.setStretch(0, 10)

        self.gridLayout.addLayout(self.verticalLayout_13, 0, 0, 1, 1)


        self.verticalLayout_17.addWidget(self.groupBox_12)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_2)

        self.verticalLayout_17.setStretch(0, 1)

        self.horizontalLayout_10.addLayout(self.verticalLayout_17)

        self.horizontalLayout_10.setStretch(0, 5)

        self.verticalLayout_19.addLayout(self.horizontalLayout_10)

        self.verticalLayout_19.setStretch(1, 10)

        self.gridLayout_15.addLayout(self.verticalLayout_19, 0, 0, 1, 1)

        self.tabWidgetHome.addTab(self.tabUploadData, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_6 = QGridLayout(self.tab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_8 = QGroupBox(self.groupBox_2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setEnabled(False)
        self.gridLayout_13 = QGridLayout(self.groupBox_8)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.groupBox_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_5.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.pushButton_4 = QPushButton(self.groupBox_8)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_6.addWidget(self.pushButton_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.verticalLayout_5.setStretch(0, 10)

        self.gridLayout_13.addLayout(self.verticalLayout_5, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_8, 1, 2, 1, 1)

        self.groupBox_9 = QGroupBox(self.groupBox_2)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setEnabled(False)
        self.gridLayout_18 = QGridLayout(self.groupBox_9)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.groupBox_9)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_8.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.label_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.pushButton_6 = QPushButton(self.groupBox_9)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_9.addWidget(self.pushButton_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.verticalLayout_7.setStretch(0, 10)

        self.gridLayout_18.addLayout(self.verticalLayout_7, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_9, 2, 2, 1, 1)

        self.groupBox = QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_7 = QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dateEditReportFrom = QDateEdit(self.groupBox)
        self.dateEditReportFrom.setObjectName(u"dateEditReportFrom")
        self.dateEditReportFrom.setMinimumSize(QSize(0, 35))
        self.dateEditReportFrom.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.dateEditReportFrom.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.dateEditReportFrom.setProperty("showGroupSeparator", False)
        self.dateEditReportFrom.setCurrentSection(QDateTimeEdit.Section.DaySection)
        self.dateEditReportFrom.setCalendarPopup(False)
        self.dateEditReportFrom.setDate(QDate(2000, 1, 1))

        self.horizontalLayout_3.addWidget(self.dateEditReportFrom)

        self.dateEditReportTo = QDateEdit(self.groupBox)
        self.dateEditReportTo.setObjectName(u"dateEditReportTo")
        self.dateEditReportTo.setMinimumSize(QSize(0, 35))
        self.dateEditReportTo.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.dateEditReportTo.setCurrentSection(QDateTimeEdit.Section.DaySection)
        self.dateEditReportTo.setCalendarPopup(False)

        self.horizontalLayout_3.addWidget(self.dateEditReportTo)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.pushButtonGetDatedReport = QPushButton(self.groupBox)
        self.pushButtonGetDatedReport.setObjectName(u"pushButtonGetDatedReport")
        self.pushButtonGetDatedReport.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_3.addWidget(self.pushButtonGetDatedReport)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2.setStretch(0, 10)

        self.gridLayout_7.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setEnabled(False)
        self.gridLayout_8 = QGridLayout(self.groupBox_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_3.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_4.addWidget(self.pushButton_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalLayout_3.setStretch(0, 10)

        self.gridLayout_8.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_3, 0, 2, 1, 1)

        self.groupBox_7 = QGroupBox(self.groupBox_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setEnabled(False)
        self.gridLayout_12 = QGridLayout(self.groupBox_7)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.groupBox_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_4.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.pushButton_3 = QPushButton(self.groupBox_7)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_5.addWidget(self.pushButton_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.verticalLayout_4.setStretch(0, 10)

        self.gridLayout_12.addLayout(self.verticalLayout_4, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_7, 1, 0, 1, 1)

        self.groupBox_13 = QGroupBox(self.groupBox_2)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setEnabled(False)
        self.gridLayout_19 = QGridLayout(self.groupBox_13)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_9 = QLabel(self.groupBox_13)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_9.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_10)

        self.pushButton_7 = QPushButton(self.groupBox_13)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_11.addWidget(self.pushButton_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.verticalLayout_8.setStretch(0, 10)

        self.gridLayout_19.addLayout(self.verticalLayout_8, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_13, 2, 0, 1, 1)

        self.groupBox_14 = QGroupBox(self.groupBox_2)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setEnabled(False)
        self.gridLayout_20 = QGridLayout(self.groupBox_14)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_11 = QLabel(self.groupBox_14)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_11.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.label_11)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_11)

        self.pushButton_8 = QPushButton(self.groupBox_14)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_19.addWidget(self.pushButton_8)


        self.verticalLayout_9.addLayout(self.horizontalLayout_19)

        self.verticalLayout_9.setStretch(0, 10)

        self.gridLayout_20.addLayout(self.verticalLayout_9, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_14, 0, 1, 1, 1)

        self.groupBox_15 = QGroupBox(self.groupBox_2)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setEnabled(False)
        self.gridLayout_21 = QGridLayout(self.groupBox_15)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_12 = QLabel(self.groupBox_15)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_12.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.label_12)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_12)

        self.pushButton_9 = QPushButton(self.groupBox_15)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_20.addWidget(self.pushButton_9)


        self.verticalLayout_10.addLayout(self.horizontalLayout_20)

        self.verticalLayout_10.setStretch(0, 10)

        self.gridLayout_21.addLayout(self.verticalLayout_10, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_15, 1, 1, 1, 1)

        self.groupBox_16 = QGroupBox(self.groupBox_2)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setEnabled(False)
        self.gridLayout_22 = QGridLayout(self.groupBox_16)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_13 = QLabel(self.groupBox_16)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_13.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_13)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_13)

        self.pushButton_10 = QPushButton(self.groupBox_16)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_21.addWidget(self.pushButton_10)


        self.verticalLayout_11.addLayout(self.horizontalLayout_21)

        self.verticalLayout_11.setStretch(0, 10)

        self.gridLayout_22.addLayout(self.verticalLayout_11, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_16, 2, 1, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.tabWidgetHome.addTab(self.tab, "")

        self.gridLayout_2.addWidget(self.tabWidgetHome, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.gridLayout_10.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindowHome.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindowHome)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        MainWindowHome.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.lineEditCreatorName, self.lineEditAccountCreatorAccountNumber)
        QWidget.setTabOrder(self.lineEditAccountCreatorAccountNumber, self.comboBoxBankName)
        QWidget.setTabOrder(self.comboBoxBankName, self.spinBoxTransactionAmount)
        QWidget.setTabOrder(self.spinBoxTransactionAmount, self.pushButtonAdd)
        QWidget.setTabOrder(self.pushButtonAdd, self.pushButtonNextLevel)
        QWidget.setTabOrder(self.pushButtonNextLevel, self.pushButtonRefresh)
        QWidget.setTabOrder(self.pushButtonRefresh, self.tableWidgetData)
        QWidget.setTabOrder(self.tableWidgetData, self.comboBoxBankNumber)
        QWidget.setTabOrder(self.comboBoxBankNumber, self.pushButtonDelete)
        QWidget.setTabOrder(self.pushButtonDelete, self.tabWidgetHome)
        QWidget.setTabOrder(self.tabWidgetHome, self.radioButtonAccountStatus)

        self.retranslateUi(MainWindowHome)

        self.tabWidgetHome.setCurrentIndex(0)
        self.pushButtonAdd.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindowHome)
    # setupUi

    def retranslateUi(self, MainWindowHome):
        MainWindowHome.setWindowTitle(QCoreApplication.translate("MainWindowHome", u"\u0627\u0644\u0631\u0626\u064a\u0633\u064a\u0629 | \u0628\u0631\u0646\u0627\u0645\u062c \u0627\u0644\u0628\u0646\u0643", None))
#if QT_CONFIG(statustip)
        MainWindowHome.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.radioButtonAccountStatus.setText(QCoreApplication.translate("MainWindowHome", u"\u063a\u064a\u0631 \u0645\u062a\u0635\u0644", None))
        self.labelHomeTitle.setText(QCoreApplication.translate("MainWindowHome", u"\u0627\u0644\u0631\u0626\u064a\u0633\u064a\u0629", None))
        self.pushButtonRefresh.setText(QCoreApplication.translate("MainWindowHome", u"\u062a\u062d\u062f\u064a\u062b", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindowHome", u"\u0627\u062f\u062e\u0627\u0644 \u0645\u0639\u0627\u0645\u0644\u0647 \u062c\u062f\u064a\u062f\u0647", None))
        self.pushButtonAdd.setText(QCoreApplication.translate("MainWindowHome", u"\u0627\u0636\u0627\u0641\u0647", None))
#if QT_CONFIG(shortcut)
        self.pushButtonAdd.setShortcut(QCoreApplication.translate("MainWindowHome", u"Ctrl+Shift+A", None))
#endif // QT_CONFIG(shortcut)
        self.pushButtonDelete.setText(QCoreApplication.translate("MainWindowHome", u"\u062d\u0630\u0641", None))
#if QT_CONFIG(shortcut)
        self.pushButtonDelete.setShortcut(QCoreApplication.translate("MainWindowHome", u"Ctrl+Shift+D", None))
#endif // QT_CONFIG(shortcut)
        self.labelMoney.setText(QCoreApplication.translate("MainWindowHome", u"\u0635\u0641\u0631", None))
        self.spinBoxTransactionAmount.setSpecialValueText("")
        self.spinBoxTransactionAmount.setSuffix("")
        self.spinBoxTransactionAmount.setPrefix(QCoreApplication.translate("MainWindowHome", u"\u062c.\u0645 ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindowHome", u"\u0627\u0644\u0645\u0628\u0644\u063a", None))
        self.comboBoxBankNumber.setCurrentText("")
        self.comboBoxBankNumber.setPlaceholderText(QCoreApplication.translate("MainWindowHome", u"\u0627\u0646\u062a\u0638\u0631 \u0643\u0648\u062f \u0627\u0644\u0628\u0646\u0643", None))
        self.comboBoxBankName.setCurrentText("")
        self.comboBoxBankName.setPlaceholderText(QCoreApplication.translate("MainWindowHome", u"\u0627\u062f\u062e\u0644 \u0627\u0633\u0645 \u0627\u0644\u0628\u0646\u0643", None))
        self.lineEditAccountCreatorAccountNumber.setPlaceholderText(QCoreApplication.translate("MainWindowHome", u"\u0627\u062f\u062e\u0644 \u0631\u0642\u0645 \u0627\u0644\u062d\u0633\u0627\u0628 \u0627\u0644\u0630\u064a \u0633\u062a\u0645 \u062a\u062d\u0648\u064a\u0644 \u0644\u0647 \u0627\u0644\u0645\u0628\u0644\u063a", None))
        self.lineEditCreatorName.setPlaceholderText(QCoreApplication.translate("MainWindowHome", u"\u0627\u062f\u062e\u0644 \u0627\u0633\u0645 \u0627\u0644\u0639\u0645\u064a\u0644 \u0627\u0644\u0630\u064a \u0633\u064a\u062a\u0645 \u062a\u062d\u0648\u064a\u0644 \u0644\u0647 \u0627\u0644\u0645\u0628\u0644\u063a", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindowHome", u"\u062c\u062f\u0648\u0644 \u0627\u0644\u0645\u0639\u0627\u0645\u0644\u0627\u062a \u0627\u0644\u062a\u064a \u0633\u064a\u062a\u0645 \u0631\u0641\u0639\u0647\u0627", None))
        ___qtablewidgetitem = self.tableWidgetData.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindowHome", u"\u0627\u0633\u0645 \u0627\u0644\u0639\u0645\u064a\u0644", None));
        ___qtablewidgetitem1 = self.tableWidgetData.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindowHome", u"\u0631\u0642\u0645 \u0627\u0644\u062d\u0633\u0627\u0628", None));
        ___qtablewidgetitem2 = self.tableWidgetData.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindowHome", u"\u0642\u064a\u0645\u0629 \u0627\u0644\u062a\u062d\u0648\u064a\u0644", None));
        ___qtablewidgetitem3 = self.tableWidgetData.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindowHome", u"\u0627\u0633\u0645 \u0627\u0644\u0628\u0646\u0643", None));
        ___qtablewidgetitem4 = self.tableWidgetData.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindowHome", u"\u0627\u064a \u062a\u0639\u0644\u064a\u0642", None));
        self.pushButtonNextLevel.setText(QCoreApplication.translate("MainWindowHome", u"\u0627\u0646\u0642\u0631 \u0647\u0646\u0627 \u0644\u0627\u0646\u0634\u0627\u0621 \u0645\u0644\u0641 \u0627\u0644\u0627\u0643\u0633\u0644 \u0644\u0644\u0628\u064a\u0627\u0646\u0627\u062a \u0627\u0644\u0645\u062f\u062e\u0644\u0647 \u0627\u0639\u0644\u0627\u0647 \u0648\u0627\u0644\u0627\u0646\u062a\u0642\u0627\u0644 \u0627\u0644\u064a \u0627\u0644\u0645\u0631\u062d\u0644\u0629 \u0627\u0644\u062a\u0627\u0644\u064a\u0647", None))
        self.tabWidgetHome.setTabText(self.tabWidgetHome.indexOf(self.tabData), QCoreApplication.translate("MainWindowHome", u"\u0645\u0631\u062d\u0644\u0629 \u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u0628\u064a\u0627\u0646\u0627\u062a", None))
        self.label.setText(QCoreApplication.translate("MainWindowHome", u"\u0647\u0630\u0647 \u0627\u0644\u062e\u0627\u0635\u064a\u0647 \u0644\u0627 \u062a\u0639\u0645\u0644 \u0647\u0646\u0627 \u0628\u0644 \u0627\u0636\u063a\u0637 \u0639\u0644\u064a F9 \u0644\u0641\u062a\u062d \u0627\u0644\u0645\u0648\u0642\u0639 \u0641\u064a \u0645\u062a\u0635\u0641\u062d \u062e\u0627\u0631\u062c\u064a", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindowHome", u"\u0645\u0648\u0642\u0639 \u0627\u0644\u0628\u0646\u0643", None))
        self.labelWebsiteLoadPrpgress.setText(QCoreApplication.translate("MainWindowHome", u"\u062c\u0627\u0631\u064a \u0627\u0644\u062a\u062d\u0645\u064a\u0644 .. \u0627\u0646\u0638\u0631 \u0642\u0644\u064a\u0644\u0627", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindowHome", u"\u0628\u064a\u0627\u0646\u0627\u062a \u0627\u0641\u062a\u0631\u0627\u0636\u064a\u0647 - \u0647\u0630\u0647 \u0627\u0644\u0628\u064a\u0627\u0646\u0627\u062a \u0644\u0645\u0633\u0627\u0639\u062f\u062a\u0643 \u0639\u0644\u064a \u062a\u0630\u0643\u0631\u0647\u0627", None))
        self.label_14.setText(QCoreApplication.translate("MainWindowHome", u"\u0647\u0630\u0647 \u0627\u0644\u0628\u064a\u0627\u0646\u0627\u062a \u0644\u0645\u0633\u0627\u0639\u062f\u062a\u0643 \u0641\u0642\u0637 \u0639\u0644\u064a \u0633\u0631\u0639\u0629 \u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644\u060c \u0648\u0644\u0633\u062a \u0645\u0636\u0637\u0631\u0627 \u0639\u0644\u064a \u0627\u0644\u0627\u0637\u0644\u0627\u0642 \u0627\u0644\u064a \u0627\u0633\u062e\u062f\u0627\u0645\u0647\u0627. \u0644\u0646\u0641\u0631\u0636 \u0645\u062b\u0644\u0627 \u0627\u0646\u0643 \u062a\u0631\u064a\u062f \u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644 \u0627\u0644\u064a \u0627\u0644\u0645\u0648\u0642\u0639: \u0641\u0623\u0646\u062a \u062a\u062d\u062a\u0627\u062c \u0627\u0644\u064a \u0627\u0633\u0645 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u060c \u064a\u062a\u0643\u0648\u0646 \u0645\u0646 16 \u0631\u0642\u0645\u060c \u0648\u0643\u0644\u0645\u0629 \u0627\u0644\u0645\u0631\u0648\u0631. \u0641\u0647\u0644 \u0645\u0646 \u0627\u0644\u0645\u0639\u0642\u0648\u0644"
                        " \u0627\u0646\u0646\u064a \u0641\u064a \u0643\u0644 \u0645\u0631\u0629 \u0627\u0643\u062a\u0628 \u0627\u0633\u0645 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645 \u0628\u062f\u0648\u0646 \u0627\u0646 \u062a\u0643\u0648\u0646 \u0647\u0646\u0627\u0643 \u0648\u0633\u064a\u0644\u0629 \u0644\u0627\u062f\u062e\u0627\u0644\u0647 \u0628\u0636\u063a\u0637\u0629 \u0632\u0631\u061f \u0628\u0627\u0644\u0637\u0628\u0639 \u0644\u0627. \u0644\u0630\u0627 \u062c\u0639\u0644\u0646\u0627 \u0644\u0643 \u062a\u0644\u0643 \u0627\u0644\u062e\u0627\u0646\u0627\u062a \u0628\u0627\u0644\u0627\u0633\u0641\u0644 \u0644\u062a\u0633\u0647\u064a\u0644 \u0630\u0644\u0643.", None))
        self.label_19.setText(QCoreApplication.translate("MainWindowHome", u"\u0627\u0633\u0645 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645", None))
        self.label_18.setText(QCoreApplication.translate("MainWindowHome", u"\u0643\u0644\u0645\u0629 \u0627\u0644\u0633\u0631", None))
        self.label_20.setText(QCoreApplication.translate("MainWindowHome", u"\u0631\u0642\u0645 \u0627\u0644\u062d\u0633\u0627\u0628 \u0627\u0644\u0627\u0641\u062a\u0631\u0627\u0636\u064a", None))
        self.label_21.setText(QCoreApplication.translate("MainWindowHome", u"\u0643\u0648\u062f \u0628\u0646\u0643 \u0627\u0641\u062a\u0631\u0627\u0636\u064a", None))
        self.label_22.setText(QCoreApplication.translate("MainWindowHome", u"\u0627\u0633\u0645 \u0639\u0645\u064a\u0644 \u0627\u0641\u062a\u0631\u0627\u0636\u064a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindowHome", u"\u0645\u0644\u0641 \u0627\u0644\u0627\u0643\u0633\u0644", None))
        self.lineEditUsername.setText("")
        self.lineEditUsername.setPlaceholderText(QCoreApplication.translate("MainWindowHome", u"\u0627\u062f\u062e\u0644 \u0627\u0633\u0645 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645", None))
        self.lineEditPassword.setInputMask("")
        self.lineEditPassword.setText("")
        self.lineEditPassword.setPlaceholderText(QCoreApplication.translate("MainWindowHome", u"\u0627\u062f\u062e\u0644 \u0643\u0644\u0645\u0629 \u0627\u0644\u0633\u0631", None))
        self.lineEditDefaultAccountNumber.setText("")
        self.lineEditDefaultAccountNumber.setPlaceholderText(QCoreApplication.translate("MainWindowHome", u"\u0627\u062f\u062e\u0644 \u0631\u0642\u0645 \u062d\u0633\u0627\u0628 \u0627\u0641\u062a\u0631\u0627\u0636\u064a", None))
        self.lineEditDefaultBankCode.setText("")
        self.lineEditDefaultBankCode.setPlaceholderText(QCoreApplication.translate("MainWindowHome", u"\u0627\u062f\u062e\u0644 \u0643\u0648\u062f \u0628\u0646\u0643 \u0627\u0641\u062a\u0631\u0627\u0636\u064a", None))
        self.lineEditDefaultCustomerName.setText("")
        self.lineEditDefaultCustomerName.setPlaceholderText(QCoreApplication.translate("MainWindowHome", u"\u0627\u062f\u062e\u0644 \u0627\u0633\u0645 \u0639\u0645\u064a\u0644 \u0627\u0641\u062a\u0631\u0627\u0636\u064a", None))
        self.lineEditXLSXPath.setPlaceholderText(QCoreApplication.translate("MainWindowHome", u"\u0641\u064a \u0647\u0630\u0627 \u0627\u0644\u0645\u0643\u0627\u0646 \u0633\u064a\u062a\u0645 \u0627\u0646\u0634\u0627\u0621 \u0627\u0644\u0645\u0633\u0627\u0631 \u0627\u0644\u062e\u0627\u0635 \u0628\u0627\u0644\u0645\u0644\u0641 \u0627\u0644\u062c\u0627\u0647\u0632 \u0644\u0644\u0631\u0641\u0639 \u0639\u0644\u064a \u0645\u0648\u0642\u0639 \u0627\u0644\u0628\u0646\u0643", None))
        self.pushButtonCopyUsername.setText(QCoreApplication.translate("MainWindowHome", u"\u0646\u0633\u062e", None))
        self.pushButtonCopyPassword.setText(QCoreApplication.translate("MainWindowHome", u"\u0646\u0633\u062e", None))
        self.pushButtonCopyAccountNumber.setText(QCoreApplication.translate("MainWindowHome", u"\u0646\u0633\u062e", None))
        self.pushButtonCopyBankCode.setText(QCoreApplication.translate("MainWindowHome", u"\u0646\u0633\u062e", None))
        self.pushButtonCopyCustomerName.setText(QCoreApplication.translate("MainWindowHome", u"\u0646\u0633\u062e", None))
        self.pushButtonCopyPath.setText(QCoreApplication.translate("MainWindowHome", u"\u0646\u0633\u062e", None))
        self.tabWidgetHome.setTabText(self.tabWidgetHome.indexOf(self.tabUploadData), QCoreApplication.translate("MainWindowHome", u"\u0645\u0631\u062d\u0644\u0629 \u0631\u0641\u0639 \u0627\u0644\u0628\u064a\u0627\u0646\u0627\u062a", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindowHome", u"\u0627\u062a\u0645\u062a\u0647 - \u0647\u0630\u0647 \u0627\u0644\u0639\u0645\u0644\u064a\u0647 \u0644\u0646 \u062a\u062a\u062f\u062e\u0644 \u0628\u0647\u0627 \u0628\u0644 \u0633\u064a\u0642\u0648\u0645 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0628\u0641\u0639\u0644 \u0643\u0644 \u0634\u0626", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindowHome", u"\u0627\u0633\u062a\u062d\u0631\u0627\u062c \u062a\u0642\u0631\u064a\u0631", None))
        self.label_5.setText(QCoreApplication.translate("MainWindowHome", u"\u0633\u064a\u0642\u0648\u0645 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0628\u0634\u0643\u0644 \u0627\u0648\u062a\u0648\u0645\u0627\u062a\u064a\u0643\u064a \u0628\u0627\u0644\u062f\u062e\u0648\u0644 \u0627\u0644\u064a \u0645\u0648\u0642\u0639 \u0627\u0644\u0628\u0646\u0643 \u0648\u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644 \u0628\u0634\u0643\u0644 \u062a\u0644\u0642\u0627\u0626\u064a \u0628\u0646\u0627\u0621\u0627 \u0639\u0644\u064a \u0627\u0644\u0628\u064a\u0627\u0646\u062a \u0627\u0644\u0627\u0641\u062a\u0631\u0627\u0636\u064a\u0647 \u0627\u0644\u0645\u062f\u062e\u0644\u0629 \u0645\u0646 \u0642\u0628\u0644 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u060c \u0648\u0628\u0639\u062f \u0630\u0644\u0643 \u064a\u0636\u063a\u0637 \u0639\u0644\u064a \u0639\u0631\u0636 \u0627\u0644\u062a\u0642\u0627\u0631\u064a\u0631 \u0648\u064a\u062e\u062a\u0627\u0631 \u0627\u0644\u0645\u062f\u0629 \u0648\u0643\u0630\u0644\u0643 \u0646\u0648\u0639 \u0627\u0644\u0645\u0644\u0641 \u0627\u0644\u0645"
                        "\u062e\u0631\u062c", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindowHome", u"\u0627\u062d\u0635\u0644 \u0639\u0644\u064a \u0627\u0644\u062a\u0642\u0631\u064a\u0631", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindowHome", u"\u0627\u0633\u062a\u062d\u0631\u0627\u062c \u062a\u0642\u0631\u064a\u0631", None))
        self.label_8.setText(QCoreApplication.translate("MainWindowHome", u"\u0633\u064a\u0642\u0648\u0645 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0628\u0634\u0643\u0644 \u0627\u0648\u062a\u0648\u0645\u0627\u062a\u064a\u0643\u064a \u0628\u0627\u0644\u062f\u062e\u0648\u0644 \u0627\u0644\u064a \u0645\u0648\u0642\u0639 \u0627\u0644\u0628\u0646\u0643 \u0648\u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644 \u0628\u0634\u0643\u0644 \u062a\u0644\u0642\u0627\u0626\u064a \u0628\u0646\u0627\u0621\u0627 \u0639\u0644\u064a \u0627\u0644\u0628\u064a\u0627\u0646\u062a \u0627\u0644\u0627\u0641\u062a\u0631\u0627\u0636\u064a\u0647 \u0627\u0644\u0645\u062f\u062e\u0644\u0629 \u0645\u0646 \u0642\u0628\u0644 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u060c \u0648\u0628\u0639\u062f \u0630\u0644\u0643 \u064a\u0636\u063a\u0637 \u0639\u0644\u064a \u0639\u0631\u0636 \u0627\u0644\u062a\u0642\u0627\u0631\u064a\u0631 \u0648\u064a\u062e\u062a\u0627\u0631 \u0627\u0644\u0645\u062f\u0629 \u0648\u0643\u0630\u0644\u0643 \u0646\u0648\u0639 \u0627\u0644\u0645\u0644\u0641 \u0627\u0644\u0645"
                        "\u062e\u0631\u062c", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindowHome", u"\u0627\u062d\u0635\u0644 \u0639\u0644\u064a \u0627\u0644\u062a\u0642\u0631\u064a\u0631", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindowHome", u"\u0627\u0633\u062a\u062d\u0631\u0627\u062c \u062a\u0642\u0631\u064a\u0631", None))
        self.label_2.setText(QCoreApplication.translate("MainWindowHome", u"\u0633\u064a\u0642\u0648\u0645 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0628\u0634\u0643\u0644 \u0627\u0648\u062a\u0648\u0645\u0627\u062a\u064a\u0643\u064a \u0628\u0627\u0644\u062f\u062e\u0648\u0644 \u0627\u0644\u064a \u0645\u0648\u0642\u0639 \u0627\u0644\u0628\u0646\u0643 \u0648\u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644 \u0628\u0634\u0643\u0644 \u062a\u0644\u0642\u0627\u0626\u064a \u0628\u0646\u0627\u0621\u0627 \u0639\u0644\u064a \u0627\u0644\u0628\u064a\u0627\u0646\u062a \u0627\u0644\u0627\u0641\u062a\u0631\u0627\u0636\u064a\u0647 \u0627\u0644\u0645\u062f\u062e\u0644\u0629 \u0645\u0646 \u0642\u0628\u0644 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u060c \u0648\u0628\u0639\u062f \u0630\u0644\u0643 \u064a\u0636\u063a\u0637 \u0639\u0644\u064a \u0639\u0631\u0636 \u0627\u0644\u062a\u0642\u0627\u0631\u064a\u0631 \u0648\u064a\u062e\u062a\u0627\u0631 \u0627\u0644\u0645\u062f\u0629 \u0648\u0643\u0630\u0644\u0643 \u0646\u0648\u0639 \u0627\u0644\u0645\u0644\u0641 \u0627\u0644\u0645"
                        "\u062e\u0631\u062c", None))
        self.dateEditReportFrom.setSpecialValueText("")
        self.dateEditReportTo.setSpecialValueText("")
        self.pushButtonGetDatedReport.setText(QCoreApplication.translate("MainWindowHome", u"\u0627\u062d\u0635\u0644 \u0639\u0644\u064a \u0627\u0644\u062a\u0642\u0631\u064a\u0631", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindowHome", u"\u0627\u0633\u062a\u062d\u0631\u0627\u062c \u062a\u0642\u0631\u064a\u0631", None))
        self.label_3.setText(QCoreApplication.translate("MainWindowHome", u"\u0633\u064a\u0642\u0648\u0645 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0628\u0634\u0643\u0644 \u0627\u0648\u062a\u0648\u0645\u0627\u062a\u064a\u0643\u064a \u0628\u0627\u0644\u062f\u062e\u0648\u0644 \u0627\u0644\u064a \u0645\u0648\u0642\u0639 \u0627\u0644\u0628\u0646\u0643 \u0648\u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644 \u0628\u0634\u0643\u0644 \u062a\u0644\u0642\u0627\u0626\u064a \u0628\u0646\u0627\u0621\u0627 \u0639\u0644\u064a \u0627\u0644\u0628\u064a\u0627\u0646\u062a \u0627\u0644\u0627\u0641\u062a\u0631\u0627\u0636\u064a\u0647 \u0627\u0644\u0645\u062f\u062e\u0644\u0629 \u0645\u0646 \u0642\u0628\u0644 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u060c \u0648\u0628\u0639\u062f \u0630\u0644\u0643 \u064a\u0636\u063a\u0637 \u0639\u0644\u064a \u0639\u0631\u0636 \u0627\u0644\u062a\u0642\u0627\u0631\u064a\u0631 \u0648\u064a\u062e\u062a\u0627\u0631 \u0627\u0644\u0645\u062f\u0629 \u0648\u0643\u0630\u0644\u0643 \u0646\u0648\u0639 \u0627\u0644\u0645\u0644\u0641 \u0627\u0644\u0645"
                        "\u062e\u0631\u062c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindowHome", u"\u0627\u062d\u0635\u0644 \u0639\u0644\u064a \u0627\u0644\u062a\u0642\u0631\u064a\u0631", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindowHome", u"\u0627\u0633\u062a\u062d\u0631\u0627\u062c \u062a\u0642\u0631\u064a\u0631", None))
        self.label_4.setText(QCoreApplication.translate("MainWindowHome", u"\u0633\u064a\u0642\u0648\u0645 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0628\u0634\u0643\u0644 \u0627\u0648\u062a\u0648\u0645\u0627\u062a\u064a\u0643\u064a \u0628\u0627\u0644\u062f\u062e\u0648\u0644 \u0627\u0644\u064a \u0645\u0648\u0642\u0639 \u0627\u0644\u0628\u0646\u0643 \u0648\u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644 \u0628\u0634\u0643\u0644 \u062a\u0644\u0642\u0627\u0626\u064a \u0628\u0646\u0627\u0621\u0627 \u0639\u0644\u064a \u0627\u0644\u0628\u064a\u0627\u0646\u062a \u0627\u0644\u0627\u0641\u062a\u0631\u0627\u0636\u064a\u0647 \u0627\u0644\u0645\u062f\u062e\u0644\u0629 \u0645\u0646 \u0642\u0628\u0644 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u060c \u0648\u0628\u0639\u062f \u0630\u0644\u0643 \u064a\u0636\u063a\u0637 \u0639\u0644\u064a \u0639\u0631\u0636 \u0627\u0644\u062a\u0642\u0627\u0631\u064a\u0631 \u0648\u064a\u062e\u062a\u0627\u0631 \u0627\u0644\u0645\u062f\u0629 \u0648\u0643\u0630\u0644\u0643 \u0646\u0648\u0639 \u0627\u0644\u0645\u0644\u0641 \u0627\u0644\u0645"
                        "\u062e\u0631\u062c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindowHome", u"\u0627\u062d\u0635\u0644 \u0639\u0644\u064a \u0627\u0644\u062a\u0642\u0631\u064a\u0631", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindowHome", u"\u0627\u0633\u062a\u062d\u0631\u0627\u062c \u062a\u0642\u0631\u064a\u0631", None))
        self.label_9.setText(QCoreApplication.translate("MainWindowHome", u"\u0633\u064a\u0642\u0648\u0645 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0628\u0634\u0643\u0644 \u0627\u0648\u062a\u0648\u0645\u0627\u062a\u064a\u0643\u064a \u0628\u0627\u0644\u062f\u062e\u0648\u0644 \u0627\u0644\u064a \u0645\u0648\u0642\u0639 \u0627\u0644\u0628\u0646\u0643 \u0648\u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644 \u0628\u0634\u0643\u0644 \u062a\u0644\u0642\u0627\u0626\u064a \u0628\u0646\u0627\u0621\u0627 \u0639\u0644\u064a \u0627\u0644\u0628\u064a\u0627\u0646\u062a \u0627\u0644\u0627\u0641\u062a\u0631\u0627\u0636\u064a\u0647 \u0627\u0644\u0645\u062f\u062e\u0644\u0629 \u0645\u0646 \u0642\u0628\u0644 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u060c \u0648\u0628\u0639\u062f \u0630\u0644\u0643 \u064a\u0636\u063a\u0637 \u0639\u0644\u064a \u0639\u0631\u0636 \u0627\u0644\u062a\u0642\u0627\u0631\u064a\u0631 \u0648\u064a\u062e\u062a\u0627\u0631 \u0627\u0644\u0645\u062f\u0629 \u0648\u0643\u0630\u0644\u0643 \u0646\u0648\u0639 \u0627\u0644\u0645\u0644\u0641 \u0627\u0644\u0645"
                        "\u062e\u0631\u062c", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindowHome", u"\u0627\u062d\u0635\u0644 \u0639\u0644\u064a \u0627\u0644\u062a\u0642\u0631\u064a\u0631", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindowHome", u"\u0627\u0633\u062a\u062d\u0631\u0627\u062c \u062a\u0642\u0631\u064a\u0631", None))
        self.label_11.setText(QCoreApplication.translate("MainWindowHome", u"\u0633\u064a\u0642\u0648\u0645 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0628\u0634\u0643\u0644 \u0627\u0648\u062a\u0648\u0645\u0627\u062a\u064a\u0643\u064a \u0628\u0627\u0644\u062f\u062e\u0648\u0644 \u0627\u0644\u064a \u0645\u0648\u0642\u0639 \u0627\u0644\u0628\u0646\u0643 \u0648\u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644 \u0628\u0634\u0643\u0644 \u062a\u0644\u0642\u0627\u0626\u064a \u0628\u0646\u0627\u0621\u0627 \u0639\u0644\u064a \u0627\u0644\u0628\u064a\u0627\u0646\u062a \u0627\u0644\u0627\u0641\u062a\u0631\u0627\u0636\u064a\u0647 \u0627\u0644\u0645\u062f\u062e\u0644\u0629 \u0645\u0646 \u0642\u0628\u0644 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u060c \u0648\u0628\u0639\u062f \u0630\u0644\u0643 \u064a\u0636\u063a\u0637 \u0639\u0644\u064a \u0639\u0631\u0636 \u0627\u0644\u062a\u0642\u0627\u0631\u064a\u0631 \u0648\u064a\u062e\u062a\u0627\u0631 \u0627\u0644\u0645\u062f\u0629 \u0648\u0643\u0630\u0644\u0643 \u0646\u0648\u0639 \u0627\u0644\u0645\u0644\u0641 \u0627\u0644\u0645"
                        "\u062e\u0631\u062c", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindowHome", u"\u0627\u062d\u0635\u0644 \u0639\u0644\u064a \u0627\u0644\u062a\u0642\u0631\u064a\u0631", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindowHome", u"\u0627\u0633\u062a\u062d\u0631\u0627\u062c \u062a\u0642\u0631\u064a\u0631", None))
        self.label_12.setText(QCoreApplication.translate("MainWindowHome", u"\u0633\u064a\u0642\u0648\u0645 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0628\u0634\u0643\u0644 \u0627\u0648\u062a\u0648\u0645\u0627\u062a\u064a\u0643\u064a \u0628\u0627\u0644\u062f\u062e\u0648\u0644 \u0627\u0644\u064a \u0645\u0648\u0642\u0639 \u0627\u0644\u0628\u0646\u0643 \u0648\u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644 \u0628\u0634\u0643\u0644 \u062a\u0644\u0642\u0627\u0626\u064a \u0628\u0646\u0627\u0621\u0627 \u0639\u0644\u064a \u0627\u0644\u0628\u064a\u0627\u0646\u062a \u0627\u0644\u0627\u0641\u062a\u0631\u0627\u0636\u064a\u0647 \u0627\u0644\u0645\u062f\u062e\u0644\u0629 \u0645\u0646 \u0642\u0628\u0644 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u060c \u0648\u0628\u0639\u062f \u0630\u0644\u0643 \u064a\u0636\u063a\u0637 \u0639\u0644\u064a \u0639\u0631\u0636 \u0627\u0644\u062a\u0642\u0627\u0631\u064a\u0631 \u0648\u064a\u062e\u062a\u0627\u0631 \u0627\u0644\u0645\u062f\u0629 \u0648\u0643\u0630\u0644\u0643 \u0646\u0648\u0639 \u0627\u0644\u0645\u0644\u0641 \u0627\u0644\u0645"
                        "\u062e\u0631\u062c", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindowHome", u"\u0627\u062d\u0635\u0644 \u0639\u0644\u064a \u0627\u0644\u062a\u0642\u0631\u064a\u0631", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindowHome", u"\u0627\u0633\u062a\u062d\u0631\u0627\u062c \u062a\u0642\u0631\u064a\u0631", None))
        self.label_13.setText(QCoreApplication.translate("MainWindowHome", u"\u0633\u064a\u0642\u0648\u0645 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0628\u0634\u0643\u0644 \u0627\u0648\u062a\u0648\u0645\u0627\u062a\u064a\u0643\u064a \u0628\u0627\u0644\u062f\u062e\u0648\u0644 \u0627\u0644\u064a \u0645\u0648\u0642\u0639 \u0627\u0644\u0628\u0646\u0643 \u0648\u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644 \u0628\u0634\u0643\u0644 \u062a\u0644\u0642\u0627\u0626\u064a \u0628\u0646\u0627\u0621\u0627 \u0639\u0644\u064a \u0627\u0644\u0628\u064a\u0627\u0646\u062a \u0627\u0644\u0627\u0641\u062a\u0631\u0627\u0636\u064a\u0647 \u0627\u0644\u0645\u062f\u062e\u0644\u0629 \u0645\u0646 \u0642\u0628\u0644 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u060c \u0648\u0628\u0639\u062f \u0630\u0644\u0643 \u064a\u0636\u063a\u0637 \u0639\u0644\u064a \u0639\u0631\u0636 \u0627\u0644\u062a\u0642\u0627\u0631\u064a\u0631 \u0648\u064a\u062e\u062a\u0627\u0631 \u0627\u0644\u0645\u062f\u0629 \u0648\u0643\u0630\u0644\u0643 \u0646\u0648\u0639 \u0627\u0644\u0645\u0644\u0641 \u0627\u0644\u0645"
                        "\u062e\u0631\u062c", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindowHome", u"\u0627\u062d\u0635\u0644 \u0639\u0644\u064a \u0627\u0644\u062a\u0642\u0631\u064a\u0631", None))
        self.tabWidgetHome.setTabText(self.tabWidgetHome.indexOf(self.tab), QCoreApplication.translate("MainWindowHome", u"\u0645\u0647\u0627\u0645 \u0633\u0631\u064a\u0639\u0647", None))
#if QT_CONFIG(tooltip)
        self.statusbar.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.statusbar.setStatusTip("")
#endif // QT_CONFIG(statustip)
    # retranslateUi

