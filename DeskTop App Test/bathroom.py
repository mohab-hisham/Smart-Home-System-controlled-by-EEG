from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class BathRoom(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #bath = "DeskTop App/"
        uic.loadUi("UIs/toi.ui", self)

        self.setStyleSheet("background-color: #122222; ")
        #

        common_style = "background-color: #fffff0; border-radius: 90px; border-color: white; background-repeat: no-repeat; "
        self.message_label.setStyleSheet(common_style)
        self.info_label.setStyleSheet(common_style)

        self.homeButton.setStyleSheet(common_style + "border-image: url(imgs/home.png);")
        self.lightButton.setStyleSheet(common_style + "border-image: url(imgs/light-bulb.png);")
        self.bidetButton.setStyleSheet(common_style + "border-image: url(imgs/bidet.jpeg);")
        self.coverButton.setStyleSheet(common_style + "border-image: url(imgs/cover.jpeg);")
        self.flushButton.setStyleSheet(common_style + "border-image: url(imgs/flush.jpeg);")



    def open(self):
        self.setWindowTitle("Bath Room")
        self.showFullScreen()

    def closeBath(self):
        self.close()

    def show_state(self, msg):
        self.message_label.setText(msg)

    def cnt_feedback(self, cnt_val):
        mapp = {21: 'Light', 22: 'Bidet', 23: 'Toilet Cover', 24: 'Flush'}
        msg = mapp[cnt_val] + " is turned on."
        self.show_state(msg)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    bath = BathRoom()
    bath.show()
    sys.exit(app.exec_())