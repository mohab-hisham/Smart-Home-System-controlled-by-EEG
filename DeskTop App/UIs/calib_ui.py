# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calib.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_calib_wind(object):
    def setupUi(self, calib_wind):
        if not calib_wind.objectName():
            calib_wind.setObjectName(u"calib_wind")
        calib_wind.setWindowModality(Qt.WindowModal)
        calib_wind.resize(400, 300)
        font = QFont()
        font.setPointSize(27)
        font.setBold(False)
        calib_wind.setFont(font)
        self.verticalLayout = QVBoxLayout(calib_wind)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.maxt_label = QLabel(calib_wind)
        self.maxt_label.setObjectName(u"maxt_label")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(14)
        self.maxt_label.setFont(font1)

        self.horizontalLayout.addWidget(self.maxt_label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.maxt_SpinBox = QDoubleSpinBox(calib_wind)
        self.maxt_SpinBox.setObjectName(u"maxt_SpinBox")
        self.maxt_SpinBox.setFont(font1)
        self.maxt_SpinBox.setMaximum(2000.000000000000000)

        self.horizontalLayout.addWidget(self.maxt_SpinBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.min_label = QLabel(calib_wind)
        self.min_label.setObjectName(u"min_label")
        self.min_label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.min_label)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.mint_SpinBox = QDoubleSpinBox(calib_wind)
        self.mint_SpinBox.setObjectName(u"mint_SpinBox")
        self.mint_SpinBox.setFont(font1)
        self.mint_SpinBox.setMinimum(-300.000000000000000)
        self.mint_SpinBox.setMaximum(0.000000000000000)

        self.horizontalLayout_2.addWidget(self.mint_SpinBox)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)

        self.autoButton = QPushButton(calib_wind)
        self.autoButton.setObjectName(u"autoButton")
        self.autoButton.setFont(font1)

        self.horizontalLayout_4.addWidget(self.autoButton)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_10)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.submitButton = QPushButton(calib_wind)
        self.submitButton.setObjectName(u"submitButton")
        self.submitButton.setFont(font1)

        self.horizontalLayout_3.addWidget(self.submitButton)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(3, 1)

        self.retranslateUi(calib_wind)

        QMetaObject.connectSlotsByName(calib_wind)
    # setupUi

    def retranslateUi(self, calib_wind):
        calib_wind.setWindowTitle(QCoreApplication.translate("calib_wind", u"Calibration", None))
        self.maxt_label.setText(QCoreApplication.translate("calib_wind", u"Maximum Threshold", None))
        self.min_label.setText(QCoreApplication.translate("calib_wind", u"Minimum Threshold", None))
        self.autoButton.setText(QCoreApplication.translate("calib_wind", u"Auto-Calibration", None))
        self.submitButton.setText(QCoreApplication.translate("calib_wind", u"Submit", None))
    # retranslateUi

