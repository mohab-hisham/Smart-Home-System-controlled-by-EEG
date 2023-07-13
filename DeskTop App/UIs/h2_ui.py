# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'h2.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1472, 902)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 3, 1, 1)

        self.room1_Button = QPushButton(Form)
        self.room1_Button.setObjectName(u"room1_Button")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.room1_Button.sizePolicy().hasHeightForWidth())
        self.room1_Button.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(50)
        self.room1_Button.setFont(font)

        self.gridLayout.addWidget(self.room1_Button, 1, 3, 1, 1)

        self.room2_Button = QPushButton(Form)
        self.room2_Button.setObjectName(u"room2_Button")
        sizePolicy.setHeightForWidth(self.room2_Button.sizePolicy().hasHeightForWidth())
        self.room2_Button.setSizePolicy(sizePolicy)
        self.room2_Button.setFont(font)

        self.gridLayout.addWidget(self.room2_Button, 1, 5, 1, 1)

        self.livingButton = QPushButton(Form)
        self.livingButton.setObjectName(u"livingButton")
        sizePolicy.setHeightForWidth(self.livingButton.sizePolicy().hasHeightForWidth())
        self.livingButton.setSizePolicy(sizePolicy)
        self.livingButton.setFont(font)

        self.gridLayout.addWidget(self.livingButton, 1, 1, 1, 1)

        self.kitchenButton = QPushButton(Form)
        self.kitchenButton.setObjectName(u"kitchenButton")
        sizePolicy.setHeightForWidth(self.kitchenButton.sizePolicy().hasHeightForWidth())
        self.kitchenButton.setSizePolicy(sizePolicy)
        self.kitchenButton.setFont(font)

        self.gridLayout.addWidget(self.kitchenButton, 3, 1, 1, 1)

        self.message_label = QLabel(Form)
        self.message_label.setObjectName(u"message_label")
        sizePolicy.setHeightForWidth(self.message_label.sizePolicy().hasHeightForWidth())
        self.message_label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(40)
        font1.setBold(False)
        font1.setItalic(False)
        self.message_label.setFont(font1)
        self.message_label.setLayoutDirection(Qt.LeftToRight)
        self.message_label.setFrameShape(QFrame.WinPanel)
        self.message_label.setFrameShadow(QFrame.Raised)
        self.message_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.message_label, 5, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.exitButton = QPushButton(Form)
        self.exitButton.setObjectName(u"exitButton")
        sizePolicy.setHeightForWidth(self.exitButton.sizePolicy().hasHeightForWidth())
        self.exitButton.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(45)
        font2.setBold(True)
        self.exitButton.setFont(font2)

        self.gridLayout.addWidget(self.exitButton, 5, 3, 1, 1)

        self.bathButton = QPushButton(Form)
        self.bathButton.setObjectName(u"bathButton")
        sizePolicy.setHeightForWidth(self.bathButton.sizePolicy().hasHeightForWidth())
        self.bathButton.setSizePolicy(sizePolicy)
        self.bathButton.setFont(font)

        self.gridLayout.addWidget(self.bathButton, 3, 5, 1, 1)

        self.info_label = QLabel(Form)
        self.info_label.setObjectName(u"info_label")
        sizePolicy.setHeightForWidth(self.info_label.sizePolicy().hasHeightForWidth())
        self.info_label.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(40)
        self.info_label.setFont(font3)
        self.info_label.setFrameShape(QFrame.WinPanel)
        self.info_label.setFrameShadow(QFrame.Raised)
        self.info_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.info_label, 5, 5, 1, 1)

        self.lobbyButton = QPushButton(Form)
        self.lobbyButton.setObjectName(u"lobbyButton")
        sizePolicy.setHeightForWidth(self.lobbyButton.sizePolicy().hasHeightForWidth())
        self.lobbyButton.setSizePolicy(sizePolicy)
        self.lobbyButton.setFont(font)

        self.gridLayout.addWidget(self.lobbyButton, 3, 3, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 2, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 6, 1, 1, 5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 0, 6, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 6, 7, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 10)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 10)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(5, 3)
        self.gridLayout.setRowStretch(6, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 20)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 20)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout.setColumnStretch(5, 20)
        self.gridLayout.setColumnStretch(6, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.room1_Button.setText("")
        self.room2_Button.setText("")
        self.livingButton.setText("")
        self.kitchenButton.setText("")
        self.message_label.setText("")
        self.exitButton.setText(QCoreApplication.translate("Form", u"Exit", None))
        self.bathButton.setText("")
        self.info_label.setText("")
        self.lobbyButton.setText("")
    # retranslateUi

