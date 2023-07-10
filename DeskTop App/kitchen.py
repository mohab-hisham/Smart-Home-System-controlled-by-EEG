from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.QtCore import *



class Kitchen(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #bath = "DeskTop App/"
        uic.loadUi("UIs/ki.ui", self)
        self.setStyleSheet("background-color: #122222; ")
        #

        common_style = "background-color: #fffff0; border-radius: 90px; border-color: white; background-repeat: no-repeat; "
        self.message_label.setStyleSheet(common_style)
        self.info_label.setStyleSheet(common_style)

        self.homeButton.setStyleSheet(common_style+"border-image: url(imgs/home.png);")
        self.lightButton.setStyleSheet(common_style+"border-image: url(imgs/light-bulb.png);")
        self.stoveButton.setStyleSheet(common_style+"border-image: url(imgs/oven.png);")
        self.washerButton.setStyleSheet(common_style+"border-image: url(imgs/washing-machine.png);")
        self.chimneyButton.setStyleSheet(common_style+"border-image: url(imgs/food.png);")


        self.lightButton.clicked.connect(lambda: self.kitchen_worker.mouse_intr.emit(1))
        self.stoveButton.clicked.connect(lambda: self.kitchen_worker.mouse_intr.emit(2))
        self.washerButton.clicked.connect(lambda: self.kitchen_worker.mouse_intr.emit(3))
        self.chimneyButton.clicked.connect(lambda: self.kitchen_worker.mouse_intr.emit(4))
        #self.homeButton.clicked.connect(lambda: self.kitchen_worker.mouse_intr.emit(5))


    def open(self):
        print("in show full screen")
        self.show()
        self.showFullScreen()

    def closeKitchen(self):
        self.close()

    def show_state(self, msg):
        self.message_label.setText(msg)

    def cnt_feedback(self, cnt_val):
        mapp = {13: 'Light', 14: 'Stove', 15: 'Washer', 16: "Chimney" }
        msg = mapp[cnt_val] + " is turned on."
        self.show_state(msg)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    kitchen = Kitchen()
    kitchen.showFullScreen()
    sys.exit(app.exec_())