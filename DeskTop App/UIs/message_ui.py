# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'message.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_message_wind(object):
    def setupUi(self, message_wind):
        if not message_wind.objectName():
            message_wind.setObjectName(u"message_wind")
        message_wind.resize(856, 517)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        message_wind.setFont(font)
        self.gridLayout = QGridLayout(message_wind)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.message_label = QLabel(message_wind)
        self.message_label.setObjectName(u"message_label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message_label.sizePolicy().hasHeightForWidth())
        self.message_label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(30)
        self.message_label.setFont(font1)
        self.message_label.setFrameShape(QFrame.WinPanel)
        self.message_label.setFrameShadow(QFrame.Raised)
        self.message_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.message_label, 1, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.clearButton = QPushButton(message_wind)
        self.clearButton.setObjectName(u"clearButton")
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(45)
        self.clearButton.setFont(font2)

        self.horizontalLayout.addWidget(self.clearButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.saveButton = QPushButton(message_wind)
        self.saveButton.setObjectName(u"saveButton")
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setFont(font2)

        self.horizontalLayout.addWidget(self.saveButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 3)
        self.horizontalLayout.setStretch(4, 1)

        self.gridLayout.addLayout(self.horizontalLayout, 5, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 31, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 6, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 2, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 3, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.code_label = QLabel(message_wind)
        self.code_label.setObjectName(u"code_label")
        sizePolicy.setHeightForWidth(self.code_label.sizePolicy().hasHeightForWidth())
        self.code_label.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(25)
        self.code_label.setFont(font3)
        self.code_label.setFrameShape(QFrame.WinPanel)
        self.code_label.setFrameShadow(QFrame.Raised)
        self.code_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.code_label)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.info_label = QLabel(message_wind)
        self.info_label.setObjectName(u"info_label")
        sizePolicy.setHeightForWidth(self.info_label.sizePolicy().hasHeightForWidth())
        self.info_label.setSizePolicy(sizePolicy)
        self.info_label.setFont(font3)
        self.info_label.setFrameShape(QFrame.WinPanel)
        self.info_label.setFrameShadow(QFrame.Raised)
        self.info_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.info_label)

        self.horizontalLayout_2.setStretch(0, 6)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 6)

        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 10)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 4)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(5, 4)
        self.gridLayout.setRowStretch(6, 2)
        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 38)
        self.gridLayout.setColumnStretch(2, 5)

        self.retranslateUi(message_wind)

        QMetaObject.connectSlotsByName(message_wind)
    # setupUi

    def retranslateUi(self, message_wind):
        message_wind.setWindowTitle(QCoreApplication.translate("message_wind", u"Message", None))
        self.message_label.setText("")
        self.clearButton.setText(QCoreApplication.translate("message_wind", u"Clear", None))
        self.saveButton.setText(QCoreApplication.translate("message_wind", u"Save", None))
        self.code_label.setText("")
        self.info_label.setText("")
    # retranslateUi

