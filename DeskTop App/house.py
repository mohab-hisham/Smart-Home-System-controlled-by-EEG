from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.QtCore import *
import main as m


class Home(qtw.QWidget):

    def __init__(self):
        super().__init__()
        #self.interrupt = [0, 0]

        bath = ""
        uic.loadUi(bath + "UIs/h2.ui", self)

        self.setStyleSheet("background-color: #122222; ")


        common_style = "background-color: #fffff0; border-radius: 90px; border-color: white; background-repeat: no-repeat; "
        self.message_label.setStyleSheet(
            "background-color: #fffff0; border-radius: 30px; border-color: white; background-repeat: no-repeat; ")
        self.info_label.setStyleSheet(
            "background-color: #fffff0; border-radius: 30px; border-color: white; background-repeat: no-repeat;")
        self.exitButton.setStyleSheet("background-color: #ff0000; border-radius: 30px; border-color: white;")
        self.livingButton.setStyleSheet(common_style + "border-image: url(imgs/living.jpeg);")
        self.room1_Button.setStyleSheet(common_style + "border-image: url(imgs/room1.jpeg);")
        self.room2_Button.setStyleSheet(common_style + "border-image: url(imgs/room.jpeg);")
        self.kitchenButton.setStyleSheet(common_style + "border-image: url(imgs/kit.jpeg);")
        self.lobbyButton.setStyleSheet(common_style + "border-image: url(imgs/lobby.jpeg);")
        self.bathButton.setStyleSheet(common_style + "border-image: url(imgs/to.jpg);")

        self.exitButton.clicked.connect(self.closeHome)

    def closeHome(self):
        self.close()

    def show_state(self, msg):
        self.message_label.setText(msg)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    home = Home()
    home.show()
    sys.exit(app.exec_())
