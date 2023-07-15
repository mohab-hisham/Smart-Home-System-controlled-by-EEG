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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1308, 770)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_10 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_10, 1, 6, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 0, 4, 1, 1)

        self.doneButton = QPushButton(Form)
        self.doneButton.setObjectName(u"doneButton")
        sizePolicy.setHeightForWidth(self.doneButton.sizePolicy().hasHeightForWidth())
        self.doneButton.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(40)
        self.doneButton.setFont(font)
        self.doneButton.setAutoDefault(True)
        self.doneButton.setFlat(False)

        self.gridLayout.addWidget(self.doneButton, 5, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 0, 2, 1, 1)

        self.cont_groupBox = QGroupBox(Form)
        self.cont_groupBox.setObjectName(u"cont_groupBox")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(30)
        self.cont_groupBox.setFont(font1)
        self.cont_groupBox.setAlignment(Qt.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.cont_groupBox)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(8, 0, 8, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.left_right_head_radioButton = QRadioButton(self.cont_groupBox)
        self.left_right_head_radioButton.setObjectName(u"left_right_head_radioButton")
        sizePolicy.setHeightForWidth(self.left_right_head_radioButton.sizePolicy().hasHeightForWidth())
        self.left_right_head_radioButton.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(20)
        self.left_right_head_radioButton.setFont(font2)

        self.gridLayout_2.addWidget(self.left_right_head_radioButton, 4, 1, 1, 1)

        self.left_right_radioButton = QRadioButton(self.cont_groupBox)
        self.left_right_radioButton.setObjectName(u"left_right_radioButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.left_right_radioButton.sizePolicy().hasHeightForWidth())
        self.left_right_radioButton.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(20)
        self.left_right_radioButton.setFont(font3)

        self.gridLayout_2.addWidget(self.left_right_radioButton, 2, 1, 1, 1)

        self.head_radioButton = QRadioButton(self.cont_groupBox)
        self.head_radioButton.setObjectName(u"head_radioButton")
        sizePolicy.setHeightForWidth(self.head_radioButton.sizePolicy().hasHeightForWidth())
        self.head_radioButton.setSizePolicy(sizePolicy)
        self.head_radioButton.setFont(font2)

        self.gridLayout_2.addWidget(self.head_radioButton, 3, 1, 1, 1)

        self.seq_radioButton = QRadioButton(self.cont_groupBox)
        self.seq_radioButton.setObjectName(u"seq_radioButton")
        sizePolicy.setHeightForWidth(self.seq_radioButton.sizePolicy().hasHeightForWidth())
        self.seq_radioButton.setSizePolicy(sizePolicy)
        self.seq_radioButton.setFont(font2)
        self.seq_radioButton.setChecked(True)

        self.gridLayout_2.addWidget(self.seq_radioButton, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 5, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_13, 2, 0, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 2)
        self.gridLayout_2.setRowStretch(2, 2)
        self.gridLayout_2.setRowStretch(3, 2)
        self.gridLayout_2.setRowStretch(4, 2)
        self.gridLayout_2.setRowStretch(5, 1)
        self.gridLayout_2.setColumnStretch(0, 3)
        self.gridLayout_2.setColumnStretch(1, 3)
        self.gridLayout_2.setColumnStretch(2, 2)

        self.gridLayout.addWidget(self.cont_groupBox, 0, 1, 4, 1)

        self.horizontalSpacer_9 = QSpacerItem(419, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 0, 0, 1, 1)

        self.lang_groupBox = QGroupBox(Form)
        self.lang_groupBox.setObjectName(u"lang_groupBox")
        sizePolicy.setHeightForWidth(self.lang_groupBox.sizePolicy().hasHeightForWidth())
        self.lang_groupBox.setSizePolicy(sizePolicy)
        self.lang_groupBox.setFont(font1)
        self.lang_groupBox.setAlignment(Qt.AlignCenter)
        self.gridLayout_4 = QGridLayout(self.lang_groupBox)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(15, 0, 0, 0)
        self.english_radioButton = QRadioButton(self.lang_groupBox)
        self.english_radioButton.setObjectName(u"english_radioButton")
        sizePolicy.setHeightForWidth(self.english_radioButton.sizePolicy().hasHeightForWidth())
        self.english_radioButton.setSizePolicy(sizePolicy)
        self.english_radioButton.setFont(font2)

        self.gridLayout_4.addWidget(self.english_radioButton, 2, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 51, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_4, 3, 1, 1, 1)

        self.arabic_radioButton = QRadioButton(self.lang_groupBox)
        self.arabic_radioButton.setObjectName(u"arabic_radioButton")
        sizePolicy.setHeightForWidth(self.arabic_radioButton.sizePolicy().hasHeightForWidth())
        self.arabic_radioButton.setSizePolicy(sizePolicy)
        self.arabic_radioButton.setFont(font2)
        self.arabic_radioButton.setChecked(True)

        self.gridLayout_4.addWidget(self.arabic_radioButton, 1, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 51, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(1, 4)
        self.gridLayout_4.setRowStretch(2, 4)
        self.gridLayout_4.setRowStretch(3, 1)
        self.gridLayout_4.setColumnStretch(0, 3)
        self.gridLayout_4.setColumnStretch(1, 3)
        self.gridLayout_4.setColumnStretch(2, 2)

        self.gridLayout.addWidget(self.lang_groupBox, 0, 5, 4, 1)

        self.custom_groupBox = QGroupBox(Form)
        self.custom_groupBox.setObjectName(u"custom_groupBox")
        sizePolicy1.setHeightForWidth(self.custom_groupBox.sizePolicy().hasHeightForWidth())
        self.custom_groupBox.setSizePolicy(sizePolicy1)
        self.custom_groupBox.setFont(font1)
        self.custom_groupBox.setAlignment(Qt.AlignCenter)
        self.gridLayout_3 = QGridLayout(self.custom_groupBox)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(8, 0, 8, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_7, 2, 0, 1, 1)

        self.duration_label = QLabel(self.custom_groupBox)
        self.duration_label.setObjectName(u"duration_label")
        sizePolicy.setHeightForWidth(self.duration_label.sizePolicy().hasHeightForWidth())
        self.duration_label.setSizePolicy(sizePolicy)
        self.duration_label.setFont(font2)

        self.gridLayout_3.addWidget(self.duration_label, 3, 1, 1, 1)

        self.duration_comboBox = QComboBox(self.custom_groupBox)
        self.duration_comboBox.setObjectName(u"duration_comboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.duration_comboBox.sizePolicy().hasHeightForWidth())
        self.duration_comboBox.setSizePolicy(sizePolicy2)
        self.duration_comboBox.setFont(font2)
        self.duration_comboBox.setEditable(True)

        self.gridLayout_3.addWidget(self.duration_comboBox, 3, 2, 1, 1)

        self.item_comboBox = QComboBox(self.custom_groupBox)
        self.item_comboBox.setObjectName(u"item_comboBox")
        sizePolicy2.setHeightForWidth(self.item_comboBox.sizePolicy().hasHeightForWidth())
        self.item_comboBox.setSizePolicy(sizePolicy2)
        self.item_comboBox.setFont(font2)
        self.item_comboBox.setEditable(True)

        self.gridLayout_3.addWidget(self.item_comboBox, 4, 2, 1, 1)

        self.index_comboBox = QComboBox(self.custom_groupBox)
        self.index_comboBox.setObjectName(u"index_comboBox")
        sizePolicy2.setHeightForWidth(self.index_comboBox.sizePolicy().hasHeightForWidth())
        self.index_comboBox.setSizePolicy(sizePolicy2)
        self.index_comboBox.setFont(font2)
        self.index_comboBox.setEditable(True)

        self.gridLayout_3.addWidget(self.index_comboBox, 1, 2, 1, 1)

        self.blink_len_comboBox = QComboBox(self.custom_groupBox)
        self.blink_len_comboBox.setObjectName(u"blink_len_comboBox")
        sizePolicy2.setHeightForWidth(self.blink_len_comboBox.sizePolicy().hasHeightForWidth())
        self.blink_len_comboBox.setSizePolicy(sizePolicy2)
        self.blink_len_comboBox.setFont(font2)
        self.blink_len_comboBox.setEditable(True)

        self.gridLayout_3.addWidget(self.blink_len_comboBox, 2, 2, 1, 1)

        self.blink_len_label = QLabel(self.custom_groupBox)
        self.blink_len_label.setObjectName(u"blink_len_label")
        sizePolicy.setHeightForWidth(self.blink_len_label.sizePolicy().hasHeightForWidth())
        self.blink_len_label.setSizePolicy(sizePolicy)
        self.blink_len_label.setFont(font2)

        self.gridLayout_3.addWidget(self.blink_len_label, 2, 1, 1, 1)

        self.item_label = QLabel(self.custom_groupBox)
        self.item_label.setObjectName(u"item_label")
        sizePolicy.setHeightForWidth(self.item_label.sizePolicy().hasHeightForWidth())
        self.item_label.setSizePolicy(sizePolicy)
        self.item_label.setFont(font2)

        self.gridLayout_3.addWidget(self.item_label, 4, 1, 1, 1)

        self.seq_len_label = QLabel(self.custom_groupBox)
        self.seq_len_label.setObjectName(u"seq_len_label")
        sizePolicy.setHeightForWidth(self.seq_len_label.sizePolicy().hasHeightForWidth())
        self.seq_len_label.setSizePolicy(sizePolicy)
        self.seq_len_label.setFont(font2)

        self.gridLayout_3.addWidget(self.seq_len_label, 0, 1, 1, 1)

        self.seq_len_spinBox = QSpinBox(self.custom_groupBox)
        self.seq_len_spinBox.setObjectName(u"seq_len_spinBox")
        sizePolicy2.setHeightForWidth(self.seq_len_spinBox.sizePolicy().hasHeightForWidth())
        self.seq_len_spinBox.setSizePolicy(sizePolicy2)
        self.seq_len_spinBox.setFont(font2)

        self.gridLayout_3.addWidget(self.seq_len_spinBox, 0, 2, 1, 1)

        self.index_label = QLabel(self.custom_groupBox)
        self.index_label.setObjectName(u"index_label")
        sizePolicy.setHeightForWidth(self.index_label.sizePolicy().hasHeightForWidth())
        self.index_label.setSizePolicy(sizePolicy)
        self.index_label.setFont(font2)

        self.gridLayout_3.addWidget(self.index_label, 1, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_8, 2, 3, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_11, 0, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_12, 0, 3, 1, 1)

        self.gridLayout_3.setRowStretch(0, 2)
        self.gridLayout_3.setRowStretch(1, 2)
        self.gridLayout_3.setRowStretch(2, 2)
        self.gridLayout_3.setRowStretch(3, 2)
        self.gridLayout_3.setRowStretch(4, 2)
        self.gridLayout_3.setColumnStretch(0, 2)
        self.gridLayout_3.setColumnStretch(1, 3)
        self.gridLayout_3.setColumnStretch(2, 3)
        self.gridLayout_3.setColumnStretch(3, 2)

        self.gridLayout.addWidget(self.custom_groupBox, 0, 3, 4, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 4, 3, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 10)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(5, 2)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 20)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 20)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout.setColumnStretch(5, 20)
        self.gridLayout.setColumnStretch(6, 1)

        self.retranslateUi(Form)

        self.doneButton.setDefault(False)
        self.blink_len_comboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.doneButton.setText(QCoreApplication.translate("Form", u"Done", None))
        self.cont_groupBox.setTitle(QCoreApplication.translate("Form", u"Control Mode", None))
        self.left_right_head_radioButton.setText(QCoreApplication.translate("Form", u"Left and Right with Head", None))
        self.left_right_radioButton.setText(QCoreApplication.translate("Form", u"Left and Right ", None))
        self.head_radioButton.setText(QCoreApplication.translate("Form", u"Head Movment", None))
        self.seq_radioButton.setText(QCoreApplication.translate("Form", u"Sequence", None))
        self.lang_groupBox.setTitle(QCoreApplication.translate("Form", u"Language", None))
        self.english_radioButton.setText(QCoreApplication.translate("Form", u"English", None))
        self.arabic_radioButton.setText(QCoreApplication.translate("Form", u"\u0627\u0644\u0639\u0631\u0628\u064a\u0629", None))
        self.custom_groupBox.setTitle(QCoreApplication.translate("Form", u"Customize Sequence", None))
        self.duration_label.setText(QCoreApplication.translate("Form", u"Duration After Blink", None))
        self.blink_len_comboBox.setCurrentText("")
        self.blink_len_label.setText(QCoreApplication.translate("Form", u"Blink Length", None))
        self.item_label.setText(QCoreApplication.translate("Form", u"Item", None))
        self.seq_len_label.setText(QCoreApplication.translate("Form", u"Sequence Length", None))
        self.index_label.setText(QCoreApplication.translate("Form", u"Index", None))
    # retranslateUi

