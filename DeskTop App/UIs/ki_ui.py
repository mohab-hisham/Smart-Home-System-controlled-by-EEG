# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ki.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1214, 777)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 0, 1, 6)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 0, 1, 6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 3)

        self.washerButton = QPushButton(Form)
        self.washerButton.setObjectName(u"washerButton")
        self.washerButton.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.washerButton.sizePolicy().hasHeightForWidth())
        self.washerButton.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(50)
        self.washerButton.setFont(font)

        self.gridLayout.addWidget(self.washerButton, 3, 1, 1, 1)

        self.chimneyButton = QPushButton(Form)
        self.chimneyButton.setObjectName(u"chimneyButton")
        sizePolicy.setHeightForWidth(self.chimneyButton.sizePolicy().hasHeightForWidth())
        self.chimneyButton.setSizePolicy(sizePolicy)
        self.chimneyButton.setFont(font)
        self.chimneyButton.setAutoFillBackground(True)
        self.chimneyButton.setAutoDefault(False)

        self.gridLayout.addWidget(self.chimneyButton, 3, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 4, 3, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.stoveButton = QPushButton(Form)
        self.stoveButton.setObjectName(u"stoveButton")
        sizePolicy.setHeightForWidth(self.stoveButton.sizePolicy().hasHeightForWidth())
        self.stoveButton.setSizePolicy(sizePolicy)
        self.stoveButton.setFont(font)
        self.stoveButton.setAutoDefault(False)

        self.gridLayout.addWidget(self.stoveButton, 1, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 3, 1)

        self.lightButton = QPushButton(Form)
        self.lightButton.setObjectName(u"lightButton")
        sizePolicy.setHeightForWidth(self.lightButton.sizePolicy().hasHeightForWidth())
        self.lightButton.setSizePolicy(sizePolicy)
        self.lightButton.setFont(font)

        self.gridLayout.addWidget(self.lightButton, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 6, 3, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.info_label = QLabel(Form)
        self.info_label.setObjectName(u"info_label")
        sizePolicy.setHeightForWidth(self.info_label.sizePolicy().hasHeightForWidth())
        self.info_label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(30)
        self.info_label.setFont(font1)
        self.info_label.setFrameShape(QFrame.WinPanel)
        self.info_label.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.info_label)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.message_label = QLabel(Form)
        self.message_label.setObjectName(u"message_label")
        sizePolicy.setHeightForWidth(self.message_label.sizePolicy().hasHeightForWidth())
        self.message_label.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(40)
        self.message_label.setFont(font2)
        self.message_label.setFrameShape(QFrame.WinPanel)
        self.message_label.setFrameShadow(QFrame.Raised)
        self.message_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.message_label)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.homeButton = QPushButton(Form)
        self.homeButton.setObjectName(u"homeButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(34)
        sizePolicy1.setHeightForWidth(self.homeButton.sizePolicy().hasHeightForWidth())
        self.homeButton.setSizePolicy(sizePolicy1)
        self.homeButton.setFont(font)
        self.homeButton.setAutoDefault(False)

        self.verticalLayout.addWidget(self.homeButton)

        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 3)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 3)

        self.gridLayout.addLayout(self.verticalLayout, 1, 5, 3, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 12)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 12)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 15)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 15)
        self.gridLayout.setColumnStretch(4, 2)
        self.gridLayout.setColumnStretch(5, 13)
        self.gridLayout.setColumnStretch(6, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.washerButton.setText("")
        self.chimneyButton.setText("")
        self.stoveButton.setText("")
        self.lightButton.setText("")
        self.info_label.setText("")
        self.message_label.setText("")
        self.homeButton.setText("")
    # retranslateUi

