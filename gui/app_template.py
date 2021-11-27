# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_design.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QGroupBox, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy,
                               QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
                               QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 540)
        MainWindow.setBaseSize(QSize(960, 540))
        self.deviceGroup = QGroupBox(MainWindow)
        self.deviceGroup.setObjectName(u"deviceGroup")
        self.deviceGroup.setGeometry(QRect(0, 100, 960, 440))
        self.devicesList = QTableWidget(self.deviceGroup)
        if (self.devicesList.columnCount() < 3):
            self.devicesList.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.devicesList.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.devicesList.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.devicesList.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.devicesList.setObjectName(u"devicesList")
        self.devicesList.setGeometry(QRect(0, 20, 960, 420))
        self.devicesList.setAutoScroll(False)
        self.devicesList.setTabKeyNavigation(False)
        self.devicesList.setProperty("showDropIndicator", False)
        self.devicesList.setAlternatingRowColors(True)
        self.devicesList.setTextElideMode(Qt.ElideRight)
        self.devicesList.setCornerButtonEnabled(True)
        self.devicesList.setRowCount(0)
        self.devicesList.setColumnCount(3)
        self.devicesList.horizontalHeader().setCascadingSectionResizes(False)
        self.devicesList.horizontalHeader().setDefaultSectionSize(319)
        self.widget = QWidget(MainWindow)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(130, 20, 706, 68))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.statusContainer = QVBoxLayout()
        self.statusContainer.setObjectName(u"statusContainer")
        self.statusTitleLabel = QLabel(self.widget)
        self.statusTitleLabel.setObjectName(u"statusTitleLabel")
        font = QFont()
        font.setPointSize(14)
        self.statusTitleLabel.setFont(font)
        self.statusTitleLabel.setAlignment(Qt.AlignCenter)

        self.statusContainer.addWidget(self.statusTitleLabel)

        self.statusLabel = QLabel(self.widget)
        self.statusLabel.setObjectName(u"statusLabel")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.statusLabel.setFont(font1)
        self.statusLabel.setStyleSheet(u"color: '#e91e63'")
        self.statusLabel.setTextFormat(Qt.RichText)
        self.statusLabel.setAlignment(Qt.AlignCenter)

        self.statusContainer.addWidget(self.statusLabel)

        self.horizontalLayout.addLayout(self.statusContainer)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.changeIntervalParentContainer = QVBoxLayout()
        self.changeIntervalParentContainer.setObjectName(u"changeIntervalParentContainer")
        self.changeIntervalContainer = QHBoxLayout()
        self.changeIntervalContainer.setObjectName(u"changeIntervalContainer")
        self.inputContainer = QHBoxLayout()
        self.inputContainer.setObjectName(u"inputContainer")
        self.refreshIntervalLabel = QLabel(self.widget)
        self.refreshIntervalLabel.setObjectName(u"refreshIntervalLabel")
        self.refreshIntervalLabel.setTextFormat(Qt.RichText)
        self.refreshIntervalLabel.setWordWrap(True)

        self.inputContainer.addWidget(self.refreshIntervalLabel)

        self.intervalInput = QLineEdit(self.widget)
        self.intervalInput.setObjectName(u"intervalInput")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.intervalInput.sizePolicy().hasHeightForWidth())
        self.intervalInput.setSizePolicy(sizePolicy)
        self.intervalInput.setMinimumSize(QSize(0, 0))
        self.intervalInput.setMaximumSize(QSize(70, 16777215))
        self.intervalInput.setCursorPosition(1)
        self.intervalInput.setAlignment(Qt.AlignCenter)

        self.inputContainer.addWidget(self.intervalInput)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.inputContainer.addItem(self.horizontalSpacer)


        self.changeIntervalContainer.addLayout(self.inputContainer)

        self.changeIntervalButton = QPushButton(self.widget)
        self.changeIntervalButton.setObjectName(u"changeIntervalButton")
        self.changeIntervalButton.setEnabled(False)
        self.changeIntervalButton.setMinimumSize(QSize(120, 30))

        self.changeIntervalContainer.addWidget(self.changeIntervalButton)


        self.changeIntervalParentContainer.addLayout(self.changeIntervalContainer)

        self.errorLabel = QLabel(self.widget)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setAlignment(Qt.AlignCenter)

        self.changeIntervalParentContainer.addWidget(self.errorLabel)


        self.horizontalLayout.addLayout(self.changeIntervalParentContainer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.startStopButtonContainer = QHBoxLayout()
        self.startStopButtonContainer.setObjectName(u"startStopButtonContainer")
        self.startIntervalButton = QPushButton(self.widget)
        self.startIntervalButton.setObjectName(u"startIntervalButton")
        self.startIntervalButton.setMinimumSize(QSize(0, 40))

        self.startStopButtonContainer.addWidget(self.startIntervalButton)

        self.stopIntervalButton = QPushButton(self.widget)
        self.stopIntervalButton.setObjectName(u"stopIntervalButton")
        self.stopIntervalButton.setEnabled(False)
        self.stopIntervalButton.setMinimumSize(QSize(0, 40))

        self.startStopButtonContainer.addWidget(self.stopIntervalButton)

        self.horizontalLayout.addLayout(self.startStopButtonContainer)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Battery Information", None))
        self.deviceGroup.setTitle(QCoreApplication.translate("MainWindow", u"Devices", None))
        ___qtablewidgetitem = self.devicesList.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Device Name", None));
        ___qtablewidgetitem1 = self.devicesList.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Battery Percentage", None));
        ___qtablewidgetitem2 = self.devicesList.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Percentage To Notify", None));
        self.statusTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"IDLE", None))
        self.refreshIntervalLabel.setText(
            QCoreApplication.translate("MainWindow", u"Refresh Interval (in seconds):", None))
        self.intervalInput.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.intervalInput.setPlaceholderText("")
        self.changeIntervalButton.setText(QCoreApplication.translate("MainWindow", u"Change Interval", None))
        self.errorLabel.setText("")
        self.startIntervalButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stopIntervalButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
    # retranslateUi

