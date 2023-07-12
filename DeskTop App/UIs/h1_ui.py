# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'h1.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1233, 640)
        self.actionCalibration_2 = QAction(MainWindow)
        self.actionCalibration_2.setObjectName(u"actionCalibration_2")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(20)
        self.actionCalibration_2.setFont(font)
        self.actionControls = QAction(MainWindow)
        self.actionControls.setObjectName(u"actionControls")
        self.actionControls.setFont(font)
        self.actionMessage = QAction(MainWindow)
        self.actionMessage.setObjectName(u"actionMessage")
        self.actionMessage.setFont(font)
        self.actionFall_Detection = QAction(MainWindow)
        self.actionFall_Detection.setObjectName(u"actionFall_Detection")
        self.actionFall_Detection.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 4, 1, 1, 5)

        self.message_label = QLabel(self.centralwidget)
        self.message_label.setObjectName(u"message_label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message_label.sizePolicy().hasHeightForWidth())
        self.message_label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setItalic(False)
        self.message_label.setFont(font1)
        self.message_label.setLayoutDirection(Qt.LeftToRight)
        self.message_label.setFrameShape(QFrame.WinPanel)
        self.message_label.setFrameShadow(QFrame.Raised)
        self.message_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.message_label, 5, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 2, 3, 1)

        self.kitchenButton = QPushButton(self.centralwidget)
        self.kitchenButton.setObjectName(u"kitchenButton")
        sizePolicy.setHeightForWidth(self.kitchenButton.sizePolicy().hasHeightForWidth())
        self.kitchenButton.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.kitchenButton, 3, 1, 1, 1)

        self.room2_Button = QPushButton(self.centralwidget)
        self.room2_Button.setObjectName(u"room2_Button")
        sizePolicy.setHeightForWidth(self.room2_Button.sizePolicy().hasHeightForWidth())
        self.room2_Button.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.room2_Button, 1, 5, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 2, 1)

        self.lobbyButton = QPushButton(self.centralwidget)
        self.lobbyButton.setObjectName(u"lobbyButton")
        sizePolicy.setHeightForWidth(self.lobbyButton.sizePolicy().hasHeightForWidth())
        self.lobbyButton.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lobbyButton, 3, 3, 1, 1)

        self.bathButton = QPushButton(self.centralwidget)
        self.bathButton.setObjectName(u"bathButton")
        sizePolicy.setHeightForWidth(self.bathButton.sizePolicy().hasHeightForWidth())
        self.bathButton.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.bathButton, 3, 5, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 4, 2, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 6, 1, 1, 5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 6, 2, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 3, 1, 1)

        self.livingButton = QPushButton(self.centralwidget)
        self.livingButton.setObjectName(u"livingButton")
        sizePolicy.setHeightForWidth(self.livingButton.sizePolicy().hasHeightForWidth())
        self.livingButton.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(8)
        self.livingButton.setFont(font2)

        self.gridLayout.addWidget(self.livingButton, 1, 1, 1, 1)

        self.room1_Button = QPushButton(self.centralwidget)
        self.room1_Button.setObjectName(u"room1_Button")
        sizePolicy.setHeightForWidth(self.room1_Button.sizePolicy().hasHeightForWidth())
        self.room1_Button.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.room1_Button, 1, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 5, 2, 1, 1)

        self.exitButton = QPushButton(self.centralwidget)
        self.exitButton.setObjectName(u"exitButton")
        sizePolicy.setHeightForWidth(self.exitButton.sizePolicy().hasHeightForWidth())
        self.exitButton.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(45)
        font3.setBold(True)
        self.exitButton.setFont(font3)

        self.gridLayout.addWidget(self.exitButton, 5, 3, 1, 1)

        self.info_label = QLabel(self.centralwidget)
        self.info_label.setObjectName(u"info_label")
        sizePolicy.setHeightForWidth(self.info_label.sizePolicy().hasHeightForWidth())
        self.info_label.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(15)
        self.info_label.setFont(font4)
        self.info_label.setFrameShape(QFrame.WinPanel)
        self.info_label.setFrameShadow(QFrame.Raised)
        self.info_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.info_label, 5, 5, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 15)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 15)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(5, 5)
        self.gridLayout.setRowStretch(6, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 20)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 20)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout.setColumnStretch(5, 20)
        self.gridLayout.setColumnStretch(6, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1233, 26))
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menuUser_Settings = QMenu(self.menubar)
        self.menuUser_Settings.setObjectName(u"menuUser_Settings")
        sizePolicy.setHeightForWidth(self.menuUser_Settings.sizePolicy().hasHeightForWidth())
        self.menuUser_Settings.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setFamilies([u"Times New Roman"])
        font5.setPointSize(25)
        self.menuUser_Settings.setFont(font5)
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        sizePolicy.setHeightForWidth(self.menuTools.sizePolicy().hasHeightForWidth())
        self.menuTools.setSizePolicy(sizePolicy)
        self.menuTools.setFont(font5)
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuUser_Settings.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menuUser_Settings.addAction(self.actionCalibration_2)
        self.menuUser_Settings.addAction(self.actionControls)
        self.menuTools.addAction(self.actionMessage)
        self.menuTools.addAction(self.actionFall_Detection)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"My Smart Home", None))
        self.actionCalibration_2.setText(QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.actionControls.setText(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.actionMessage.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.actionFall_Detection.setText(QCoreApplication.translate("MainWindow", u"Fall Detection", None))
        self.message_label.setText("")
        self.kitchenButton.setText("")
        self.room2_Button.setText("")
        self.lobbyButton.setText("")
        self.bathButton.setText("")
        self.livingButton.setText("")
        self.room1_Button.setText("")
        self.exitButton.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.info_label.setText("")
        self.menuUser_Settings.setTitle(QCoreApplication.translate("MainWindow", u"User Settings", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

