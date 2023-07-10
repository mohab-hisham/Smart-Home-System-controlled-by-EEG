from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class Controls(qtw.QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("UIs/controls.ui", self)

        #self.doneButton.clicked.connect(self.closeControl)

    def closeControl(self):
        self.close()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    control = Controls()
    control.show()
    sys.exit(app.exec_())