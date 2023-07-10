from PyQt5 import QtWidgets as qtw
from PyQt5 import uic, QtCore
from PyQt5.QtGui import QPixmap
import sys

class Room(qtw.QWidget):
    def __init__(self, name):
        super().__init__()
        #bath = "DeskTop App/"
        uic.loadUi("UIs/l2.ui", self)
        self.message_label.setText(name)
        self.setStyleSheet("background-color: #122222; ")


        common_style = "background-color: #fffff0; border-radius: 90px; border-color: white; background-repeat: no-repeat; "
        self.message_label.setStyleSheet(common_style)

        self.homeButton.setStyleSheet(common_style + "border-image: url(imgs/home.png);")
        self.fanButton.setStyleSheet(common_style + "border-image: url(imgs/fan.png);")
        self.tvButton.setStyleSheet(common_style + "border-image: url(imgs/smart-tv.png);")
        self.cartensButton.setStyleSheet(common_style + "border-image: url(imgs/curtains.png);")
        self.lightButton.setStyleSheet(common_style + "border-image: url(imgs/light-bulb.png);")
        #self.homeButton.clicked.connect(self.closeRoom)



    def closeRoom(self):
        self.close()

    def open(self, name):
        self.message_label.setText(name)
        self.showFullScreen()

    def show_state(self, msg):
        self.message_label.setText(msg)

    def cnt_feedback(self, cnt_val):
        mapp = {1: 'Light', 2: 'Cartens', 3: 'TV', 4: "Fan", 5: 'Light', 6: 'Cartens', 7: 'TV', 8: "Fan", 9: 'Light',
                10: 'Cartens', 11: 'TV', 12: "Fan"}
        msg = mapp[cnt_val] + " is turned on."
        self.show_state(msg)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    room = Room()
    room.show()
    sys.exit(app.exec_())