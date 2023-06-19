from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys


class Corridor(qtw.QWidget):
    def __init__(self):
        super().__init__()
        bath = "DeskTop App/"
        uic.loadUi(bath + "UIs/corridorui.ui", self)
        self.light_img = QPixmap(bath + "imgs/lamp2.jpeg")
        self.light_label.setPixmap(self.light_img)

        self.door1_img = QPixmap(bath + "imgs/door.jpeg")
        self.door1_label.setPixmap(self.door1_img)

        self.door2_img = QPixmap(bath + "imgs/door.jpeg")
        self.door2_label.setPixmap(self.door2_img)

        self.toilet_img = QPixmap(bath + "imgs/door.jpeg")
        self.toilet_label.setPixmap(self.toilet_img)

        self.homeButton.clicked.connect(self.closeCorridor)

    def open(self):
        self.show()

    def closeCorridor(self):
        self.close()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    corridor = Corridor()
    corridor.show()
    sys.exit(app.exec_())