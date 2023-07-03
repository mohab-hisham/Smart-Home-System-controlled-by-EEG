from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class Fall(qtw.QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("UIs/fall.ui", self)
        self.backButton.clicked.connect(self.closeFall)

    def closeFall(self):
        self.close()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    fall = Fall()
    fall.show()
    sys.exit(app.exec_())