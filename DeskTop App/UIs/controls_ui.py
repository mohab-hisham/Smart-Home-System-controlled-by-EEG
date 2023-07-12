# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'controls.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)
import resources_rc

class Ui_control_form(object):
    def setupUi(self, control_form):
        if not control_form.objectName():
            control_form.setObjectName(u"control_form")
        control_form.resize(683, 447)
        font = QFont()
        font.setFamilies([u"Old Antic Decorative"])
        font.setPointSize(14)
        control_form.setFont(font)
        self.verticalLayout = QVBoxLayout(control_form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.wind_label = QLabel(control_form)
        self.wind_label.setObjectName(u"wind_label")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(14)
        self.wind_label.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.wind_label)

        self.wind_comboBox = QComboBox(control_form)
        self.wind_comboBox.setObjectName(u"wind_comboBox")
        self.wind_comboBox.setFont(font1)
        self.wind_comboBox.setEditable(False)
        self.wind_comboBox.setCurrentText(u"")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.wind_comboBox)

        self.item_label = QLabel(control_form)
        self.item_label.setObjectName(u"item_label")
        self.item_label.setFont(font1)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.item_label)

        self.item_comboBox = QComboBox(control_form)
        self.item_comboBox.setObjectName(u"item_comboBox")
        self.item_comboBox.setFont(font1)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.item_comboBox)

        self.seq_len_label = QLabel(control_form)
        self.seq_len_label.setObjectName(u"seq_len_label")
        self.seq_len_label.setFont(font1)

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.seq_len_label)

        self.seq_len_spinBox = QSpinBox(control_form)
        self.seq_len_spinBox.setObjectName(u"seq_len_spinBox")
        self.seq_len_spinBox.setFont(font1)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.seq_len_spinBox)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout.setItem(0, QFormLayout.LabelRole, self.horizontalSpacer_7)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout.setItem(1, QFormLayout.LabelRole, self.horizontalSpacer_8)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout.setItem(2, QFormLayout.LabelRole, self.horizontalSpacer_9)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(4, QFormLayout.LabelRole, self.verticalSpacer_4)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(7, QFormLayout.LabelRole, self.verticalSpacer_5)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(5, QFormLayout.LabelRole, self.verticalSpacer_8)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(8, QFormLayout.LabelRole, self.verticalSpacer_9)


        self.horizontalLayout.addLayout(self.formLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.index_label = QLabel(control_form)
        self.index_label.setObjectName(u"index_label")
        self.index_label.setFont(font1)
        self.index_label.setAutoFillBackground(False)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.index_label)

        self.index_comboBox = QComboBox(control_form)
        self.index_comboBox.setObjectName(u"index_comboBox")
        self.index_comboBox.setFont(font1)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.index_comboBox)

        self.blink_label = QLabel(control_form)
        self.blink_label.setObjectName(u"blink_label")
        self.blink_label.setFont(font1)

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.blink_label)

        self.blink_comboBox = QComboBox(control_form)
        self.blink_comboBox.setObjectName(u"blink_comboBox")
        self.blink_comboBox.setFont(font1)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.blink_comboBox)

        self.duration_label = QLabel(control_form)
        self.duration_label.setObjectName(u"duration_label")
        self.duration_label.setFont(font1)

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.duration_label)

        self.duration_comboBox = QComboBox(control_form)
        self.duration_comboBox.setObjectName(u"duration_comboBox")
        self.duration_comboBox.setFont(font1)

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.duration_comboBox)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout_2.setItem(0, QFormLayout.LabelRole, self.horizontalSpacer_10)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout_2.setItem(1, QFormLayout.LabelRole, self.horizontalSpacer_11)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout_2.setItem(2, QFormLayout.LabelRole, self.horizontalSpacer_12)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(5, QFormLayout.LabelRole, self.verticalSpacer_6)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(8, QFormLayout.LabelRole, self.verticalSpacer_7)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(4, QFormLayout.LabelRole, self.verticalSpacer_10)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(7, QFormLayout.LabelRole, self.verticalSpacer_11)


        self.horizontalLayout.addLayout(self.formLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 4)
        self.horizontalLayout.setStretch(4, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.addButton = QPushButton(control_form)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setFont(font1)

        self.horizontalLayout_7.addWidget(self.addButton)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_13)

        self.pushButton = QPushButton(control_form)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_7.addWidget(self.pushButton)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.doneButton = QPushButton(control_form)
        self.doneButton.setObjectName(u"doneButton")
        self.doneButton.setFont(font1)

        self.horizontalLayout_7.addWidget(self.doneButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(3, 3)
        self.verticalLayout.setStretch(4, 3)

        self.retranslateUi(control_form)

        self.wind_comboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(control_form)
    # setupUi

    def retranslateUi(self, control_form):
        control_form.setWindowTitle(QCoreApplication.translate("control_form", u"Controls", None))
        self.wind_label.setText(QCoreApplication.translate("control_form", u"Window", None))
        self.item_label.setText(QCoreApplication.translate("control_form", u"Item", None))
        self.seq_len_label.setText(QCoreApplication.translate("control_form", u"Sequence Length", None))
        self.index_label.setText(QCoreApplication.translate("control_form", u"Index", None))
        self.blink_label.setText(QCoreApplication.translate("control_form", u"Blink", None))
        self.duration_label.setText(QCoreApplication.translate("control_form", u"Duration After Blink", None))
        self.addButton.setText(QCoreApplication.translate("control_form", u"Add", None))
        self.pushButton.setText(QCoreApplication.translate("control_form", u"PushButton", None))
        self.doneButton.setText(QCoreApplication.translate("control_form", u"Done", None))
    # retranslateUi

