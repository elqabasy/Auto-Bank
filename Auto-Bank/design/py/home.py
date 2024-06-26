# -*- coding: utf-8 -*-

# import resources_rc
from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QMetaObject,
    QSize,
    Qt,
)
from PySide6.QtGui import (
    QFont,
    QIcon,
)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (
    QAbstractItemView,
    QAbstractScrollArea,
    QAbstractSpinBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLayout,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QSplitter,
    QStackedWidget,
    QStatusBar,
    QTableWidget,
    QTableWidgetItem,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindowHome(object):
    def setupUi(self, MainWindowHome):
        if not MainWindowHome.objectName():
            MainWindowHome.setObjectName("MainWindowHome")
        MainWindowHome.setWindowModality(Qt.WindowModality.ApplicationModal)
        MainWindowHome.resize(900, 637)
        font = QFont()
        font.setFamilies(["Candara"])
        font.setPointSize(1)
        MainWindowHome.setFont(font)
        icon = QIcon()
        icon.addFile(":/icons/.ico/app.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindowHome.setWindowIcon(icon)
        MainWindowHome.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.centralwidget = QWidget(MainWindowHome)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_10 = QGridLayout(self.centralwidget)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 0, 9, 0)
        self.radioButtonAccountStatus = QRadioButton(self.centralwidget)
        self.radioButtonAccountStatus.setObjectName("radioButtonAccountStatus")
        self.radioButtonAccountStatus.setEnabled(True)
        self.radioButtonAccountStatus.setMinimumSize(QSize(73, 0))
        self.radioButtonAccountStatus.setMaximumSize(QSize(73, 16777215))
        font1 = QFont()
        font1.setFamilies(["Cairo"])
        font1.setPointSize(9)
        font1.setBold(False)
        self.radioButtonAccountStatus.setFont(font1)
        self.radioButtonAccountStatus.setCheckable(True)
        self.radioButtonAccountStatus.setChecked(False)

        self.horizontalLayout.addWidget(self.radioButtonAccountStatus)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.labelHomeTitle = QLabel(self.centralwidget)
        self.labelHomeTitle.setObjectName("labelHomeTitle")
        font2 = QFont()
        font2.setFamilies(["Cairo"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.labelHomeTitle.setFont(font2)

        self.horizontalLayout.addWidget(self.labelHomeTitle)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButtonRefresh = QPushButton(self.centralwidget)
        self.pushButtonRefresh.setObjectName("pushButtonRefresh")
        self.pushButtonRefresh.setMinimumSize(QSize(0, 35))
        font3 = QFont()
        font3.setFamilies(["Cairo"])
        font3.setPointSize(9)
        font3.setItalic(True)
        self.pushButtonRefresh.setFont(font3)
        icon1 = QIcon(QIcon.fromTheme("emblem-synchronized"))
        self.pushButtonRefresh.setIcon(icon1)

        self.horizontalLayout.addWidget(self.pushButtonRefresh)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        font4 = QFont()
        font4.setFamilies(["Cairo"])
        font4.setPointSize(9)
        self.stackedWidget.setFont(font4)
        self.stackedWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.stackedWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.stackedWidget.setLineWidth(1)
        self.page = QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.tabWidgetHome = QTabWidget(self.page)
        self.tabWidgetHome.setObjectName("tabWidgetHome")
        self.tabWidgetHome.setEnabled(True)
        self.tabWidgetHome.setFont(font4)
        self.tabWidgetHome.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.tabWidgetHome.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidgetHome.setDocumentMode(False)
        self.tabWidgetHome.setMovable(False)
        self.tabWidgetHome.setTabBarAutoHide(False)
        self.tabData = QWidget()
        self.tabData.setObjectName("tabData")
        self.gridLayout_11 = QGridLayout(self.tabData)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.groupBox_4 = QGroupBox(self.tabData)
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_4.setFont(font4)
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.splitter = QSplitter(self.groupBox_4)
        self.splitter.setObjectName("splitter")
        self.splitter.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setHandleWidth(2)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_15 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_15.setSpacing(11)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalLayout_15.setSizeConstraint(
            QLayout.SizeConstraint.SetFixedSize
        )
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.pushButtonAdd = QPushButton(self.layoutWidget)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.pushButtonAdd.setMinimumSize(QSize(0, 35))
        self.pushButtonAdd.setFont(font4)
        self.pushButtonAdd.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon2 = QIcon(QIcon.fromTheme("list-add"))
        self.pushButtonAdd.setIcon(icon2)

        self.horizontalLayout_15.addWidget(self.pushButtonAdd)

        self.pushButtonDelete = QPushButton(self.layoutWidget)
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.pushButtonDelete.setMinimumSize(QSize(0, 35))
        self.pushButtonDelete.setFont(font4)
        self.pushButtonDelete.setLayoutDirection(
            Qt.LayoutDirection.LeftToRight
        )
        icon3 = QIcon(QIcon.fromTheme("list-remove"))
        self.pushButtonDelete.setIcon(icon3)

        self.horizontalLayout_15.addWidget(self.pushButtonDelete)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget2 = QWidget(self.splitter)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_14 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_14.setSpacing(9)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(5, 0, 5, 0)
        self.labelMoney = QLabel(self.layoutWidget2)
        self.labelMoney.setObjectName("labelMoney")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.labelMoney.sizePolicy().hasHeightForWidth()
        )
        self.labelMoney.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setFamilies(["Cairo"])
        font5.setPointSize(9)
        font5.setBold(True)
        self.labelMoney.setFont(font5)
        self.labelMoney.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelMoney.setWordWrap(True)

        self.horizontalLayout_14.addWidget(self.labelMoney)

        self.spinBoxTransactionAmount = QSpinBox(self.layoutWidget2)
        self.spinBoxTransactionAmount.setObjectName("spinBoxTransactionAmount")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.spinBoxTransactionAmount.sizePolicy().hasHeightForWidth()
        )
        self.spinBoxTransactionAmount.setSizePolicy(sizePolicy1)
        self.spinBoxTransactionAmount.setMinimumSize(QSize(0, 38))
        self.spinBoxTransactionAmount.setFont(font4)
        self.spinBoxTransactionAmount.setButtonSymbols(
            QAbstractSpinBox.ButtonSymbols.PlusMinus
        )
        self.spinBoxTransactionAmount.setAccelerated(True)
        self.spinBoxTransactionAmount.setMinimum(0)
        self.spinBoxTransactionAmount.setMaximum(1500000)
        self.spinBoxTransactionAmount.setSingleStep(1000)
        self.spinBoxTransactionAmount.setValue(0)
        self.spinBoxTransactionAmount.setDisplayIntegerBase(10)

        self.horizontalLayout_14.addWidget(self.spinBoxTransactionAmount)

        self.label_10 = QLabel(self.layoutWidget2)
        self.label_10.setObjectName("label_10")
        sizePolicy.setHeightForWidth(
            self.label_10.sizePolicy().hasHeightForWidth()
        )
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setFont(font4)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_10)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 1)
        self.splitter.addWidget(self.layoutWidget2)
        self.layoutWidget3 = QWidget(self.splitter)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_13 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.comboBoxBankName = QComboBox(self.layoutWidget3)
        self.comboBoxBankName.setObjectName("comboBoxBankName")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.comboBoxBankName.sizePolicy().hasHeightForWidth()
        )
        self.comboBoxBankName.setSizePolicy(sizePolicy2)
        self.comboBoxBankName.setMinimumSize(QSize(0, 38))
        self.comboBoxBankName.setFont(font4)
        self.comboBoxBankName.setLayoutDirection(
            Qt.LayoutDirection.RightToLeft
        )
        self.comboBoxBankName.setEditable(False)

        self.horizontalLayout_13.addWidget(self.comboBoxBankName)

        self.splitter.addWidget(self.layoutWidget3)
        self.layoutWidget4 = QWidget(self.splitter)
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_12 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lineEditAccountCreatorAccountNumber = QLineEdit(
            self.layoutWidget4
        )
        self.lineEditAccountCreatorAccountNumber.setObjectName(
            "lineEditAccountCreatorAccountNumber"
        )
        sizePolicy1.setHeightForWidth(
            self.lineEditAccountCreatorAccountNumber.sizePolicy(
            ).hasHeightForWidth()
        )
        self.lineEditAccountCreatorAccountNumber.setSizePolicy(sizePolicy1)
        self.lineEditAccountCreatorAccountNumber.setMinimumSize(QSize(0, 35))
        self.lineEditAccountCreatorAccountNumber.setFont(font4)
        self.lineEditAccountCreatorAccountNumber.setLayoutDirection(
            Qt.LayoutDirection.RightToLeft
        )
        self.lineEditAccountCreatorAccountNumber.setMaxLength(16)
        self.lineEditAccountCreatorAccountNumber.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.horizontalLayout_12.addWidget(
            self.lineEditAccountCreatorAccountNumber
        )

        self.lineEditCreatorName = QLineEdit(self.layoutWidget4)
        self.lineEditCreatorName.setObjectName("lineEditCreatorName")
        sizePolicy1.setHeightForWidth(
            self.lineEditCreatorName.sizePolicy().hasHeightForWidth()
        )
        self.lineEditCreatorName.setSizePolicy(sizePolicy1)
        self.lineEditCreatorName.setMinimumSize(QSize(0, 35))
        self.lineEditCreatorName.setFont(font4)
        self.lineEditCreatorName.setLayoutDirection(
            Qt.LayoutDirection.RightToLeft
        )
        self.lineEditCreatorName.setMaxLength(63)
        self.lineEditCreatorName.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.horizontalLayout_12.addWidget(self.lineEditCreatorName)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 1)
        self.splitter.addWidget(self.layoutWidget4)

        self.gridLayout_4.addWidget(self.splitter, 0, 0, 1, 1)

        self.gridLayout_11.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.tabData)
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_5.setFont(font4)
        self.gridLayout_9 = QGridLayout(self.groupBox_5)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.tableWidgetData = QTableWidget(self.groupBox_5)
        if self.tableWidgetData.columnCount() < 5:
            self.tableWidgetData.setColumnCount(5)
        font6 = QFont()
        font6.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font6)
        self.tableWidgetData.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font6)
        self.tableWidgetData.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font6)
        self.tableWidgetData.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font6)
        self.tableWidgetData.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font6)
        self.tableWidgetData.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidgetData.setObjectName("tableWidgetData")
        self.tableWidgetData.setEnabled(True)
        self.tableWidgetData.setFont(font4)
        self.tableWidgetData.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )
        self.tableWidgetData.setAlternatingRowColors(True)
        self.tableWidgetData.setRowCount(0)
        self.tableWidgetData.horizontalHeader().setCascadingSectionResizes(
            True
        )
        self.tableWidgetData.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidgetData.horizontalHeader().setDefaultSectionSize(300)
        self.tableWidgetData.horizontalHeader().setHighlightSections(True)
        self.tableWidgetData.horizontalHeader().setProperty(
            "showSortIndicator",
            False
        )
        self.tableWidgetData.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetData.verticalHeader().setDefaultSectionSize(50)

        self.gridLayout_9.addWidget(self.tableWidgetData, 0, 0, 1, 1)

        self.gridLayout_11.addWidget(self.groupBox_5, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(
            QLayout.SizeConstraint.SetMaximumSize
        )
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButtonNextLevel = QPushButton(self.tabData)
        self.pushButtonNextLevel.setObjectName("pushButtonNextLevel")
        self.pushButtonNextLevel.setEnabled(True)
        self.pushButtonNextLevel.setMinimumSize(QSize(0, 35))
        self.pushButtonNextLevel.setFont(font4)
        self.pushButtonNextLevel.setLayoutDirection(
            Qt.LayoutDirection.LeftToRight
        )
        icon4 = QIcon(QIcon.fromTheme("go-next"))
        self.pushButtonNextLevel.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.pushButtonNextLevel)

        self.gridLayout_11.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.tabWidgetHome.addTab(self.tabData, "")
        self.tabUploadData = QWidget()
        self.tabUploadData.setObjectName("tabUploadData")
        self.gridLayout_14 = QGridLayout(self.tabUploadData)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_10 = QGroupBox(self.tabUploadData)
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_3 = QGridLayout(self.groupBox_10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label = QLabel(self.groupBox_10)
        self.label.setObjectName("label")
        self.label.setFont(font5)
        self.label.setStyleSheet("color:yellow")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.label)

        self.widgetWebPage = QWebEngineView(self.groupBox_10)
        self.widgetWebPage.setObjectName("widgetWebPage")
        self.widgetWebPage.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.verticalLayout_14.addWidget(self.widgetWebPage)

        self.labelWebsiteLoadPrpgress = QLabel(self.groupBox_10)
        self.labelWebsiteLoadPrpgress.setObjectName("labelWebsiteLoadPrpgress")
        font7 = QFont()
        font7.setFamilies(["Cairo"])
        font7.setPointSize(12)
        font7.setBold(True)
        self.labelWebsiteLoadPrpgress.setFont(font7)
        self.labelWebsiteLoadPrpgress.setStyleSheet("color:yellow")
        self.labelWebsiteLoadPrpgress.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.verticalLayout_14.addWidget(self.labelWebsiteLoadPrpgress)

        self.verticalLayout_14.setStretch(1, 1)
        self.verticalLayout_14.setStretch(2, 1)

        self.gridLayout_3.addLayout(self.verticalLayout_14, 0, 0, 1, 1)

        self.verticalLayout_6.addWidget(self.groupBox_10)

        self.verticalLayout_6.setStretch(0, 1)

        self.horizontalLayout_10.addLayout(self.verticalLayout_6)

        self.groupBox_12 = QGroupBox(self.tabUploadData)
        self.groupBox_12.setObjectName("groupBox_12")
        self.groupBox_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout = QGridLayout(self.groupBox_12)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.radioButtonActivateAutoLogin = QRadioButton(self.groupBox_12)
        self.radioButtonActivateAutoLogin.setObjectName(
            "radioButtonActivateAutoLogin"
        )
        self.radioButtonActivateAutoLogin.setEnabled(False)
        self.radioButtonActivateAutoLogin.setLayoutDirection(
            Qt.LayoutDirection.RightToLeft
        )

        self.horizontalLayout_8.addWidget(self.radioButtonActivateAutoLogin)

        self.horizontalSpacer_8 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.radioButtonActivateAutoUpload = QRadioButton(self.groupBox_12)
        self.radioButtonActivateAutoUpload.setObjectName(
            "radioButtonActivateAutoUpload"
        )
        self.radioButtonActivateAutoUpload.setEnabled(False)
        self.radioButtonActivateAutoUpload.setLayoutDirection(
            Qt.LayoutDirection.RightToLeft
        )

        self.horizontalLayout_8.addWidget(self.radioButtonActivateAutoUpload)

        self.gridLayout.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)

        self.line_2 = QFrame(self.groupBox_12)
        self.line_2.setObjectName("line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_14 = QLabel(self.groupBox_12)
        self.label_14.setObjectName("label_14")
        self.label_14.setContextMenuPolicy(
            Qt.ContextMenuPolicy.DefaultContextMenu
        )
        self.label_14.setAlignment(
            Qt.AlignmentFlag.AlignJustify | Qt.AlignmentFlag.AlignTop
        )
        self.label_14.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.label_14)

        self.line = QFrame(self.groupBox_12)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(
            QLayout.SizeConstraint.SetMaximumSize
        )
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(12)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_19 = QLabel(self.groupBox_12)
        self.label_19.setObjectName("label_19")

        self.verticalLayout_12.addWidget(self.label_19)

        self.verticalSpacer_12 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_12.addItem(self.verticalSpacer_12)

        self.label_18 = QLabel(self.groupBox_12)
        self.label_18.setObjectName("label_18")
        self.label_18.setFrameShape(QFrame.Shape.NoFrame)
        self.label_18.setScaledContents(False)

        self.verticalLayout_12.addWidget(self.label_18)

        self.verticalSpacer_13 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_12.addItem(self.verticalSpacer_13)

        self.label_20 = QLabel(self.groupBox_12)
        self.label_20.setObjectName("label_20")

        self.verticalLayout_12.addWidget(self.label_20)

        self.verticalSpacer_14 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_12.addItem(self.verticalSpacer_14)

        self.label_21 = QLabel(self.groupBox_12)
        self.label_21.setObjectName("label_21")

        self.verticalLayout_12.addWidget(self.label_21)

        self.verticalSpacer_15 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_12.addItem(self.verticalSpacer_15)

        self.label_22 = QLabel(self.groupBox_12)
        self.label_22.setObjectName("label_22")

        self.verticalLayout_12.addWidget(self.label_22)

        self.verticalSpacer_16 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_12.addItem(self.verticalSpacer_16)

        self.label_6 = QLabel(self.groupBox_12)
        self.label_6.setObjectName("label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_12.addWidget(self.label_6)

        self.horizontalLayout_7.addLayout(self.verticalLayout_12)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.lineEditDefaultUsername = QLineEdit(self.groupBox_12)
        self.lineEditDefaultUsername.setObjectName("lineEditDefaultUsername")
        self.lineEditDefaultUsername.setMinimumSize(QSize(0, 32))
        self.lineEditDefaultUsername.setFrame(False)
        self.lineEditDefaultUsername.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.lineEditDefaultUsername)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_15.addItem(self.verticalSpacer)

        self.lineEditDefaultPassword = QLineEdit(self.groupBox_12)
        self.lineEditDefaultPassword.setObjectName("lineEditDefaultPassword")
        self.lineEditDefaultPassword.setMinimumSize(QSize(0, 32))
        self.lineEditDefaultPassword.setMaxLength(32767)
        self.lineEditDefaultPassword.setFrame(False)
        self.lineEditDefaultPassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEditDefaultPassword.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEditDefaultPassword.setCursorMoveStyle(
            Qt.CursorMoveStyle.VisualMoveStyle
        )
        self.lineEditDefaultPassword.setClearButtonEnabled(False)

        self.verticalLayout_15.addWidget(self.lineEditDefaultPassword)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_15.addItem(self.verticalSpacer_3)

        self.lineEditDefaultAccountNumber = QLineEdit(self.groupBox_12)
        self.lineEditDefaultAccountNumber.setObjectName(
            "lineEditDefaultAccountNumber"
        )
        self.lineEditDefaultAccountNumber.setMinimumSize(QSize(0, 32))
        self.lineEditDefaultAccountNumber.setMaxLength(16)
        self.lineEditDefaultAccountNumber.setFrame(False)
        self.lineEditDefaultAccountNumber.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.verticalLayout_15.addWidget(self.lineEditDefaultAccountNumber)

        self.verticalSpacer_4 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_15.addItem(self.verticalSpacer_4)

        self.lineEditDefaultBankName = QLineEdit(self.groupBox_12)
        self.lineEditDefaultBankName.setObjectName("lineEditDefaultBankName")
        self.lineEditDefaultBankName.setMinimumSize(QSize(0, 32))
        self.lineEditDefaultBankName.setFrame(False)
        self.lineEditDefaultBankName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.lineEditDefaultBankName)

        self.verticalSpacer_5 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_15.addItem(self.verticalSpacer_5)

        self.lineEditDefaultCustomerName = QLineEdit(self.groupBox_12)
        self.lineEditDefaultCustomerName.setObjectName(
            "lineEditDefaultCustomerName"
        )
        self.lineEditDefaultCustomerName.setMinimumSize(QSize(0, 32))
        self.lineEditDefaultCustomerName.setFrame(False)
        self.lineEditDefaultCustomerName.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.verticalLayout_15.addWidget(self.lineEditDefaultCustomerName)

        self.verticalSpacer_6 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_15.addItem(self.verticalSpacer_6)

        self.lineEditXLSXPath = QLineEdit(self.groupBox_12)
        self.lineEditXLSXPath.setObjectName("lineEditXLSXPath")
        self.lineEditXLSXPath.setMinimumSize(QSize(0, 35))
        self.lineEditXLSXPath.setFont(font1)
        self.lineEditXLSXPath.setFrame(False)
        self.lineEditXLSXPath.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEditXLSXPath.setReadOnly(True)
        self.lineEditXLSXPath.setCursorMoveStyle(
            Qt.CursorMoveStyle.VisualMoveStyle
        )

        self.verticalLayout_15.addWidget(self.lineEditXLSXPath)

        self.horizontalLayout_7.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.pushButtonCopyUsername = QPushButton(self.groupBox_12)
        self.pushButtonCopyUsername.setObjectName("pushButtonCopyUsername")
        self.pushButtonCopyUsername.setFont(font1)
        icon5 = QIcon(QIcon.fromTheme("edit-copy"))
        self.pushButtonCopyUsername.setIcon(icon5)

        self.verticalLayout_16.addWidget(self.pushButtonCopyUsername)

        self.verticalSpacer_7 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_16.addItem(self.verticalSpacer_7)

        self.pushButtonCopyPassword = QPushButton(self.groupBox_12)
        self.pushButtonCopyPassword.setObjectName("pushButtonCopyPassword")
        self.pushButtonCopyPassword.setFont(font1)
        self.pushButtonCopyPassword.setIcon(icon5)

        self.verticalLayout_16.addWidget(self.pushButtonCopyPassword)

        self.verticalSpacer_8 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_16.addItem(self.verticalSpacer_8)

        self.pushButtonCopyAccountNumber = QPushButton(self.groupBox_12)
        self.pushButtonCopyAccountNumber.setObjectName(
            "pushButtonCopyAccountNumber"
        )
        self.pushButtonCopyAccountNumber.setFont(font1)
        self.pushButtonCopyAccountNumber.setIcon(icon5)

        self.verticalLayout_16.addWidget(self.pushButtonCopyAccountNumber)

        self.verticalSpacer_9 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_16.addItem(self.verticalSpacer_9)

        self.pushButtonCopyBankName = QPushButton(self.groupBox_12)
        self.pushButtonCopyBankName.setObjectName("pushButtonCopyBankName")
        self.pushButtonCopyBankName.setFont(font1)
        self.pushButtonCopyBankName.setIcon(icon5)

        self.verticalLayout_16.addWidget(self.pushButtonCopyBankName)

        self.verticalSpacer_10 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_16.addItem(self.verticalSpacer_10)

        self.pushButtonCopyCustomerName = QPushButton(self.groupBox_12)
        self.pushButtonCopyCustomerName.setObjectName(
            "pushButtonCopyCustomerName"
        )
        self.pushButtonCopyCustomerName.setFont(font1)
        self.pushButtonCopyCustomerName.setIcon(icon5)

        self.verticalLayout_16.addWidget(self.pushButtonCopyCustomerName)

        self.verticalSpacer_11 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_16.addItem(self.verticalSpacer_11)

        self.pushButtonCopyPath = QPushButton(self.groupBox_12)
        self.pushButtonCopyPath.setObjectName("pushButtonCopyPath")
        self.pushButtonCopyPath.setFont(font1)
        self.pushButtonCopyPath.setIcon(icon5)

        self.verticalLayout_16.addWidget(self.pushButtonCopyPath)

        self.horizontalLayout_7.addLayout(self.verticalLayout_16)

        self.verticalLayout_13.addLayout(self.horizontalLayout_7)

        self.verticalLayout_13.setStretch(0, 10)

        self.gridLayout.addLayout(self.verticalLayout_13, 0, 0, 1, 1)

        self.horizontalLayout_10.addWidget(self.groupBox_12)

        self.horizontalLayout_10.setStretch(0, 10)

        self.gridLayout_14.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)

        self.tabWidgetHome.addTab(self.tabUploadData, "")
        self.tabQuickParts = QWidget()
        self.tabQuickParts.setObjectName("tabQuickParts")
        self.gridLayout_6 = QGridLayout(self.tabQuickParts)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBoxAutomationParts = QGroupBox(self.tabQuickParts)
        self.groupBoxAutomationParts.setObjectName("groupBoxAutomationParts")
        self.gridLayout_5 = QGridLayout(self.groupBoxAutomationParts)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_8 = QGroupBox(self.groupBoxAutomationParts)
        self.groupBox_8.setObjectName("groupBox_8")
        self.groupBox_8.setEnabled(False)
        self.gridLayout_13 = QGridLayout(self.groupBox_8)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QLabel(self.groupBox_8)
        self.label_5.setObjectName("label_5")
        self.label_5.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )
        self.label_5.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalSpacer_7 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.pushButton_4 = QPushButton(self.groupBox_8)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_6.addWidget(self.pushButton_4)

        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.verticalLayout_5.setStretch(0, 10)

        self.gridLayout_13.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.gridLayout_5.addWidget(self.groupBox_8, 1, 2, 1, 1)

        self.groupBox_9 = QGroupBox(self.groupBoxAutomationParts)
        self.groupBox_9.setObjectName("groupBox_9")
        self.groupBox_9.setEnabled(False)
        self.gridLayout_18 = QGridLayout(self.groupBox_9)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_8 = QLabel(self.groupBox_9)
        self.label_8.setObjectName("label_8")
        self.label_8.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )
        self.label_8.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.label_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalSpacer_9 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.pushButton_6 = QPushButton(self.groupBox_9)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_9.addWidget(self.pushButton_6)

        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.verticalLayout_7.setStretch(0, 10)

        self.gridLayout_18.addLayout(self.verticalLayout_7, 0, 0, 1, 1)

        self.gridLayout_5.addWidget(self.groupBox_9, 2, 2, 1, 1)

        self.groupBoxGetReports = QGroupBox(self.groupBoxAutomationParts)
        self.groupBoxGetReports.setObjectName("groupBoxGetReports")
        self.groupBoxGetReports.setEnabled(False)
        self.gridLayout_7 = QGridLayout(self.groupBoxGetReports)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelGetReports = QLabel(self.groupBoxGetReports)
        self.labelGetReports.setObjectName("labelGetReports")
        self.labelGetReports.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )
        self.labelGetReports.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.labelGetReports)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dateEditReportFrom = QDateEdit(self.groupBoxGetReports)
        self.dateEditReportFrom.setObjectName("dateEditReportFrom")
        self.dateEditReportFrom.setMinimumSize(QSize(0, 35))
        self.dateEditReportFrom.setLayoutDirection(
            Qt.LayoutDirection.RightToLeft
        )
        self.dateEditReportFrom.setButtonSymbols(
            QAbstractSpinBox.ButtonSymbols.UpDownArrows
        )
        self.dateEditReportFrom.setProperty("showGroupSeparator", False)
        self.dateEditReportFrom.setCurrentSection(
            QDateTimeEdit.Section.DaySection
        )
        self.dateEditReportFrom.setCalendarPopup(False)
        self.dateEditReportFrom.setDate(QDate(2000, 1, 1))

        self.horizontalLayout_3.addWidget(self.dateEditReportFrom)

        self.dateEditReportTo = QDateEdit(self.groupBoxGetReports)
        self.dateEditReportTo.setObjectName("dateEditReportTo")
        self.dateEditReportTo.setMinimumSize(QSize(0, 35))
        self.dateEditReportTo.setButtonSymbols(
            QAbstractSpinBox.ButtonSymbols.UpDownArrows
        )
        self.dateEditReportTo.setCurrentSection(
            QDateTimeEdit.Section.DaySection
        )
        self.dateEditReportTo.setCalendarPopup(False)

        self.horizontalLayout_3.addWidget(self.dateEditReportTo)

        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.pushButtonGetDatedReport = QPushButton(self.groupBoxGetReports)
        self.pushButtonGetDatedReport.setObjectName("pushButtonGetDatedReport")
        self.pushButtonGetDatedReport.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_3.addWidget(self.pushButtonGetDatedReport)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2.setStretch(0, 10)

        self.gridLayout_7.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.gridLayout_5.addWidget(self.groupBoxGetReports, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.groupBoxAutomationParts)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setEnabled(False)
        self.gridLayout_8 = QGridLayout(self.groupBox_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )
        self.label_3.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalLayout_3.setStretch(0, 10)

        self.gridLayout_8.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.gridLayout_5.addWidget(self.groupBox_3, 0, 2, 1, 1)

        self.groupBox_7 = QGroupBox(self.groupBoxAutomationParts)
        self.groupBox_7.setObjectName("groupBox_7")
        self.groupBox_7.setEnabled(False)
        self.gridLayout_12 = QGridLayout(self.groupBox_7)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QLabel(self.groupBox_7)
        self.label_4.setObjectName("label_4")
        self.label_4.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )
        self.label_4.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalSpacer_6 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.pushButton_3 = QPushButton(self.groupBox_7)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_5.addWidget(self.pushButton_3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.verticalLayout_4.setStretch(0, 10)

        self.gridLayout_12.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.gridLayout_5.addWidget(self.groupBox_7, 1, 0, 1, 1)

        self.groupBox_13 = QGroupBox(self.groupBoxAutomationParts)
        self.groupBox_13.setObjectName("groupBox_13")
        self.groupBox_13.setEnabled(False)
        self.gridLayout_19 = QGridLayout(self.groupBox_13)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_9 = QLabel(self.groupBox_13)
        self.label_9.setObjectName("label_9")
        self.label_9.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )
        self.label_9.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalSpacer_10 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_11.addItem(self.horizontalSpacer_10)

        self.pushButton_7 = QPushButton(self.groupBox_13)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_11.addWidget(self.pushButton_7)

        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.verticalLayout_8.setStretch(0, 10)

        self.gridLayout_19.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.gridLayout_5.addWidget(self.groupBox_13, 2, 0, 1, 1)

        self.groupBox_14 = QGroupBox(self.groupBoxAutomationParts)
        self.groupBox_14.setObjectName("groupBox_14")
        self.groupBox_14.setEnabled(False)
        self.gridLayout_20 = QGridLayout(self.groupBox_14)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_11 = QLabel(self.groupBox_14)
        self.label_11.setObjectName("label_11")
        self.label_11.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )
        self.label_11.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.label_11)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.horizontalSpacer_11 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_19.addItem(self.horizontalSpacer_11)

        self.pushButton_8 = QPushButton(self.groupBox_14)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_19.addWidget(self.pushButton_8)

        self.verticalLayout_9.addLayout(self.horizontalLayout_19)

        self.verticalLayout_9.setStretch(0, 10)

        self.gridLayout_20.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.gridLayout_5.addWidget(self.groupBox_14, 0, 1, 1, 1)

        self.groupBox_15 = QGroupBox(self.groupBoxAutomationParts)
        self.groupBox_15.setObjectName("groupBox_15")
        self.groupBox_15.setEnabled(False)
        self.gridLayout_21 = QGridLayout(self.groupBox_15)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_12 = QLabel(self.groupBox_15)
        self.label_12.setObjectName("label_12")
        self.label_12.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )
        self.label_12.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.label_12)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.horizontalSpacer_12 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_20.addItem(self.horizontalSpacer_12)

        self.pushButton_9 = QPushButton(self.groupBox_15)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_20.addWidget(self.pushButton_9)

        self.verticalLayout_10.addLayout(self.horizontalLayout_20)

        self.verticalLayout_10.setStretch(0, 10)

        self.gridLayout_21.addLayout(self.verticalLayout_10, 0, 0, 1, 1)

        self.gridLayout_5.addWidget(self.groupBox_15, 1, 1, 1, 1)

        self.groupBox_16 = QGroupBox(self.groupBoxAutomationParts)
        self.groupBox_16.setObjectName("groupBox_16")
        self.groupBox_16.setEnabled(False)
        self.gridLayout_22 = QGridLayout(self.groupBox_16)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_13 = QLabel(self.groupBox_16)
        self.label_13.setObjectName("label_13")
        self.label_13.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )
        self.label_13.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_13)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.horizontalSpacer_13 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_21.addItem(self.horizontalSpacer_13)

        self.pushButton_10 = QPushButton(self.groupBox_16)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_21.addWidget(self.pushButton_10)

        self.verticalLayout_11.addLayout(self.horizontalLayout_21)

        self.verticalLayout_11.setStretch(0, 10)

        self.gridLayout_22.addLayout(self.verticalLayout_11, 0, 0, 1, 1)

        self.gridLayout_5.addWidget(self.groupBox_16, 2, 1, 1, 1)

        self.gridLayout_6.addWidget(self.groupBoxAutomationParts, 1, 0, 1, 1)

        self.labelWarningAboutQuickParts = QLabel(self.tabQuickParts)
        self.labelWarningAboutQuickParts.setObjectName(
            "labelWarningAboutQuickParts"
        )
        self.labelWarningAboutQuickParts.setFont(font5)
        self.labelWarningAboutQuickParts.setStyleSheet("color:yellow")
        self.labelWarningAboutQuickParts.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.gridLayout_6.addWidget(self.labelWarningAboutQuickParts, 0, 0, 1, 1)

        self.tabWidgetHome.addTab(self.tabQuickParts, "")
        self.tabShortcuts = QWidget()
        self.tabShortcuts.setObjectName("tabShortcuts")
        self.gridLayout_15 = QGridLayout(self.tabShortcuts)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_2 = QLabel(self.tabShortcuts)
        self.label_2.setObjectName("label_2")

        self.verticalLayout_17.addWidget(self.label_2)

        self.tableWidget = QTableWidget(self.tabShortcuts)
        if self.tableWidget.columnCount() < 2:
            self.tableWidget.setColumnCount(2)
        font8 = QFont()
        font8.setFamilies(["Cairo"])
        font8.setBold(True)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font8)
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font8)
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        if self.tableWidget.rowCount() < 20:
            self.tableWidget.setRowCount(20)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(2, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(3, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(4, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(4, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(5, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(5, 1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(6, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(7, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(8, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(9, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(9, 1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(10, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setItem(10, 1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(11, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(12, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(13, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget.setItem(13, 1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(14, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(15, 0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget.setItem(15, 1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(16, 0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(17, 0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget.setItem(17, 1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(18, 0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget.setItem(18, 1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(19, 0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget.setItem(19, 1, __qtablewidgetitem39)
        self.tableWidget.setObjectName("tableWidget")
        font9 = QFont()
        font9.setFamilies(["Cairo"])
        font9.setPointSize(10)
        font9.setBold(False)
        font9.setKerning(True)
        self.tableWidget.setFont(font9)
        self.tableWidget.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.tableWidget.setSizeAdjustPolicy(
            QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow
        )
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.PenStyle.DotLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setRowCount(20)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(235)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)

        self.verticalLayout_17.addWidget(self.tableWidget)

        self.gridLayout_15.addLayout(self.verticalLayout_17, 0, 0, 1, 1)

        self.tabWidgetHome.addTab(self.tabShortcuts, "")

        self.gridLayout_2.addWidget(self.tabWidgetHome, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.gridLayout_10.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindowHome.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindowHome)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        MainWindowHome.setStatusBar(self.statusbar)
        QWidget.setTabOrder(
            self.lineEditCreatorName, self.lineEditAccountCreatorAccountNumber
        )
        QWidget.setTabOrder(
            self.lineEditAccountCreatorAccountNumber, self.comboBoxBankName
        )
        QWidget.setTabOrder(self.comboBoxBankName, self.spinBoxTransactionAmount)
        QWidget.setTabOrder(self.spinBoxTransactionAmount, self.pushButtonAdd)
        QWidget.setTabOrder(self.pushButtonAdd, self.pushButtonNextLevel)
        QWidget.setTabOrder(self.pushButtonNextLevel, self.pushButtonRefresh)
        QWidget.setTabOrder(self.pushButtonRefresh, self.tableWidgetData)
        QWidget.setTabOrder(self.tableWidgetData, self.pushButtonDelete)
        QWidget.setTabOrder(self.pushButtonDelete, self.tabWidgetHome)
        QWidget.setTabOrder(self.tabWidgetHome, self.radioButtonAccountStatus)
        QWidget.setTabOrder(
            self.radioButtonAccountStatus, self.radioButtonActivateAutoLogin
        )
        QWidget.setTabOrder(
            self.radioButtonActivateAutoLogin, self.radioButtonActivateAutoUpload
        )
        QWidget.setTabOrder(
            self.radioButtonActivateAutoUpload, self.lineEditDefaultUsername
        )
        QWidget.setTabOrder(self.lineEditDefaultUsername, self.lineEditDefaultPassword)
        QWidget.setTabOrder(
            self.lineEditDefaultPassword, self.lineEditDefaultAccountNumber
        )
        QWidget.setTabOrder(
            self.lineEditDefaultAccountNumber, self.lineEditDefaultBankName
        )
        QWidget.setTabOrder(
            self.lineEditDefaultBankName, self.lineEditDefaultCustomerName
        )
        QWidget.setTabOrder(self.lineEditDefaultCustomerName, self.lineEditXLSXPath)
        QWidget.setTabOrder(self.lineEditXLSXPath, self.pushButtonCopyUsername)
        QWidget.setTabOrder(self.pushButtonCopyUsername, self.pushButtonCopyPassword)
        QWidget.setTabOrder(
            self.pushButtonCopyPassword, self.pushButtonCopyAccountNumber
        )
        QWidget.setTabOrder(
            self.pushButtonCopyAccountNumber, self.pushButtonCopyBankName
        )
        QWidget.setTabOrder(
            self.pushButtonCopyBankName, self.pushButtonCopyCustomerName
        )
        QWidget.setTabOrder(self.pushButtonCopyCustomerName, self.pushButtonCopyPath)
        QWidget.setTabOrder(self.pushButtonCopyPath, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.pushButton_6)
        QWidget.setTabOrder(self.pushButton_6, self.dateEditReportFrom)
        QWidget.setTabOrder(self.dateEditReportFrom, self.dateEditReportTo)
        QWidget.setTabOrder(self.dateEditReportTo, self.pushButtonGetDatedReport)
        QWidget.setTabOrder(self.pushButtonGetDatedReport, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.pushButton_7)
        QWidget.setTabOrder(self.pushButton_7, self.pushButton_8)
        QWidget.setTabOrder(self.pushButton_8, self.pushButton_9)
        QWidget.setTabOrder(self.pushButton_9, self.pushButton_10)
        QWidget.setTabOrder(self.pushButton_10, self.tableWidget)

        self.retranslateUi(MainWindowHome)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidgetHome.setCurrentIndex(0)
        self.pushButtonAdd.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindowHome)

    # setupUi

    def retranslateUi(self, MainWindowHome):
        MainWindowHome.setWindowTitle(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0644\u0631\u0626\u064a\u0633\u064a\u0629 | \u0628\u0631\u0646\u0627\u0645\u062c \u0627\u0644\u0628\u0646\u0643",
                None,
            )
        )
        # if QT_CONFIG(statustip)
        MainWindowHome.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.radioButtonAccountStatus.setText(
            QCoreApplication.translate(
                "MainWindowHome", "\u063a\u064a\u0631 \u0645\u062a\u0635\u0644", None
            )
        )
        self.labelHomeTitle.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0644\u0631\u0626\u064a\u0633\u064a\u0629",
                None,
            )
        )
        self.pushButtonRefresh.setText(
            QCoreApplication.translate(
                "MainWindowHome", "\u062a\u062d\u062f\u064a\u062b", None
            )
        )
        self.groupBox_4.setTitle(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u062f\u062e\u0627\u0644 \u0645\u0639\u0627\u0645\u0644\u0647 \u062c\u062f\u064a\u062f\u0647",
                None,
            )
        )
        self.pushButtonAdd.setText(
            QCoreApplication.translate(
                "MainWindowHome", "\u0627\u0636\u0627\u0641\u0647", None
            )
        )
        # if QT_CONFIG(shortcut)
        self.pushButtonAdd.setShortcut(
            QCoreApplication.translate("MainWindowHome", "Ctrl+Shift+A", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.pushButtonDelete.setText(
            QCoreApplication.translate("MainWindowHome", "\u062d\u0630\u0641", None)
        )
        # if QT_CONFIG(shortcut)
        self.pushButtonDelete.setShortcut(
            QCoreApplication.translate("MainWindowHome", "Ctrl+Shift+D", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.labelMoney.setText(
            QCoreApplication.translate("MainWindowHome", "\u0635\u0641\u0631", None)
        )
        self.spinBoxTransactionAmount.setSpecialValueText("")
        self.spinBoxTransactionAmount.setSuffix("")
        self.spinBoxTransactionAmount.setPrefix(
            QCoreApplication.translate("MainWindowHome", "\u062c.\u0645 ", None)
        )
        self.label_10.setText(
            QCoreApplication.translate(
                "MainWindowHome", "\u0627\u0644\u0645\u0628\u0644\u063a", None
            )
        )
        self.comboBoxBankName.setCurrentText("")
        self.comboBoxBankName.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u062f\u062e\u0644 \u0627\u0633\u0645 \u0627\u0644\u0628\u0646\u0643",
                None,
            )
        )
        self.lineEditAccountCreatorAccountNumber.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u062f\u062e\u0644 \u0631\u0642\u0645 \u0627\u0644\u062d\u0633\u0627\u0628 \u0627\u0644\u0645\u0643\u0648\u0646 \u0645\u0646 16 \u0631\u0642\u0645",
                None,
            )
        )
        self.lineEditCreatorName.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u062f\u062e\u0644 \u0627\u0633\u0645 \u0627\u0644\u0639\u0645\u064a\u0644 \u0628\u0627\u0644\u0644\u063a\u0629 \u0627\u0644\u0639\u0631\u0628\u064a\u0629 \u0648 \u0644\u0627 \u064a\u0642\u0644 \u0639\u0646 10 \u0627\u062d\u0631\u0641",
                None,
            )
        )
        self.groupBox_5.setTitle(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u062c\u062f\u0648\u0644 \u0627\u0644\u0645\u0639\u0627\u0645\u0644\u0627\u062a \u0627\u0644\u062a\u064a \u0633\u064a\u062a\u0645 \u0631\u0641\u0639\u0647\u0627",
                None,
            )
        )
        ___qtablewidgetitem = self.tableWidgetData.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0633\u0645 \u0627\u0644\u0639\u0645\u064a\u0644",
                None,
            )
        )
        ___qtablewidgetitem1 = self.tableWidgetData.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0631\u0642\u0645 \u0627\u0644\u062d\u0633\u0627\u0628",
                None,
            )
        )
        ___qtablewidgetitem2 = self.tableWidgetData.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0642\u064a\u0645\u0629 \u0627\u0644\u062a\u062d\u0648\u064a\u0644",
                None,
            )
        )
        ___qtablewidgetitem3 = self.tableWidgetData.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0633\u0645 \u0627\u0644\u0628\u0646\u0643",
                None,
            )
        )
        ___qtablewidgetitem4 = self.tableWidgetData.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0643\u0648\u062f \u0627\u0644\u0628\u0646\u0643",
                None,
            )
        )
        self.pushButtonNextLevel.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0646\u0642\u0631 \u0647\u0646\u0627 \u0644\u0627\u0646\u0634\u0627\u0621 \u0645\u0644\u0641 \u0627\u0644\u0627\u0643\u0633\u0644 \u0644\u0644\u0628\u064a\u0627\u0646\u0627\u062a \u0627\u0644\u0645\u062f\u062e\u0644\u0647 \u0627\u0639\u0644\u0627\u0647 \u0648\u0627\u0644\u0627\u0646\u062a\u0642\u0627\u0644 \u0627\u0644\u064a \u0627\u0644\u0645\u0631\u062d\u0644\u0629 \u0627\u0644\u062a\u0627\u0644\u064a\u0647",
                None,
            )
        )
        self.tabWidgetHome.setTabText(
            self.tabWidgetHome.indexOf(self.tabData),
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0645\u0631\u062d\u0644\u0629 \u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u0628\u064a\u0627\u0646\u0627\u062a",
                None,
            ),
        )
        self.groupBox_10.setTitle(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0645\u0648\u0642\u0639 \u0627\u0644\u0628\u0646\u0643",
                None,
            )
        )
        self.label.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0647\u0630\u0647 \u062e\u0627\u0635\u064a\u0629 \u062f\u0645\u062c \u0627\u0644\u0645\u0648\u0642\u0639 \u0641\u064a \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c\u060c \u0648\u0647\u064a \u062a\u062d\u062a \u0627\u0644\u0627\u062e\u062a\u0628\u0627\u0631\u060c \u0644\u0630\u0627 \u0627\u0646 \u062d\u062f\u062b \u062e\u0637\u0623 \u0627\u0636\u063a\u0637 \u0639\u0644\u064a F9 \u0644\u0644\u0639\u0645\u0644 \u0628\u0634\u0643\u0644 \u0645\u0633\u062a\u0642\u0644",
                None,
            )
        )
        self.labelWebsiteLoadPrpgress.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u062c\u0627\u0631\u064a \u0627\u0644\u062a\u062d\u0645\u064a\u0644 .. \u0627\u0646\u0638\u0631 \u0642\u0644\u064a\u0644\u0627",
                None,
            )
        )
        self.groupBox_12.setTitle(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0628\u064a\u0627\u0646\u0627\u062a \u0627\u0641\u062a\u0631\u0627\u0636\u064a\u0647 - \u0647\u0630\u0647 \u0627\u0644\u0628\u064a\u0627\u0646\u0627\u062a \u0644\u0645\u0633\u0627\u0639\u062f\u062a\u0643 \u0639\u0644\u064a \u062a\u0630\u0643\u0631\u0647\u0627",
                None,
            )
        )
        self.radioButtonActivateAutoLogin.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u062a\u0634\u063a\u064a\u0644 \u062e\u0627\u0635\u064a\u0629 \u0627\u0644\u062f\u062e\u0648\u0644 \u0627\u0644\u0627\u0644\u064a",
                None,
            )
        )
        self.radioButtonActivateAutoUpload.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u062a\u0634\u063a\u064a\u0644 \u062e\u0627\u0635\u064a\u0629 \u0627\u0644\u0631\u0641\u0639 \u0627\u0644\u0627\u0644\u064a",
                None,
            )
        )
        self.label_14.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0647\u0630\u0647 \u0627\u0644\u0628\u064a\u0627\u0646\u0627\u062a \u0644\u0645\u0633\u0627\u0639\u062f\u062a\u0643 \u0641\u0642\u0637 \u0639\u0644\u064a \u0633\u0631\u0639\u0629 \u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644\u060c \u0648\u0644\u0633\u062a \u0645\u0636\u0637\u0631\u0627 \u0639\u0644\u064a \u0627\u0644\u0627\u0637\u0644\u0627\u0642 \u0627\u0644\u064a \u0627\u0633\u062e\u062f\u0627\u0645\u0647\u0627. \u0644\u0646\u0641\u0631\u0636 \u0645\u062b\u0644\u0627 \u0627\u0646\u0643 \u062a\u0631\u064a\u062f \u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644 \u0627\u0644\u064a \u0627\u0644\u0645\u0648\u0642\u0639: \u0641\u0623\u0646\u062a \u062a\u062d\u062a\u0627\u062c \u0627\u0644\u064a \u0627\u0633\u0645 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u060c \u064a\u062a\u0643\u0648\u0646 \u0645\u0646 16 \u0631\u0642\u0645\u060c \u0648\u0643\u0644\u0645\u0629 \u0627\u0644\u0645\u0631\u0648\u0631. \u0641\u0647\u0644 \u0645\u0646 \u0627\u0644\u0645\u0639\u0642\u0648\u0644"
                " \u0627\u0646\u0646\u064a \u0641\u064a \u0643\u0644 \u0645\u0631\u0629 \u0627\u0643\u062a\u0628 \u0627\u0633\u0645 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645 \u0628\u062f\u0648\u0646 \u0627\u0646 \u062a\u0643\u0648\u0646 \u0647\u0646\u0627\u0643 \u0648\u0633\u064a\u0644\u0629 \u0644\u0627\u062f\u062e\u0627\u0644\u0647 \u0628\u0636\u063a\u0637\u0629 \u0632\u0631\u061f \u0628\u0627\u0644\u0637\u0628\u0639 \u0644\u0627. \u0644\u0630\u0627 \u062c\u0639\u0644\u0646\u0627 \u0644\u0643 \u062a\u0644\u0643 \u0627\u0644\u062e\u0627\u0646\u0627\u062a \u0628\u0627\u0644\u0627\u0633\u0641\u0644 \u0644\u062a\u0633\u0647\u064a\u0644 \u0630\u0644\u0643.",
                None,
            )
        )
        self.label_19.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0633\u0645 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645",
                None,
            )
        )
        self.label_18.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0643\u0644\u0645\u0629 \u0627\u0644\u0633\u0631",
                None,
            )
        )
        self.label_20.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0631\u0642\u0645 \u062d\u0633\u0627\u0628 \u0627\u0641\u062a\u0631\u0627\u0636\u064a",
                None,
            )
        )
        self.label_21.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0633\u0645 \u0628\u0646\u0643 \u0627\u0641\u062a\u0631\u0627\u0636\u064a",
                None,
            )
        )
        self.label_22.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0633\u0645 \u0639\u0645\u064a\u0644 \u0627\u0641\u062a\u0631\u0627\u0636\u064a",
                None,
            )
        )
        self.label_6.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0645\u0644\u0641 \u0627\u0644\u0627\u0643\u0633\u0644",
                None,
            )
        )
        self.lineEditDefaultUsername.setText("")
        self.lineEditDefaultUsername.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u062f\u062e\u0644 \u0627\u0633\u0645 \u0645\u0633\u062a\u062e\u062f\u0645 \u0627\u0641\u062a\u0631\u0627\u0636\u064a",
                None,
            )
        )
        self.lineEditDefaultPassword.setInputMask("")
        self.lineEditDefaultPassword.setText("")
        self.lineEditDefaultPassword.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u062f\u062e\u0644 \u0643\u0644\u0645\u0629 \u0633\u0631 \u0627\u0641\u062a\u0631\u0627\u0636\u064a\u0647",
                None,
            )
        )
        self.lineEditDefaultAccountNumber.setText("")
        self.lineEditDefaultAccountNumber.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u062f\u062e\u0644 \u0631\u0642\u0645 \u062d\u0633\u0627\u0628 \u0627\u0641\u062a\u0631\u0627\u0636\u064a",
                None,
            )
        )
        self.lineEditDefaultBankName.setText("")
        self.lineEditDefaultBankName.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u062f\u062e\u0644 \u0627\u0633\u0645 \u0628\u0646\u0643 \u0627\u0641\u062a\u0631\u0627\u0636\u064a",
                None,
            )
        )
        self.lineEditDefaultCustomerName.setText("")
        self.lineEditDefaultCustomerName.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u062f\u062e\u0644 \u0627\u0633\u0645 \u0639\u0645\u064a\u0644 \u0627\u0641\u062a\u0631\u0627\u0636\u064a",
                None,
            )
        )
        self.lineEditXLSXPath.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0646\u062a\u0638\u0631 \u0645\u0633\u0627\u0631 \u0645\u0644\u0641 \u0627\u0644\u0627\u0643\u0633\u0644",
                None,
            )
        )
        self.pushButtonCopyUsername.setText(
            QCoreApplication.translate("MainWindowHome", "\u0646\u0633\u062e", None)
        )
        self.pushButtonCopyPassword.setText(
            QCoreApplication.translate("MainWindowHome", "\u0646\u0633\u062e", None)
        )
        self.pushButtonCopyAccountNumber.setText(
            QCoreApplication.translate("MainWindowHome", "\u0646\u0633\u062e", None)
        )
        self.pushButtonCopyBankName.setText(
            QCoreApplication.translate("MainWindowHome", "\u0646\u0633\u062e", None)
        )
        self.pushButtonCopyCustomerName.setText(
            QCoreApplication.translate("MainWindowHome", "\u0646\u0633\u062e", None)
        )
        self.pushButtonCopyPath.setText(
            QCoreApplication.translate("MainWindowHome", "\u0646\u0633\u062e", None)
        )
        self.tabWidgetHome.setTabText(
            self.tabWidgetHome.indexOf(self.tabUploadData),
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0645\u0631\u062d\u0644\u0629 \u0631\u0641\u0639 \u0627\u0644\u0628\u064a\u0627\u0646\u0627\u062a",
                None,
            ),
        )
        self.groupBoxAutomationParts.setTitle(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u062a\u0645\u062a\u0647 - \u0647\u0630\u0647 \u0627\u0644\u0639\u0645\u0644\u064a\u0647 \u0644\u0646 \u062a\u062a\u062f\u062e\u0644 \u0628\u0647\u0627 \u0628\u0644 \u0633\u064a\u0642\u0648\u0645 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0628\u0641\u0639\u0644 \u0643\u0644 \u0634\u0626",
                None,
            )
        )
        self.groupBox_8.setTitle(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0633\u062a\u062d\u0631\u0627\u062c \u062a\u0642\u0631\u064a\u0631",
                None,
            )
        )
        self.label_5.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0633\u064a\u0642\u0648\u0645 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0628\u0634\u0643\u0644 \u0627\u0648\u062a\u0648\u0645\u0627\u062a\u064a\u0643\u064a \u0628\u0627\u0644\u062f\u062e\u0648\u0644 \u0627\u0644\u064a \u0645\u0648\u0642\u0639 \u0627\u0644\u0628\u0646\u0643 \u0648\u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644 \u0628\u0634\u0643\u0644 \u062a\u0644\u0642\u0627\u0626\u064a \u0628\u0646\u0627\u0621\u0627 \u0639\u0644\u064a \u0627\u0644\u0628\u064a\u0627\u0646\u062a \u0627\u0644\u0627\u0641\u062a\u0631\u0627\u0636\u064a\u0647 \u0627\u0644\u0645\u062f\u062e\u0644\u0629 \u0645\u0646 \u0642\u0628\u0644 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u060c \u0648\u0628\u0639\u062f \u0630\u0644\u0643 \u064a\u0636\u063a\u0637 \u0639\u0644\u064a \u0639\u0631\u0636 \u0627\u0644\u062a\u0642\u0627\u0631\u064a\u0631 \u0648\u064a\u062e\u062a\u0627\u0631 \u0627\u0644\u0645\u062f\u0629 \u0648\u0643\u0630\u0644\u0643 \u0646\u0648\u0639 \u0627\u0644\u0645\u0644\u0641 \u0627\u0644\u0645"
                "\u062e\u0631\u062c",
                None,
            )
        )
        self.pushButton_4.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u062d\u0635\u0644 \u0639\u0644\u064a \u0627\u0644\u062a\u0642\u0631\u064a\u0631",
                None,
            )
        )
        self.groupBox_9.setTitle(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0633\u062a\u062d\u0631\u0627\u062c \u062a\u0642\u0631\u064a\u0631",
                None,
            )
        )
        self.label_8.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0633\u064a\u0642\u0648\u0645 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0628\u0634\u0643\u0644 \u0627\u0648\u062a\u0648\u0645\u0627\u062a\u064a\u0643\u064a \u0628\u0627\u0644\u062f\u062e\u0648\u0644 \u0627\u0644\u064a \u0645\u0648\u0642\u0639 \u0627\u0644\u0628\u0646\u0643 \u0648\u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644 \u0628\u0634\u0643\u0644 \u062a\u0644\u0642\u0627\u0626\u064a \u0628\u0646\u0627\u0621\u0627 \u0639\u0644\u064a \u0627\u0644\u0628\u064a\u0627\u0646\u062a \u0627\u0644\u0627\u0641\u062a\u0631\u0627\u0636\u064a\u0647 \u0627\u0644\u0645\u062f\u062e\u0644\u0629 \u0645\u0646 \u0642\u0628\u0644 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u060c \u0648\u0628\u0639\u062f \u0630\u0644\u0643 \u064a\u0636\u063a\u0637 \u0639\u0644\u064a \u0639\u0631\u0636 \u0627\u0644\u062a\u0642\u0627\u0631\u064a\u0631 \u0648\u064a\u062e\u062a\u0627\u0631 \u0627\u0644\u0645\u062f\u0629 \u0648\u0643\u0630\u0644\u0643 \u0646\u0648\u0639 \u0627\u0644\u0645\u0644\u0641 \u0627\u0644\u0645"
                "\u062e\u0631\u062c",
                None,
            )
        )
        self.pushButton_6.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u062d\u0635\u0644 \u0639\u0644\u064a \u0627\u0644\u062a\u0642\u0631\u064a\u0631",
                None,
            )
        )
        self.groupBoxGetReports.setTitle(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0633\u062a\u062e\u0631\u0627\u062c \u062a\u0642\u0631\u064a\u0631",
                None,
            )
        )
        self.labelGetReports.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0633\u064a\u0642\u0648\u0645 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0628\u0634\u0643\u0644 \u0627\u0648\u062a\u0648\u0645\u0627\u062a\u064a\u0643\u064a \u0628\u0627\u0644\u062f\u062e\u0648\u0644 \u0627\u0644\u064a \u0645\u0648\u0642\u0639 \u0627\u0644\u0628\u0646\u0643 \u0648\u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644 \u0628\u0634\u0643\u0644 \u062a\u0644\u0642\u0627\u0626\u064a \u0628\u0646\u0627\u0621\u0627 \u0639\u0644\u064a \u0627\u0644\u0628\u064a\u0627\u0646\u062a \u0627\u0644\u0627\u0641\u062a\u0631\u0627\u0636\u064a\u0647 \u0627\u0644\u0645\u062f\u062e\u0644\u0629 \u0645\u0646 \u0642\u0628\u0644 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u060c \u0648\u0628\u0639\u062f \u0630\u0644\u0643 \u064a\u0636\u063a\u0637 \u0639\u0644\u064a \u0639\u0631\u0636 \u0627\u0644\u062a\u0642\u0627\u0631\u064a\u0631 \u0648\u064a\u062e\u062a\u0627\u0631 \u0627\u0644\u0645\u062f\u0629 \u0648\u0643\u0630\u0644\u0643 \u0646\u0648\u0639 \u0627\u0644\u0645\u0644\u0641 \u0627\u0644\u0645"
                "\u062e\u0631\u062c",
                None,
            )
        )
        self.dateEditReportFrom.setSpecialValueText("")
        self.dateEditReportTo.setSpecialValueText("")
        self.pushButtonGetDatedReport.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u062d\u0635\u0644 \u0639\u0644\u064a \u0627\u0644\u062a\u0642\u0631\u064a\u0631",
                None,
            )
        )
        self.groupBox_3.setTitle(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0633\u062a\u062d\u0631\u0627\u062c \u062a\u0642\u0631\u064a\u0631",
                None,
            )
        )
        self.label_3.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0633\u064a\u0642\u0648\u0645 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0628\u0634\u0643\u0644 \u0627\u0648\u062a\u0648\u0645\u0627\u062a\u064a\u0643\u064a \u0628\u0627\u0644\u062f\u062e\u0648\u0644 \u0627\u0644\u064a \u0645\u0648\u0642\u0639 \u0627\u0644\u0628\u0646\u0643 \u0648\u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644 \u0628\u0634\u0643\u0644 \u062a\u0644\u0642\u0627\u0626\u064a \u0628\u0646\u0627\u0621\u0627 \u0639\u0644\u064a \u0627\u0644\u0628\u064a\u0627\u0646\u062a \u0627\u0644\u0627\u0641\u062a\u0631\u0627\u0636\u064a\u0647 \u0627\u0644\u0645\u062f\u062e\u0644\u0629 \u0645\u0646 \u0642\u0628\u0644 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u060c \u0648\u0628\u0639\u062f \u0630\u0644\u0643 \u064a\u0636\u063a\u0637 \u0639\u0644\u064a \u0639\u0631\u0636 \u0627\u0644\u062a\u0642\u0627\u0631\u064a\u0631 \u0648\u064a\u062e\u062a\u0627\u0631 \u0627\u0644\u0645\u062f\u0629 \u0648\u0643\u0630\u0644\u0643 \u0646\u0648\u0639 \u0627\u0644\u0645\u0644\u0641 \u0627\u0644\u0645"
                "\u062e\u0631\u062c",
                None,
            )
        )
        self.pushButton_2.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u062d\u0635\u0644 \u0639\u0644\u064a \u0627\u0644\u062a\u0642\u0631\u064a\u0631",
                None,
            )
        )
        self.groupBox_7.setTitle(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0633\u062a\u062d\u0631\u0627\u062c \u062a\u0642\u0631\u064a\u0631",
                None,
            )
        )
        self.label_4.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0633\u064a\u0642\u0648\u0645 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0628\u0634\u0643\u0644 \u0627\u0648\u062a\u0648\u0645\u0627\u062a\u064a\u0643\u064a \u0628\u0627\u0644\u062f\u062e\u0648\u0644 \u0627\u0644\u064a \u0645\u0648\u0642\u0639 \u0627\u0644\u0628\u0646\u0643 \u0648\u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644 \u0628\u0634\u0643\u0644 \u062a\u0644\u0642\u0627\u0626\u064a \u0628\u0646\u0627\u0621\u0627 \u0639\u0644\u064a \u0627\u0644\u0628\u064a\u0627\u0646\u062a \u0627\u0644\u0627\u0641\u062a\u0631\u0627\u0636\u064a\u0647 \u0627\u0644\u0645\u062f\u062e\u0644\u0629 \u0645\u0646 \u0642\u0628\u0644 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u060c \u0648\u0628\u0639\u062f \u0630\u0644\u0643 \u064a\u0636\u063a\u0637 \u0639\u0644\u064a \u0639\u0631\u0636 \u0627\u0644\u062a\u0642\u0627\u0631\u064a\u0631 \u0648\u064a\u062e\u062a\u0627\u0631 \u0627\u0644\u0645\u062f\u0629 \u0648\u0643\u0630\u0644\u0643 \u0646\u0648\u0639 \u0627\u0644\u0645\u0644\u0641 \u0627\u0644\u0645"
                "\u062e\u0631\u062c",
                None,
            )
        )
        self.pushButton_3.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u062d\u0635\u0644 \u0639\u0644\u064a \u0627\u0644\u062a\u0642\u0631\u064a\u0631",
                None,
            )
        )
        self.groupBox_13.setTitle(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0633\u062a\u062d\u0631\u0627\u062c \u062a\u0642\u0631\u064a\u0631",
                None,
            )
        )
        self.label_9.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0633\u064a\u0642\u0648\u0645 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0628\u0634\u0643\u0644 \u0627\u0648\u062a\u0648\u0645\u0627\u062a\u064a\u0643\u064a \u0628\u0627\u0644\u062f\u062e\u0648\u0644 \u0627\u0644\u064a \u0645\u0648\u0642\u0639 \u0627\u0644\u0628\u0646\u0643 \u0648\u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644 \u0628\u0634\u0643\u0644 \u062a\u0644\u0642\u0627\u0626\u064a \u0628\u0646\u0627\u0621\u0627 \u0639\u0644\u064a \u0627\u0644\u0628\u064a\u0627\u0646\u062a \u0627\u0644\u0627\u0641\u062a\u0631\u0627\u0636\u064a\u0647 \u0627\u0644\u0645\u062f\u062e\u0644\u0629 \u0645\u0646 \u0642\u0628\u0644 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u060c \u0648\u0628\u0639\u062f \u0630\u0644\u0643 \u064a\u0636\u063a\u0637 \u0639\u0644\u064a \u0639\u0631\u0636 \u0627\u0644\u062a\u0642\u0627\u0631\u064a\u0631 \u0648\u064a\u062e\u062a\u0627\u0631 \u0627\u0644\u0645\u062f\u0629 \u0648\u0643\u0630\u0644\u0643 \u0646\u0648\u0639 \u0627\u0644\u0645\u0644\u0641 \u0627\u0644\u0645"
                "\u062e\u0631\u062c",
                None,
            )
        )
        self.pushButton_7.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u062d\u0635\u0644 \u0639\u0644\u064a \u0627\u0644\u062a\u0642\u0631\u064a\u0631",
                None,
            )
        )
        self.groupBox_14.setTitle(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0633\u062a\u062d\u0631\u0627\u062c \u062a\u0642\u0631\u064a\u0631",
                None,
            )
        )
        self.label_11.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0633\u064a\u0642\u0648\u0645 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0628\u0634\u0643\u0644 \u0627\u0648\u062a\u0648\u0645\u0627\u062a\u064a\u0643\u064a \u0628\u0627\u0644\u062f\u062e\u0648\u0644 \u0627\u0644\u064a \u0645\u0648\u0642\u0639 \u0627\u0644\u0628\u0646\u0643 \u0648\u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644 \u0628\u0634\u0643\u0644 \u062a\u0644\u0642\u0627\u0626\u064a \u0628\u0646\u0627\u0621\u0627 \u0639\u0644\u064a \u0627\u0644\u0628\u064a\u0627\u0646\u062a \u0627\u0644\u0627\u0641\u062a\u0631\u0627\u0636\u064a\u0647 \u0627\u0644\u0645\u062f\u062e\u0644\u0629 \u0645\u0646 \u0642\u0628\u0644 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u060c \u0648\u0628\u0639\u062f \u0630\u0644\u0643 \u064a\u0636\u063a\u0637 \u0639\u0644\u064a \u0639\u0631\u0636 \u0627\u0644\u062a\u0642\u0627\u0631\u064a\u0631 \u0648\u064a\u062e\u062a\u0627\u0631 \u0627\u0644\u0645\u062f\u0629 \u0648\u0643\u0630\u0644\u0643 \u0646\u0648\u0639 \u0627\u0644\u0645\u0644\u0641 \u0627\u0644\u0645"
                "\u062e\u0631\u062c",
                None,
            )
        )
        self.pushButton_8.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u062d\u0635\u0644 \u0639\u0644\u064a \u0627\u0644\u062a\u0642\u0631\u064a\u0631",
                None,
            )
        )
        self.groupBox_15.setTitle(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0633\u062a\u062d\u0631\u0627\u062c \u062a\u0642\u0631\u064a\u0631",
                None,
            )
        )
        self.label_12.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0633\u064a\u0642\u0648\u0645 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0628\u0634\u0643\u0644 \u0627\u0648\u062a\u0648\u0645\u0627\u062a\u064a\u0643\u064a \u0628\u0627\u0644\u062f\u062e\u0648\u0644 \u0627\u0644\u064a \u0645\u0648\u0642\u0639 \u0627\u0644\u0628\u0646\u0643 \u0648\u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644 \u0628\u0634\u0643\u0644 \u062a\u0644\u0642\u0627\u0626\u064a \u0628\u0646\u0627\u0621\u0627 \u0639\u0644\u064a \u0627\u0644\u0628\u064a\u0627\u0646\u062a \u0627\u0644\u0627\u0641\u062a\u0631\u0627\u0636\u064a\u0647 \u0627\u0644\u0645\u062f\u062e\u0644\u0629 \u0645\u0646 \u0642\u0628\u0644 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u060c \u0648\u0628\u0639\u062f \u0630\u0644\u0643 \u064a\u0636\u063a\u0637 \u0639\u0644\u064a \u0639\u0631\u0636 \u0627\u0644\u062a\u0642\u0627\u0631\u064a\u0631 \u0648\u064a\u062e\u062a\u0627\u0631 \u0627\u0644\u0645\u062f\u0629 \u0648\u0643\u0630\u0644\u0643 \u0646\u0648\u0639 \u0627\u0644\u0645\u0644\u0641 \u0627\u0644\u0645"
                "\u062e\u0631\u062c",
                None,
            )
        )
        self.pushButton_9.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u062d\u0635\u0644 \u0639\u0644\u064a \u0627\u0644\u062a\u0642\u0631\u064a\u0631",
                None,
            )
        )
        self.groupBox_16.setTitle(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0633\u062a\u062d\u0631\u0627\u062c \u062a\u0642\u0631\u064a\u0631",
                None,
            )
        )
        self.label_13.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0633\u064a\u0642\u0648\u0645 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0628\u0634\u0643\u0644 \u0627\u0648\u062a\u0648\u0645\u0627\u062a\u064a\u0643\u064a \u0628\u0627\u0644\u062f\u062e\u0648\u0644 \u0627\u0644\u064a \u0645\u0648\u0642\u0639 \u0627\u0644\u0628\u0646\u0643 \u0648\u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644 \u0628\u0634\u0643\u0644 \u062a\u0644\u0642\u0627\u0626\u064a \u0628\u0646\u0627\u0621\u0627 \u0639\u0644\u064a \u0627\u0644\u0628\u064a\u0627\u0646\u062a \u0627\u0644\u0627\u0641\u062a\u0631\u0627\u0636\u064a\u0647 \u0627\u0644\u0645\u062f\u062e\u0644\u0629 \u0645\u0646 \u0642\u0628\u0644 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u060c \u0648\u0628\u0639\u062f \u0630\u0644\u0643 \u064a\u0636\u063a\u0637 \u0639\u0644\u064a \u0639\u0631\u0636 \u0627\u0644\u062a\u0642\u0627\u0631\u064a\u0631 \u0648\u064a\u062e\u062a\u0627\u0631 \u0627\u0644\u0645\u062f\u0629 \u0648\u0643\u0630\u0644\u0643 \u0646\u0648\u0639 \u0627\u0644\u0645\u0644\u0641 \u0627\u0644\u0645"
                "\u062e\u0631\u062c",
                None,
            )
        )
        self.pushButton_10.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u062d\u0635\u0644 \u0639\u0644\u064a \u0627\u0644\u062a\u0642\u0631\u064a\u0631",
                None,
            )
        )
        self.labelWarningAboutQuickParts.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0647\u0630\u0647 \u0627\u0644\u062e\u0648\u0627\u0635 \u0644\u0627 \u062a\u0639\u0645\u0644 \u062d\u0627\u0644\u064a\u0627\u060c \u0648\u0647\u064a \u062a\u062d\u062a \u0627\u0644\u0627\u062e\u062a\u0628\u0627\u0631 \u0648\u0633\u064a\u062a\u0645 \u062a\u0641\u0639\u064a\u0644\u0647\u0627 \u062d\u064a\u0646 \u0646\u0646\u062a\u0647\u064a \u0645\u0646 \u0627\u0644\u0627\u062e\u062a\u0628\u0627\u0631 \u0645\u0639 \u0627\u0644\u0646\u0633\u062e\u0629 \u0627\u0644\u062c\u062f\u064a\u062f\u0629 \u0628\u0627\u0630\u0646 \u0627\u0644\u0644\u0647",
                None,
            )
        )
        self.tabWidgetHome.setTabText(
            self.tabWidgetHome.indexOf(self.tabQuickParts),
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0645\u0647\u0627\u0645 \u0633\u0631\u064a\u0639\u0647",
                None,
            ),
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u062e\u062a\u0635\u0627\u0631\u0627\u062a \u0647\u0627\u0645\u0629 \u0641\u064a \u062a\u0633\u0631\u064a\u0639 \u0644\u062a\u062d\u0633\u064a\u0646 \u062a\u062c\u0631\u0628\u0629 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645",
                None,
            )
        )
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0644\u0627\u062e\u062a\u0635\u0627\u0631",
                None,
            )
        )
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(
            QCoreApplication.translate(
                "MainWindowHome", "\u0627\u0644\u0648\u0635\u0641", None
            )
        )

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem7.setText(
            QCoreApplication.translate("MainWindowHome", "Ctrl+Tab", None)
        )
        ___qtablewidgetitem8 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem8.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0644\u0627\u0646\u062a\u0642\u0627\u0644 \u0627\u0644\u064a \u0627\u0644\u0635\u0641\u062d\u0629 \u0627\u0644\u062a\u0627\u0644\u064a\u0647 \u0645\u0646 \u0627\u0644\u064a\u0645\u064a\u0646 \u0627\u0644\u064a \u0627\u0644\u064a\u0633\u0627\u0631",
                None,
            )
        )
        ___qtablewidgetitem9 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem9.setText(
            QCoreApplication.translate("MainWindowHome", "Ctrl+Shift+Tab", None)
        )
        ___qtablewidgetitem10 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem10.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0644\u0627\u0646\u062a\u0642\u0627\u0644 \u0627\u0644\u064a \u0627\u0644\u0635\u0641\u062d\u0629 \u0627\u0644\u0633\u0627\u0628\u0642\u0647 \u0645\u0646 \u0627\u0644\u064a\u0633\u0627\u0631 \u0627\u0644\u064a \u0627\u0644\u064a\u0645\u064a\u0646",
                None,
            )
        )
        ___qtablewidgetitem11 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem11.setText(
            QCoreApplication.translate("MainWindowHome", "Insert", None)
        )
        ___qtablewidgetitem12 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem12.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0636\u0627\u0641\u0629 \u0627\u0644\u0628\u064a\u0627\u0646\u0627\u062a \u0641\u064a \u0627\u0644\u0645\u062f\u062e\u0644\u0627\u062a \u0627\u0644\u0639\u0644\u0648\u064a\u0629 \u0627\u0644\u064a \u0627\u0644\u062c\u062f\u0648\u0644 \u0627\u0644\u0633\u0641\u0644\u064a",
                None,
            )
        )
        ___qtablewidgetitem13 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem13.setText(
            QCoreApplication.translate("MainWindowHome", "Refresh", None)
        )
        ___qtablewidgetitem14 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem14.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0639\u0627\u062f\u0629 \u062a\u062d\u0645\u064a\u0644 \u0627\u0644\u062a\u0637\u0628\u064a\u0642",
                None,
            )
        )
        ___qtablewidgetitem15 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem15.setText(
            QCoreApplication.translate("MainWindowHome", "Delete", None)
        )
        ___qtablewidgetitem16 = self.tableWidget.item(4, 1)
        ___qtablewidgetitem16.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u062d\u0630\u0641 \u0627\u0644\u0635\u0641 \u0627\u0644\u062d\u0627\u0644\u064a \u0645\u0646 \u0627\u0644\u062c\u062f\u0648\u0644",
                None,
            )
        )
        ___qtablewidgetitem17 = self.tableWidget.item(5, 0)
        ___qtablewidgetitem17.setText(
            QCoreApplication.translate("MainWindowHome", "F1", None)
        )
        ___qtablewidgetitem18 = self.tableWidget.item(5, 1)
        ___qtablewidgetitem18.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0641\u062a\u062d \u0634\u0627\u0634\u0629 `\u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0627\u0644\u062a\u0637\u0628\u064a\u0642`",
                None,
            )
        )
        ___qtablewidgetitem19 = self.tableWidget.item(6, 0)
        ___qtablewidgetitem19.setText(
            QCoreApplication.translate("MainWindowHome", "F2", None)
        )
        ___qtablewidgetitem20 = self.tableWidget.item(7, 0)
        ___qtablewidgetitem20.setText(
            QCoreApplication.translate("MainWindowHome", "F3", None)
        )
        ___qtablewidgetitem21 = self.tableWidget.item(8, 0)
        ___qtablewidgetitem21.setText(
            QCoreApplication.translate("MainWindowHome", "F4", None)
        )
        ___qtablewidgetitem22 = self.tableWidget.item(9, 0)
        ___qtablewidgetitem22.setText(
            QCoreApplication.translate("MainWindowHome", "F5", None)
        )
        ___qtablewidgetitem23 = self.tableWidget.item(9, 1)
        ___qtablewidgetitem23.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0639\u0627\u062f\u0629 \u062a\u062d\u0645\u064a\u0644 \u0627\u0644\u062a\u0637\u0628\u064a\u0642",
                None,
            )
        )
        ___qtablewidgetitem24 = self.tableWidget.item(10, 0)
        ___qtablewidgetitem24.setText(
            QCoreApplication.translate("MainWindowHome", "F6", None)
        )
        ___qtablewidgetitem25 = self.tableWidget.item(10, 1)
        ___qtablewidgetitem25.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0646\u0634\u0627\u0621 \u0645\u0639\u0627\u0645\u0644\u0629 \u0628\u0628\u064a\u0627\u0646\u0627\u062a \u0627\u0641\u062a\u0631\u0627\u0636\u064a\u0647 - \u062a\u0633\u062a\u062e\u062f\u0645 \u0645\u0646 \u0642\u0628\u0644 \u0627\u0644\u0645\u0637\u0648\u0631 \u0641\u0642\u0637",
                None,
            )
        )
        ___qtablewidgetitem26 = self.tableWidget.item(11, 0)
        ___qtablewidgetitem26.setText(
            QCoreApplication.translate("MainWindowHome", "F7", None)
        )
        ___qtablewidgetitem27 = self.tableWidget.item(12, 0)
        ___qtablewidgetitem27.setText(
            QCoreApplication.translate("MainWindowHome", "F8", None)
        )
        ___qtablewidgetitem28 = self.tableWidget.item(13, 0)
        ___qtablewidgetitem28.setText(
            QCoreApplication.translate("MainWindowHome", "F9", None)
        )
        ___qtablewidgetitem29 = self.tableWidget.item(13, 1)
        ___qtablewidgetitem29.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0641\u062a\u062d \u0645\u0648\u0642\u0639 \u0627\u0644\u0628\u0646\u0643 \u0641\u064a \u0645\u062a\u0635\u0641 \u062e\u0627\u0631\u062c\u064a",
                None,
            )
        )
        ___qtablewidgetitem30 = self.tableWidget.item(14, 0)
        ___qtablewidgetitem30.setText(
            QCoreApplication.translate("MainWindowHome", "F10", None)
        )
        ___qtablewidgetitem31 = self.tableWidget.item(15, 0)
        ___qtablewidgetitem31.setText(
            QCoreApplication.translate("MainWindowHome", "F11", None)
        )
        ___qtablewidgetitem32 = self.tableWidget.item(15, 1)
        ___qtablewidgetitem32.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u062a\u0643\u0628\u064a\u0631 \u0648\u062a\u0635\u063a\u064a\u0631 \u0627\u0644\u0634\u0627\u0634\u0629 \u0627\u0644\u062d\u0627\u0644\u0647",
                None,
            )
        )
        ___qtablewidgetitem33 = self.tableWidget.item(16, 0)
        ___qtablewidgetitem33.setText(
            QCoreApplication.translate("MainWindowHome", "F12", None)
        )
        ___qtablewidgetitem34 = self.tableWidget.item(17, 0)
        ___qtablewidgetitem34.setText(
            QCoreApplication.translate("MainWindowHome", "Ctrl+P", None)
        )
        ___qtablewidgetitem35 = self.tableWidget.item(17, 1)
        ___qtablewidgetitem35.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u062e\u062f \u0644\u0642\u0637\u0629 \u0634\u0627\u0634\u0647 \u0644\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0643\u0645\u0627 \u0647\u0648 \u0627\u0644\u0627\u0646",
                None,
            )
        )
        ___qtablewidgetitem36 = self.tableWidget.item(18, 0)
        ___qtablewidgetitem36.setText(
            QCoreApplication.translate("MainWindowHome", "Esc", None)
        )
        ___qtablewidgetitem37 = self.tableWidget.item(18, 1)
        ___qtablewidgetitem37.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u063a\u0644\u0627\u0642 \u0627\u064a \u0634\u0627\u0634\u0629 \u0641\u0631\u0639\u064a\u0647",
                None,
            )
        )
        ___qtablewidgetitem38 = self.tableWidget.item(19, 0)
        ___qtablewidgetitem38.setText(
            QCoreApplication.translate("MainWindowHome", "Ctrl+Number", None)
        )
        ___qtablewidgetitem39 = self.tableWidget.item(19, 1)
        ___qtablewidgetitem39.setText(
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u0644\u0627\u0646\u062a\u0642\u0627\u0644 \u0627\u0644\u064a \u0627\u0644\u062a\u0628\u0648\u064a\u0628 \u0631\u0642\u0645 <\u0631\u0642\u0645 \u0627\u0644\u062a\u0628\u0648\u064a\u0628>",
                None,
            )
        )
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.tabWidgetHome.setTabText(
            self.tabWidgetHome.indexOf(self.tabShortcuts),
            QCoreApplication.translate(
                "MainWindowHome",
                "\u0627\u062e\u062a\u0635\u0627\u0631\u0627\u062a",
                None,
            ),
        )
        # if QT_CONFIG(tooltip)
        self.statusbar.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.statusbar.setStatusTip("")


# endif // QT_CONFIG(statustip)
# retranslateUi
