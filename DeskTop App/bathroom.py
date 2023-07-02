from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class BathRoom(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #bath = "DeskTop App/"
        uic.loadUi("UIs/toilet.ui", self)
        self.light_img = QPixmap("imgs/light.jpeg")
        self.light_label.setPixmap(self.light_img)

        self.bidet_img = QPixmap("imgs/bidet.jpeg")
        self.bidet_label.setPixmap(self.bidet_img)

        self.flush_img = QPixmap("imgs/flush.jpeg")
        self.flush_label.setPixmap(self.flush_img)

        self.cover_img = QPixmap("imgs/cover.jpeg")
        self.cover_label.setPixmap(self.cover_img)

        self.homeButton.clicked.connect(self.closeBath)

    def open(self):
        self.setWindowTitle("Bath Room")
        self.show()

    def closeBath(self):
        self.close()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    bath = BathRoom()
    bath.show()
    sys.exit(app.exec_())