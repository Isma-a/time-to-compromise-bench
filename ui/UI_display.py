# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'display.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QProgressBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSplitter, QStackedWidget, QStatusBar, QToolBar,
    QVBoxLayout, QWidget)

from password_line_edit import PasswordLineEdit

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1062, 709)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Horizontal)
        self.lateralFrameWidget = QFrame(self.splitter_2)
        self.lateralFrameWidget.setObjectName(u"lateralFrameWidget")
        self.lateralFrameWidget.setFrameShape(QFrame.Shape.StyledPanel)
        self.lateralFrameWidget.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.lateralFrameWidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.stackedWidgetLateral = QStackedWidget(self.lateralFrameWidget)
        self.stackedWidgetLateral.setObjectName(u"stackedWidgetLateral")
        self.lateralOnePasswordPage = QWidget()
        self.lateralOnePasswordPage.setObjectName(u"lateralOnePasswordPage")
        self.stackedWidgetLateral.addWidget(self.lateralOnePasswordPage)
        self.lateralManyPasswordPage = QWidget()
        self.lateralManyPasswordPage.setObjectName(u"lateralManyPasswordPage")
        self.stackedWidgetLateral.addWidget(self.lateralManyPasswordPage)

        self.gridLayout_8.addWidget(self.stackedWidgetLateral, 0, 0, 1, 1)

        self.splitter_2.addWidget(self.lateralFrameWidget)
        self.centralStackWidget = QStackedWidget(self.splitter_2)
        self.centralStackWidget.setObjectName(u"centralStackWidget")
        self.onePasswordPage = QWidget()
        self.onePasswordPage.setObjectName(u"onePasswordPage")
        self.gridLayout_2 = QGridLayout(self.onePasswordPage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_main = QVBoxLayout()
        self.verticalLayout_main.setSpacing(0)
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.verticalLayout_main.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.passwordEntryArea = QFrame(self.onePasswordPage)
        self.passwordEntryArea.setObjectName(u"passwordEntryArea")
        self.gridLayout_3 = QGridLayout(self.passwordEntryArea)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_passwordEntry = QVBoxLayout()
        self.verticalLayout_passwordEntry.setSpacing(10)
        self.verticalLayout_passwordEntry.setObjectName(u"verticalLayout_passwordEntry")
        self.horizontalLayout_passwordEntryText = QHBoxLayout()
        self.horizontalLayout_passwordEntryText.setObjectName(u"horizontalLayout_passwordEntryText")
        self.horizontalLayout_passwordEntryText.setContentsMargins(5, -1, -1, -1)
        self.passwordEntryTextLabel = QLabel(self.passwordEntryArea)
        self.passwordEntryTextLabel.setObjectName(u"passwordEntryTextLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordEntryTextLabel.sizePolicy().hasHeightForWidth())
        self.passwordEntryTextLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_passwordEntryText.addWidget(self.passwordEntryTextLabel)

        self.horizontalSpacer_passwordEntry = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_passwordEntryText.addItem(self.horizontalSpacer_passwordEntry)


        self.verticalLayout_passwordEntry.addLayout(self.horizontalLayout_passwordEntryText)

        self.horizontalLayout_passwordEntryEdit = QHBoxLayout()
        self.horizontalLayout_passwordEntryEdit.setSpacing(10)
        self.horizontalLayout_passwordEntryEdit.setObjectName(u"horizontalLayout_passwordEntryEdit")
        self.horizontalLayout_passwordEntryEdit.setContentsMargins(-1, -1, 10, -1)
        self.passwordLineEdit = PasswordLineEdit(self.passwordEntryArea)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.passwordLineEdit.sizePolicy().hasHeightForWidth())
        self.passwordLineEdit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_passwordEntryEdit.addWidget(self.passwordLineEdit)

        self.passwordAnalyzePushButton = QPushButton(self.passwordEntryArea)
        self.passwordAnalyzePushButton.setObjectName(u"passwordAnalyzePushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.passwordAnalyzePushButton.sizePolicy().hasHeightForWidth())
        self.passwordAnalyzePushButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout_passwordEntryEdit.addWidget(self.passwordAnalyzePushButton)

        self.horizontalLayout_passwordEntryEdit.setStretch(0, 3)
        self.horizontalLayout_passwordEntryEdit.setStretch(1, 1)

        self.verticalLayout_passwordEntry.addLayout(self.horizontalLayout_passwordEntryEdit)

        self.passwordSafetyProgressBar = QProgressBar(self.passwordEntryArea)
        self.passwordSafetyProgressBar.setObjectName(u"passwordSafetyProgressBar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.passwordSafetyProgressBar.sizePolicy().hasHeightForWidth())
        self.passwordSafetyProgressBar.setSizePolicy(sizePolicy3)
        self.passwordSafetyProgressBar.setMinimumSize(QSize(0, 5))
        self.passwordSafetyProgressBar.setMaximum(5)
        self.passwordSafetyProgressBar.setValue(4)
        self.passwordSafetyProgressBar.setTextVisible(False)
        self.passwordSafetyProgressBar.setOrientation(Qt.Orientation.Horizontal)
        self.passwordSafetyProgressBar.setInvertedAppearance(False)

        self.verticalLayout_passwordEntry.addWidget(self.passwordSafetyProgressBar)

        self.verticalLayout_passwordEntry.setStretch(0, 1)
        self.verticalLayout_passwordEntry.setStretch(1, 5)
        self.verticalLayout_passwordEntry.setStretch(2, 1)

        self.gridLayout_3.addLayout(self.verticalLayout_passwordEntry, 0, 0, 1, 1)


        self.verticalLayout_main.addWidget(self.passwordEntryArea)

        self.hashageAndGpuArea = QFrame(self.onePasswordPage)
        self.hashageAndGpuArea.setObjectName(u"hashageAndGpuArea")
        self.gridLayout_5 = QGridLayout(self.hashageAndGpuArea)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.stackedWidget = QStackedWidget(self.hashageAndGpuArea)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.hashPage = QWidget()
        self.hashPage.setObjectName(u"hashPage")
        self.gridLayout_6 = QGridLayout(self.hashPage)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayoutHash = QVBoxLayout()
        self.verticalLayoutHash.setObjectName(u"verticalLayoutHash")
        self.labelHash = QLabel(self.hashPage)
        self.labelHash.setObjectName(u"labelHash")

        self.verticalLayoutHash.addWidget(self.labelHash)

        self.splitterHash = QSplitter(self.hashPage)
        self.splitterHash.setObjectName(u"splitterHash")
        self.splitterHash.setOrientation(Qt.Orientation.Horizontal)
        self.hashCategory = QListWidget(self.splitterHash)
        self.hashCategory.setObjectName(u"hashCategory")
        self.splitterHash.addWidget(self.hashCategory)
        self.layoutWidget = QWidget(self.splitterHash)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayoutHashSearch = QVBoxLayout(self.layoutWidget)
        self.verticalLayoutHashSearch.setObjectName(u"verticalLayoutHashSearch")
        self.verticalLayoutHashSearch.setContentsMargins(0, 0, 0, 0)
        self.lineEditHashSearch = QLineEdit(self.layoutWidget)
        self.lineEditHashSearch.setObjectName(u"lineEditHashSearch")
        self.lineEditHashSearch.setClearButtonEnabled(True)

        self.verticalLayoutHashSearch.addWidget(self.lineEditHashSearch)

        self.scrollAreaHashGrid = QScrollArea(self.layoutWidget)
        self.scrollAreaHashGrid.setObjectName(u"scrollAreaHashGrid")
        self.scrollAreaHashGrid.setWidgetResizable(True)
        self.scrollAreaWidgetContentsHashGrid = QWidget()
        self.scrollAreaWidgetContentsHashGrid.setObjectName(u"scrollAreaWidgetContentsHashGrid")
        self.scrollAreaWidgetContentsHashGrid.setGeometry(QRect(0, 0, 165, 156))
        self.scrollAreaHashGrid.setWidget(self.scrollAreaWidgetContentsHashGrid)

        self.verticalLayoutHashSearch.addWidget(self.scrollAreaHashGrid)

        self.splitterHash.addWidget(self.layoutWidget)
        self.scrollAreaHashInfo = QScrollArea(self.splitterHash)
        self.scrollAreaHashInfo.setObjectName(u"scrollAreaHashInfo")
        self.scrollAreaHashInfo.setWidgetResizable(True)
        self.scrollAreaWidgetContentsHashInfo = QWidget()
        self.scrollAreaWidgetContentsHashInfo.setObjectName(u"scrollAreaWidgetContentsHashInfo")
        self.scrollAreaWidgetContentsHashInfo.setGeometry(QRect(0, 0, 68, 189))
        self.scrollAreaHashInfo.setWidget(self.scrollAreaWidgetContentsHashInfo)
        self.splitterHash.addWidget(self.scrollAreaHashInfo)

        self.verticalLayoutHash.addWidget(self.splitterHash)


        self.gridLayout_6.addLayout(self.verticalLayoutHash, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.hashPage)
        self.GPUPage = QWidget()
        self.GPUPage.setObjectName(u"GPUPage")
        self.gridLayout_7 = QGridLayout(self.GPUPage)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayoutGPU = QVBoxLayout()
        self.verticalLayoutGPU.setObjectName(u"verticalLayoutGPU")
        self.labelGPU = QLabel(self.GPUPage)
        self.labelGPU.setObjectName(u"labelGPU")
        sizePolicy.setHeightForWidth(self.labelGPU.sizePolicy().hasHeightForWidth())
        self.labelGPU.setSizePolicy(sizePolicy)

        self.verticalLayoutGPU.addWidget(self.labelGPU)

        self.splitterGPU = QSplitter(self.GPUPage)
        self.splitterGPU.setObjectName(u"splitterGPU")
        self.splitterGPU.setOrientation(Qt.Orientation.Horizontal)
        self.GPUCategory = QListWidget(self.splitterGPU)
        self.GPUCategory.setObjectName(u"GPUCategory")
        self.splitterGPU.addWidget(self.GPUCategory)
        self.layoutWidget_3 = QWidget(self.splitterGPU)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.verticalLayoutGPUSearch = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayoutGPUSearch.setObjectName(u"verticalLayoutGPUSearch")
        self.verticalLayoutGPUSearch.setContentsMargins(0, 0, 0, 0)
        self.lineEditGPUSearch = QLineEdit(self.layoutWidget_3)
        self.lineEditGPUSearch.setObjectName(u"lineEditGPUSearch")
        self.lineEditGPUSearch.setClearButtonEnabled(True)

        self.verticalLayoutGPUSearch.addWidget(self.lineEditGPUSearch)

        self.scrollAreaGPUGrid = QScrollArea(self.layoutWidget_3)
        self.scrollAreaGPUGrid.setObjectName(u"scrollAreaGPUGrid")
        self.scrollAreaGPUGrid.setWidgetResizable(True)
        self.scrollAreaWidgetContentsGPUGrid = QWidget()
        self.scrollAreaWidgetContentsGPUGrid.setObjectName(u"scrollAreaWidgetContentsGPUGrid")
        self.scrollAreaWidgetContentsGPUGrid.setGeometry(QRect(0, 0, 274, 156))
        self.scrollAreaGPUGrid.setWidget(self.scrollAreaWidgetContentsGPUGrid)

        self.verticalLayoutGPUSearch.addWidget(self.scrollAreaGPUGrid)

        self.splitterGPU.addWidget(self.layoutWidget_3)
        self.scrollAreaGPUInfo = QScrollArea(self.splitterGPU)
        self.scrollAreaGPUInfo.setObjectName(u"scrollAreaGPUInfo")
        self.scrollAreaGPUInfo.setWidgetResizable(True)
        self.scrollAreaWidgetContentsGPUInfo = QWidget()
        self.scrollAreaWidgetContentsGPUInfo.setObjectName(u"scrollAreaWidgetContentsGPUInfo")
        self.scrollAreaWidgetContentsGPUInfo.setGeometry(QRect(0, 0, 68, 189))
        self.scrollAreaGPUInfo.setWidget(self.scrollAreaWidgetContentsGPUInfo)
        self.splitterGPU.addWidget(self.scrollAreaGPUInfo)

        self.verticalLayoutGPU.addWidget(self.splitterGPU)


        self.gridLayout_7.addLayout(self.verticalLayoutGPU, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.GPUPage)

        self.gridLayout_5.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.verticalLayout_main.addWidget(self.hashageAndGpuArea)

        self.attackPipelineArea = QFrame(self.onePasswordPage)
        self.attackPipelineArea.setObjectName(u"attackPipelineArea")
        self.gridLayout_4 = QGridLayout(self.attackPipelineArea)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelAttackPipeline = QLabel(self.attackPipelineArea)
        self.labelAttackPipeline.setObjectName(u"labelAttackPipeline")
        sizePolicy.setHeightForWidth(self.labelAttackPipeline.sizePolicy().hasHeightForWidth())
        self.labelAttackPipeline.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.labelAttackPipeline)

        self.splitter = QSplitter(self.attackPipelineArea)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.listWidget = QListWidget(self.splitter)
        self.listWidget.setObjectName(u"listWidget")
        self.splitter.addWidget(self.listWidget)
        self.listWidget_2 = QListWidget(self.splitter)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setFlow(QListView.Flow.LeftToRight)
        self.listWidget_2.setViewMode(QListView.ViewMode.ListMode)
        self.splitter.addWidget(self.listWidget_2)
        self.scrollArea = QScrollArea(self.splitter)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 68, 207))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.splitter.addWidget(self.scrollArea)

        self.verticalLayout.addWidget(self.splitter)

        self.verticalLayout.setStretch(0, 1)

        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.verticalLayout_main.addWidget(self.attackPipelineArea)

        self.verticalLayout_main.setStretch(0, 1)
        self.verticalLayout_main.setStretch(1, 2)
        self.verticalLayout_main.setStretch(2, 2)

        self.gridLayout_2.addLayout(self.verticalLayout_main, 0, 0, 1, 1)

        self.centralStackWidget.addWidget(self.onePasswordPage)
        self.manyPasswordsPage = QWidget()
        self.manyPasswordsPage.setObjectName(u"manyPasswordsPage")
        self.centralStackWidget.addWidget(self.manyPasswordsPage)
        self.splitter_2.addWidget(self.centralStackWidget)

        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)

        self.centralStackWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.passwordEntryTextLabel.setText(QCoreApplication.translate("MainWindow", u"Password Entry", None))
        self.passwordLineEdit.setText("")
        self.passwordAnalyzePushButton.setText(QCoreApplication.translate("MainWindow", u"Analyze", None))
        self.passwordSafetyProgressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.labelHash.setText(QCoreApplication.translate("MainWindow", u"Hash Selector", None))
        self.labelGPU.setText(QCoreApplication.translate("MainWindow", u"GPUs Selector", None))
        self.labelAttackPipeline.setText(QCoreApplication.translate("MainWindow", u"Attack Pipeline", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

