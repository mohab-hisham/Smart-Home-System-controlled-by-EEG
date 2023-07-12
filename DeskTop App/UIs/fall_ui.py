# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fall.ui'
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
    QVBoxLayout, QWidget)

class Ui_fall_detect_form(object):
    def setupUi(self, fall_detect_form):
        if not fall_detect_form.objectName():
            fall_detect_form.setObjectName(u"fall_detect_form")
        fall_detect_form.resize(532, 352)
        self.gridLayout = QGridLayout(fall_detect_form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)

        self.xacc_label = QLabel(fall_detect_form)
        self.xacc_label.setObjectName(u"xacc_label")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        self.xacc_label.setFont(font)

        self.horizontalLayout.addWidget(self.xacc_label)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.xval_label = QLabel(fall_detect_form)
        self.xval_label.setObjectName(u"xval_label")
        self.xval_label.setFont(font)
        self.xval_label.setFrameShape(QFrame.WinPanel)
        self.xval_label.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.xval_label)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_9)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 3)
        self.horizontalLayout.setStretch(4, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_10)

        self.yacc_label = QLabel(fall_detect_form)
        self.yacc_label.setObjectName(u"yacc_label")
        self.yacc_label.setFont(font)

        self.horizontalLayout_2.addWidget(self.yacc_label)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.yval_label = QLabel(fall_detect_form)
        self.yval_label.setObjectName(u"yval_label")
        self.yval_label.setFont(font)
        self.yval_label.setFrameShape(QFrame.WinPanel)
        self.yval_label.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.yval_label)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_11)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 5)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 3)
        self.horizontalLayout_2.setStretch(4, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_12)

        self.zcc_label = QLabel(fall_detect_form)
        self.zcc_label.setObjectName(u"zcc_label")
        self.zcc_label.setFont(font)

        self.horizontalLayout_3.addWidget(self.zcc_label)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.zval_label = QLabel(fall_detect_form)
        self.zval_label.setObjectName(u"zval_label")
        self.zval_label.setFont(font)
        self.zval_label.setFrameShape(QFrame.WinPanel)
        self.zval_label.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.zval_label)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_13)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 5)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 3)
        self.horizontalLayout_3.setStretch(4, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_14)

        self.heart_label = QLabel(fall_detect_form)
        self.heart_label.setObjectName(u"heart_label")
        self.heart_label.setFont(font)

        self.horizontalLayout_6.addWidget(self.heart_label)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_15)

        self.hval_label = QLabel(fall_detect_form)
        self.hval_label.setObjectName(u"hval_label")
        self.hval_label.setFont(font)
        self.hval_label.setFrameShape(QFrame.WinPanel)
        self.hval_label.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.hval_label)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_16)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 5)
        self.horizontalLayout_6.setStretch(2, 1)
        self.horizontalLayout_6.setStretch(3, 3)
        self.horizontalLayout_6.setStretch(4, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.msg_label = QLabel(fall_detect_form)
        self.msg_label.setObjectName(u"msg_label")
        self.msg_label.setFont(font)
        self.msg_label.setFrameShape(QFrame.WinPanel)
        self.msg_label.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.msg_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 6)
        self.horizontalLayout_4.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.backButton = QPushButton(fall_detect_form)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setFont(font)
        self.backButton.setAutoDefault(True)
        self.backButton.setFlat(False)

        self.horizontalLayout_5.addWidget(self.backButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)
        self.horizontalLayout_5.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 3)
        self.verticalLayout.setStretch(3, 3)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 3)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(7, 3)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(fall_detect_form)

        self.backButton.setDefault(False)


        QMetaObject.connectSlotsByName(fall_detect_form)
    # setupUi

    def retranslateUi(self, fall_detect_form):
        fall_detect_form.setWindowTitle(QCoreApplication.translate("fall_detect_form", u"Fall Detection", None))
        self.xacc_label.setText(QCoreApplication.translate("fall_detect_form", u"X Acceleration", None))
        self.xval_label.setText("")
        self.yacc_label.setText(QCoreApplication.translate("fall_detect_form", u"Y Acceleration", None))
        self.yval_label.setText("")
        self.zcc_label.setText(QCoreApplication.translate("fall_detect_form", u"Z Acceleration", None))
        self.zval_label.setText("")
        self.heart_label.setText(QCoreApplication.translate("fall_detect_form", u"Heart Rate", None))
        self.hval_label.setText("")
        self.msg_label.setText("")
        self.backButton.setText(QCoreApplication.translate("fall_detect_form", u"Home", None))
    # retranslateUi

