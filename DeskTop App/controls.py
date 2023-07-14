from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class Controls(qtw.QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("UIs/cont.ui", self)
        self.setStyleSheet("background-color: #fffff1; ")

    def closeControl(self):
        self.close()

    def get_control_option(self):
        cont = None
        lang = None
        if self.seq_radioButton.isChecked():
            cont = 0
        elif self.left_right_radioButton.isChecked():
            cont = 1
        elif self.left_right_head_radioButton.isChecked():
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