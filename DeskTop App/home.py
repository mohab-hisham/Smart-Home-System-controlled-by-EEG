from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import room, bathroom, kitchen, corridor
import sys


class Smarthome(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("UIs/home.ui", self)
        self.living_img = QPixmap("imgs/living.jpeg")
        self.living_label.setPixmap(self.living_img)

        self.room1_img = QPixmap("imgs/room1.jpeg")
        self.room1_label.setPixmap(self.room1_img)

        self.room2_img = QPixmap("imgs/room.jpeg")
        self.room2_label.setPixmap(self.room2_img)

        self.kitchen_img = QPixmap("imgs/kit.jpeg")
        self.kitchen_label.setPixmap(self.kitchen_img)

        self.lobby_img = QPixmap("imgs/lobby.jpeg")
        self.lobby_label.setPixmap(self.lobby_img)

        self.bath_img = QPixmap("imgs/toilet.jpeg")
        self.bath_label.setPixmap(self.bath_img)

        self.room = room.Room()
        self.living = room.Room()
        self.bath = bathroom.BathRoom()
        self.kitchen = kitchen.Kitchen()
        self.corridor = corridor.Corridor()

        self.room.homeButton.clicked.connect(self.returnHome)
        self.room1_Button.clicked.connect(lambda: self.openRoom("Room 1"))
        self.room2_Button.clicked.connect(lambda: self.openRoom("Room 2"))
        self.livingButton.clicked.connect(lambda: self.openRoom("Living Room"))
        self.bathButton.clicked.connect(self.openBath)
        self.bath.homeButton.clicked.connect(self.returnHome)
        self.kitchen.homeButton.clicked.connect(self.returnHome)
        self.kitchenButton.clicked.connect(self.openKitchen)
        self.corridor.homeButton.clicked.connect(self.returnHome)
        self.lobbyButton.clicked.connect(self.openCorridor)

    def returnHome(self):
        self.show()

    def openRoom(self, name):
        self.room.open(name)
        self.close()

    def openBath(self):
        self.bath.open()
        self.close()

    def openKitchen(self):
        self.kitchen.open()
        self.close()

    def openCorridor(self):
        self.corridor.open()
        self.close()





if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    home = Smarthome()
    home.show()
    sys.exit(app.exec_())
