from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys


class Corridor(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #bath = "DeskTop App/"
        uic.loadUi("UIs/cori.ui", self)

        self.setStyleSheet("background-color: #122222; ")
        #

        common_style = "background-color: #fffff0; border-radius: 90px; border-color: white; background-repeat: no-repeat; "
        self.message_label.setStyleSheet(common_style)

        self.homeButton.setStyleSheet(common_style + "border-image: url(imgs/home.png);")
        self.lightButton.setStyleSheet(common_style + "border-image: url(imgs/light-bulb.png);")
        self.door2Button.setStyleSheet(common_style + "border-image: url(imgs/door.png);")
        self.door1Button.setStyleSheet(common_style + "border-image: url(imgs/door1.png);")
        self.toiletButton.setStyleSheet(common_style + "border-image: url(imgs/wc.png);")

        #self.homeButton.clicked.connect(self.closeCorridor)

    def open(self):
        self.showFullScreen()

    def closeCorridor(self):
        self.close()

    def show_state(self, msg):
        self.message_label.setText(msg)

    def cnt_feedback(self, cnt_val):
        mapp = {17: 'Light', 18: 'Door 1', 19: 'Door 2', 20: "Toilet Door" }
        msg = mapp[cnt_val] + " is turned on."
        self.show_state(msg)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    corridor = Corridor()
    corridor.show()
    sys.exit(app.exec_())