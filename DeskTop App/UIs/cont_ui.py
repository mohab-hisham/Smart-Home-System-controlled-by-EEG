# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cont.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(884, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.seq_radioButton = QRadioButton(Form)
        self.seq_radioButton.setObjectName(u"seq_radioButton")
        self.seq_radioButton.setChecked(True)

        self.verticalLayout.addWidget(self.seq_radioButton)

        self.left_right_radioButton = QRadioButton(Form)
        self.left_right_radioButton.setObjectName(u"left_right_radioButton")

        self.verticalLayout.addWidget(self.left_right_radioButton)

        self.head_radioButton = QRadioButton(Form)
        self.head_radioButton.setObjectName(u"head_radioButton")

        self.verticalLayout.addWidget(self.head_radioButton)

        self.doneButton = QPushButton(Form)
        self.doneButton.setObjectName(u"doneButton")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        self.doneButton.setFont(font)

        self.verticalLayout.addWidget(self.doneButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.seq_radioButton.setText(QCoreApplication.translate("Form", u"Sequence", None))
        self.left_right_radioButton.setText(QCoreApplication.translate("Form", u"Left and Right ", None))
        self.head_radioButton.setText(QCoreApplication.translate("Form", u"Head Movment", None))
        self.doneButton.setText(QCoreApplication.translate("Form", u"Done", None))
    # retranslateUi

