from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys


class Kitchen(qtw.QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("UIs/kitchen.ui", self)
        self.light_img = QPixmap("imgs/lamp2.jpeg")
        self.light_label.setPixmap(self.light_img)

        self.washer_img = QPixmap("imgs/washer.jpeg")
        self.washer_label.setPixmap(self.washer_img)

        self.stove_img = QPixmap("imgs/stove.jpeg")
        self.stove_label.setPixmap(self.stove_img)

        self.chimney_img = QPixmap("imgs/smoke.jpeg")
        self.chimney_label.setPixmap(self.chimney_img)

        self.homeButton.clicked.connect(self.closeKitchen)

    def open(self):
        self.show()

    def closeKitchen(self):
        self.close()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    kitchen = Kitchen()
    kitchen.show()
    sys.exit(app.exec_())