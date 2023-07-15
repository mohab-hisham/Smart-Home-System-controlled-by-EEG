# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loading.ui'
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
    QProgressBar, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1150, 589)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(50)
        self.progressBar.setFont(font)
        self.progressBar.setMaximum(4)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)

        self.verticalLayout.addWidget(self.progressBar)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.info_label = QLabel(Form)
        self.info_label.setObjectName(u"info_label")
        sizePolicy.setHeightForWidth(self.info_label.sizePolicy().hasHeightForWidth())
        self.info_label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(40)
        self.info_label.setFont(font1)
        self.info_label.setFrameShape(QFrame.NoFrame)
        self.info_label.setFrameShadow(QFrame.Plain)
        self.info_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.info_label)

        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 3)

        self.gridLayout.addLayout(self.verticalLayout, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.welcome_label = QLabel(Form)
        self.welcome_label.setObjectName(u"welcome_label")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(60)
        self.welcome_label.setFont(font2)
        self.welcome_label.setFrameShape(QFrame.WinPanel)
        self.welcome_label.setFrameShadow(QFrame.Raised)
        self.welcome_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.welcome_label, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 4, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 6)
        self.gridLayout.setRowStretch(2, 2)
        self.gridLayout.setRowStretch(3, 4)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 40)
        self.gridLayout.setColumnStretch(2, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.info_label.setText("")
        self.welcome_label.setText(QCoreApplication.translate("Form", u"My Smart Home", None))
    # retranslateUi

