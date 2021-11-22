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
        if (self.devicesList.rowCount() < 1):
            self.devicesList.setRowCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.devicesList.setItem(0, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.devicesList.setItem(0, 1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.devicesList.setItem(0, 2, __qtablewidgetitem5)
        self.devicesList.setObjectName(u"devicesList")
        self.devicesList.setGeometry(QRect(0, 15, 960, 425))
        self.devicesList.setAutoScroll(False)
        self.devicesList.setTabKeyNavigation(False)
        self.devicesList.setProperty("showDropIndicator", False)
        self.devicesList.setAlternatingRowColors(True)
        self.devicesList.setTextElideMode(Qt.ElideRight)
        self.devicesList.setCornerButtonEnabled(True)
        self.devicesList.setRowCount(1)
        self.devicesList.setColumnCount(3)
        self.devicesList.horizontalHeader().setCascadingSectionResizes(False)
        self.devicesList.horizontalHeader().setDefaultSectionSize(320)
        self.layoutWidget = QWidget(MainWindow)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(290, 20, 381, 60))
        self.changeIntervalParentContainer = QVBoxLayout(self.layoutWidget)
        self.changeIntervalParentContainer.setObjectName(u"changeIntervalParentContainer")
        self.changeIntervalParentContainer.setContentsMargins(0, 0, 0, 0)
        self.changeIntervalContainer = QHBoxLayout()
        self.changeIntervalContainer.setObjectName(u"changeIntervalContainer")
        self.inputContainer = QHBoxLayout()
        self.inputContainer.setObjectName(u"inputContainer")
        self.refreshIntervalLabel = QLabel(self.layoutWidget)
        self.refreshIntervalLabel.setObjectName(u"refreshIntervalLabel")
        self.refreshIntervalLabel.setTextFormat(Qt.RichText)
        self.refreshIntervalLabel.setWordWrap(True)

        self.inputContainer.addWidget(self.refreshIntervalLabel)

        self.intervalInput = QLineEdit(self.layoutWidget)
        self.intervalInput.setObjectName(u"intervalInput")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.intervalInput.sizePolicy().hasHeightForWidth())
        self.intervalInput.setSizePolicy(sizePolicy)
        self.intervalInput.setCursorPosition(1)
        self.intervalInput.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.inputContainer.addWidget(self.intervalInput)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.inputContainer.addItem(self.horizontalSpacer)

        self.changeIntervalContainer.addLayout(self.inputContainer)

        self.changeIntervalButton = QPushButton(self.layoutWidget)
        self.changeIntervalButton.setObjectName(u"changeIntervalButton")
        self.changeIntervalButton.setEnabled(False)

        self.changeIntervalContainer.addWidget(self.changeIntervalButton)

        self.changeIntervalParentContainer.addLayout(self.changeIntervalContainer)

        self.errorLabel = QLabel(self.layoutWidget)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setAlignment(Qt.AlignCenter)

        self.changeIntervalParentContainer.addWidget(self.errorLabel)

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

        __sortingEnabled = self.devicesList.isSortingEnabled()
        self.devicesList.setSortingEnabled(False)
        ___qtablewidgetitem3 = self.devicesList.item(0, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"test123", None));
        ___qtablewidgetitem4 = self.devicesList.item(0, 1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"50", None));
        self.devicesList.setSortingEnabled(__sortingEnabled)

        self.refreshIntervalLabel.setText(
            QCoreApplication.translate("MainWindow", u"Refresh Interval (in seconds):", None))
        self.intervalInput.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.intervalInput.setPlaceholderText("")
        self.changeIntervalButton.setText(QCoreApplication.translate("MainWindow", u"Change Interval", None))
        self.errorLabel.setText(QCoreApplication.translate("MainWindow", u"lorem ipsum", None))
    # retranslateUi
