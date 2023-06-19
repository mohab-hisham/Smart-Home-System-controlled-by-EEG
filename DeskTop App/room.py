from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class Room(qtw.QWidget):
    def __init__(self):
        super().__init__()
        bath = "DeskTop App/"
        uic.loadUi(bath + "UIs/living.ui", self)
        self.light_img = QPixmap(bath + "imgs/light.jpeg")
        self.light_label.setPixmap(self.light_img)

        self.tv_img = QPixmap(bath + "imgs/tv.jpeg")
        self.tv_label.setPixmap(self.tv_img)

        self.fan_img = QPixmap(bath + "imgs/fan.jpeg")
        self.fan_label.setPixmap(self.fan_img)

        self.carten_img = QPixmap(bath + "imgs/cartens.jpeg")
        self.carten_label.setPixmap(self.carten_img)

        self.homeButton.clicked.connect(self.closeRoom)

    def closeRoom(self):
        self.close()

    def open(self, name):
        self.setWindowTitle(name)
        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    room = Room()
    room.show()
    sys.exit(app.exec_())