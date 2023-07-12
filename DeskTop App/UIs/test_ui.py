# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionCalibration = QAction(MainWindow)
        self.actionCalibration.setObjectName(u"actionCalibration")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(20)
        self.actionCalibration.setFont(font)
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
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.testLayout = QVBoxLayout()
        self.testLayout.setSpacing(0)
        self.testLayout.setObjectName(u"testLayout")

        self.verticalLayout_2.addLayout(self.testLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menuUser_Sittings = QMenu(self.menubar)
        self.menuUser_Sittings.setObjectName(u"menuUser_Sittings")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuUser_Sittings.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menuUser_Sittings.addAction(self.actionCalibration)
        self.menuUser_Sittings.addAction(self.actionControls)
        self.menuTools.addAction(self.actionMessage)
        self.menuTools.addAction(self.actionFall_Detection)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionCalibration.setText(QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.actionControls.setText(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.actionMessage.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.actionFall_Detection.setText(QCoreApplication.translate("MainWindow", u"Fall Detection", None))
        self.menuUser_Sittings.setTitle(QCoreApplication.translate("MainWindow", u"User Settings", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

