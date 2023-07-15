from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class Controls(qtw.QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("UIs/cont.ui", self)
        self.setStyleSheet("background-color: #fffff1; ")

        #self.blink_len_comboBox.addItem(["Short Blink", "Long Blink"])
        #self.duration_comboBox.addItem(["Short Duration", "Long Duration"])
        #self.item_comboBox.addItem(["1", "2", "3", "4", "5", "6", "7"])
        #self.item_comboBox.addItem(["1", "2", "3", "4", "5", "6", "7"])


        #self.seq_len_spinBox.valueChanged.connect()
        self.group_style = "background-color: #cccccc; border-radius: 70px;  border: 10px solid black;"
        self.btn_style = "background-color: #cccccc;border-radius: 0px;  border: 0px solid black;"
        self.combo_style = "background-color: #fffff1;border-radius: 1px;  border: 2px solid black;"
        self.lang_groupBox.setStyleSheet(self.group_style)
        self.custom_groupBox.setStyleSheet(self.group_style)
        self.cont_groupBox.setStyleSheet(self.group_style)
        self.arabic_radioButton.setStyleSheet(self.btn_style)
        self.english_radioButton.setStyleSheet(self.btn_style)
        self.seq_radioButton.setStyleSheet(self.btn_style)
        self.left_right_radioButton.setStyleSheet(self.btn_style)
        self.head_radioButton.setStyleSheet(self.btn_style)
        self.left_right_head_radioButton.setStyleSheet(self.btn_style)
        self.seq_len_label.setStyleSheet(self.btn_style)
        self.index_label.setStyleSheet(self.btn_style)
        self.blink_len_label.setStyleSheet(self.btn_style)
        self.duration_label.setStyleSheet(self.btn_style)
        self.item_label.setStyleSheet(self.btn_style)
        self.seq_len_spinBox.setStyleSheet(self.combo_style)
        self.index_comboBox.setStyleSheet(self.combo_style)
        self.blink_len_comboBox.setStyleSheet(self.combo_style)
        self.duration_comboBox.setStyleSheet(self.combo_style)
        self.item_comboBox.setStyleSheet(self.combo_style)
        self.doneButton.setStyleSheet("background-color: #9ACD32; border-radius: 30px;  border: 10px solid black;")

    def closeControl(self):
        self.close()

    def get_control_option(self):
        cont = None
        lang = None
        if self.seq_radioButton.isChecked():
            cont = 0
        elif self.left_right_radioButton.isChecked():
            cont = 1
        elif self.head_radioButton.isChecked():
            cont = 2
        else:
            cont = 3

        if self.arabic_radioButton.isChecked():
            lang = 1
        else:
            lang =0

        return cont, lang


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    control = Controls()
    control.show()
    sys.exit(app.exec_())