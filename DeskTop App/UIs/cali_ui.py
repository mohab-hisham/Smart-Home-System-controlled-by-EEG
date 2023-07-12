# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cali.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(977, 687)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.maxt_label = QLabel(Form)
        self.maxt_label.setObjectName(u"maxt_label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxt_label.sizePolicy().hasHeightForWidth())
        self.maxt_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(45)
        self.maxt_label.setFont(font)
        self.maxt_label.setFrameShape(QFrame.WinPanel)
        self.maxt_label.setFrameShadow(QFrame.Raised)
        self.maxt_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.maxt_label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.maxt_SpinBox = QDoubleSpinBox(Form)
        self.maxt_SpinBox.setObjectName(u"maxt_SpinBox")
        sizePolicy.setHeightForWidth(self.maxt_SpinBox.sizePolicy().hasHeightForWidth())
        self.maxt_SpinBox.setSizePolicy(sizePolicy)
        self.maxt_SpinBox.setFont(font)
        self.maxt_SpinBox.setAlignment(Qt.AlignCenter)
        self.maxt_SpinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.maxt_SpinBox.setMaximum(2000.000000000000000)

        self.horizontalLayout.addWidget(self.maxt_SpinBox)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 5)

        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.min_label = QLabel(Form)
        self.min_label.setObjectName(u"min_label")
        sizePolicy.setHeightForWidth(self.min_label.sizePolicy().hasHeightForWidth())
        self.min_label.setSizePolicy(sizePolicy)
        self.min_label.setFont(font)
        self.min_label.setFrameShape(QFrame.WinPanel)
        self.min_label.setFrameShadow(QFrame.Raised)
        self.min_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.min_label)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.mint_SpinBox = QDoubleSpinBox(Form)
        self.mint_SpinBox.setObjectName(u"mint_SpinBox")
        sizePolicy.setHeightForWidth(self.mint_SpinBox.sizePolicy().hasHeightForWidth())
        self.mint_SpinBox.setSizePolicy(sizePolicy)
        self.mint_SpinBox.setFont(font)
        self.mint_SpinBox.setAlignment(Qt.AlignCenter)
        self.mint_SpinBox.setMinimum(-300.000000000000000)
        self.mint_SpinBox.setMaximum(0.000000000000000)

        self.horizontalLayout_2.addWidget(self.mint_SpinBox)

        self.horizontalLayout_2.setStretch(0, 5)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 5)

        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)

        self.autoButton = QPushButton(Form)
        self.autoButton.setObjectName(u"autoButton")
        sizePolicy.setHeightForWidth(self.autoButton.sizePolicy().hasHeightForWidth())
        self.autoButton.setSizePolicy(sizePolicy)
        self.autoButton.setFont(font)

        self.horizontalLayout_4.addWidget(self.autoButton)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_10)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(2, 1)

        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.submitButton = QPushButton(Form)
        self.submitButton.setObjectName(u"submitButton")
        sizePolicy.setHeightForWidth(self.submitButton.sizePolicy().hasHeightForWidth())
        self.submitButton.setSizePolicy(sizePolicy)
        self.submitButton.setFont(font)

        self.horizontalLayout_3.addWidget(self.submitButton)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 1)

        self.gridLayout.addLayout(self.horizontalLayout_3, 7, 1, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_11, 3, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_12, 5, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 8, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 4, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 6, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 11)
        self.gridLayout.setRowStretch(2, 2)
        self.gridLayout.setRowStretch(3, 11)
        self.gridLayout.setRowStretch(4, 2)
        self.gridLayout.setRowStretch(5, 11)
        self.gridLayout.setRowStretch(6, 2)
        self.gridLayout.setRowStretch(7, 11)
        self.gridLayout.setRowStretch(8, 2)
        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 38)
        self.gridLayout.setColumnStretch(2, 5)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.maxt_label.setText(QCoreApplication.translate("Form", u"Maximum Threshold", None))
        self.min_label.setText(QCoreApplication.translate("Form", u"Minimum Threshold", None))
        self.autoButton.setText(QCoreApplication.translate("Form", u"Auto-Calibration", None))
        self.submitButton.setText(QCoreApplication.translate("Form", u"Submit", None))
    # retranslateUi

