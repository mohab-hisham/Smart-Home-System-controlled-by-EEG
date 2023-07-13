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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(884, 300)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cont_groupBox = QGroupBox(Form)
        self.cont_groupBox.setObjectName(u"cont_groupBox")
        self.cont_groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout_3 = QVBoxLayout(self.cont_groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.seq_radioButton = QRadioButton(self.cont_groupBox)
        self.seq_radioButton.setObjectName(u"seq_radioButton")
        self.seq_radioButton.setChecked(True)

        self.verticalLayout.addWidget(self.seq_radioButton)

        self.left_right_radioButton = QRadioButton(self.cont_groupBox)
        self.left_right_radioButton.setObjectName(u"left_right_radioButton")

        self.verticalLayout.addWidget(self.left_right_radioButton)

        self.head_radioButton = QRadioButton(self.cont_groupBox)
        self.head_radioButton.setObjectName(u"head_radioButton")

        self.verticalLayout.addWidget(self.head_radioButton)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.cont_groupBox, 0, 0, 1, 1)

        self.lang_groupBox = QGroupBox(Form)
        self.lang_groupBox.setObjectName(u"lang_groupBox")
        self.lang_groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout_4 = QVBoxLayout(self.lang_groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.arabic_radioButton = QRadioButton(self.lang_groupBox)
        self.arabic_radioButton.setObjectName(u"arabic_radioButton")
        self.arabic_radioButton.setChecked(True)

        self.verticalLayout_2.addWidget(self.arabic_radioButton)

        self.english_radioButton = QRadioButton(self.lang_groupBox)
        self.english_radioButton.setObjectName(u"english_radioButton")

        self.verticalLayout_2.addWidget(self.english_radioButton)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.lang_groupBox, 0, 2, 1, 1)

        self.doneButton = QPushButton(Form)
        self.doneButton.setObjectName(u"doneButton")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        self.doneButton.setFont(font)

        self.gridLayout.addWidget(self.doneButton, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.cont_groupBox.setTitle(QCoreApplication.translate("Form", u"Control Mode", None))
        self.seq_radioButton.setText(QCoreApplication.translate("Form", u"Sequence", None))
        self.left_right_radioButton.setText(QCoreApplication.translate("Form", u"Left and Right ", None))
        self.head_radioButton.setText(QCoreApplication.translate("Form", u"Head Movment", None))
        self.lang_groupBox.setTitle(QCoreApplication.translate("Form", u"Language", None))
        self.arabic_radioButton.setText(QCoreApplication.translate("Form", u"\u0627\u0644\u0639\u0631\u0628\u064a\u0629", None))
        self.english_radioButton.setText(QCoreApplication.translate("Form", u"English", None))
        self.doneButton.setText(QCoreApplication.translate("Form", u"Done", None))
    # retranslateUi

