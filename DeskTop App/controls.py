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
        if self.seq_radioButton.isChecked():
            return 0
        elif self.left_right_radioButton.isChecked():
            return 1
        else:
            return 2


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    control = Controls()
    control.show()
    sys.exit(app.exec_())