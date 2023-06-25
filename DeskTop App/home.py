from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import room, bathroom, kitchen, corridor
import sys
import main
from main import start_threads
from PyQt5.QtCore import *


class Smarthome(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.cnt_thr = QThread()
        self.cnt_worker = main.CntWorker()
        self.cnt_worker.moveToThread(self.cnt_thr)
        self.cnt_thr.started.connect(self.show)
        self.cnt_thr.started.connect(self.cnt_worker.choose)
        self.cnt_worker.eeg_cnt.connect(self.control)
        self.cnt_worker.fin.connect(self.cnt_thr.quit)
        bath = "DeskTop App/"
        uic.loadUi(bath + "UIs/home.ui", self)
        self.living_img = QPixmap(bath + "imgs/living.jpeg")
        self.living_label.setPixmap(self.living_img)

        self.room1_img = QPixmap(bath + "imgs/room1.jpeg")
        self.room1_label.setPixmap(self.room1_img)

        self.room2_img = QPixmap(bath + "imgs/room.jpeg")
        self.room2_label.setPixmap(self.room2_img)

        self.kitchen_img = QPixmap(bath + "imgs/kit.jpeg")
        self.kitchen_label.setPixmap(self.kitchen_img)

        self.lobby_img = QPixmap(bath + "imgs/lobby.jpeg")
        self.lobby_label.setPixmap(self.lobby_img)

        self.bath_img = QPixmap(bath + "imgs/toilet.jpeg")
        self.bath_label.setPixmap(self.bath_img)

        self.room1 = room.Room()
        self.room2 = room.Room()
        self.living = room.Room()
        self.bath = bathroom.BathRoom()
        self.kitchen = kitchen.Kitchen()
        self.corridor = corridor.Corridor()

        self.room1.homeButton.clicked.connect(self.returnHome)
        self.room2.homeButton.clicked.connect(self.returnHome)
        self.living.homeButton.clicked.connect(self.returnHome)
        self.room1_Button.clicked.connect(lambda: self.room1.open("Room 1"))
        self.room1_Button.clicked.connect(self.close)
        self.room2_Button.clicked.connect(lambda: self.room2.open("Room 2"))
        self.room2_Button.clicked.connect(self.close)
        self.livingButton.clicked.connect(lambda: self.living.open("Living Room"))
        self.livingButton.clicked.connect(self.close)
        self.bathButton.clicked.connect(self.openBath)
        self.bath.homeButton.clicked.connect(self.returnHome)
        self.kitchen.homeButton.clicked.connect(self.returnHome)
        self.kitchenButton.clicked.connect(self.openKitchen)
        self.corridor.homeButton.clicked.connect(self.returnHome)
        self.lobbyButton.clicked.connect(self.openCorridor)

        self.living_thr = QThread()
        self.living_worker = main.EEG_Worker()
        self.living_worker.moveToThread(self.living_thr)
        self.living_thr.started.connect(self.living_worker.navigate)
        self.living_worker.eeg_sig.connect(lambda: self.living.open("Living Room"))
        self.living_worker.eeg_sig.connect(self.close)
        self.living_worker.fin.connect(self.living.close)
        self.living_worker.cnt_return.connect(self.cnt_thr.start)
        self.living_worker.fin.connect(self.living_thr.quit)

        self.room1_thr = QThread()
        self.room1_worker = main.EEG_Worker()
        self.room1_worker.moveToThread(self.room1_thr)
        self.room1_thr.started.connect(self.room1_worker.navigate)
        self.room1_worker.eeg_sig.connect(lambda: self.room1.open("Room 1"))
        self.room1_worker.eeg_sig.connect(self.close)
        self.room1_worker.fin.connect(self.room1.close)
        self.room1_worker.cnt_return.connect(self.cnt_thr.start)
        self.room1_worker.fin.connect(self.room1_thr.quit)

        self.room2_thr = QThread()
        self.room2_worker = main.EEG_Worker()
        self.room2_worker.moveToThread(self.room2_thr)
        self.room2_thr.started.connect(self.room2_worker.navigate)
        self.room2_worker.eeg_sig.connect(lambda: self.room2.open("Room 2"))
        self.room2_worker.eeg_sig.connect(self.close)
        self.room2_worker.fin.connect(self.room2.close)
        self.room2_worker.cnt_return.connect(self.cnt_thr.start)
        self.room2_worker.fin.connect(self.room2_thr.quit)

        self.corridor_thr = QThread()
        self.corridor_worker = main.EEG_Worker()
        self.corridor_worker.moveToThread(self.corridor_thr)
        self.corridor_thr.started.connect(self.corridor_worker.navigate)
        self.corridor_worker.eeg_sig.connect(self.openCorridor)
        self.corridor_worker.fin.connect(self.corridor.close)
        self.corridor_worker.cnt_return.connect(self.cnt_thr.start)
        self.corridor_worker.fin.connect(self.corridor_thr.quit)

        self.bath_thr = QThread()
        self.bath_worker = main.EEG_Worker()
        self.bath_worker.moveToThread(self.bath_thr)
        self.bath_thr.started.connect(self.bath_worker.navigate)
        self.bath_worker.eeg_sig.connect(self.openBath)
        self.bath_worker.fin.connect(self.bath.close)
        self.bath_worker.cnt_return.connect(self.cnt_thr.start)
        self.bath_worker.fin.connect(self.bath_thr.quit)

        self.kitchen_thr = QThread()
        self.kitchen_worker = main.EEG_Worker()
        self.kitchen_worker.moveToThread(self.kitchen_thr)
        self.kitchen_thr.started.connect(self.kitchen_worker.navigate)
        self.kitchen_worker.eeg_sig.connect(self.openKitchen)
        self.kitchen_worker.fin.connect(self.kitchen.close)
        self.kitchen_worker.cnt_return.connect(self.cnt_thr.start)
        self.kitchen_worker.fin.connect(self.kitchen_thr.quit)

    def control(self, code):
        dic = {1: self.living_thr, 2: self.room1_thr, 3: self.room2_thr,
               4: self.kitchen_thr, 5: self.corridor_thr, 6: self.bath_thr}
        dic[code].start()

    def returnHome(self):
        self.show()

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
    start_threads()
    home = Smarthome()
    home.cnt_thr.start()
    sys.exit(app.exec_())

