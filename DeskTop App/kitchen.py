from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.QtCore import *
import main as m


class Kitchen(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #bath = "DeskTop App/"
        uic.loadUi("UIs/ki.ui", self)
        self.setStyleSheet("background-color: #122222; ")
        #

        common_style = "background-color: #fffff0; border-radius: 90px; border-color: white; background-repeat: no-repeat; "
        self.message_label.setStyleSheet(common_style)

        self.homeButton.setStyleSheet(common_style+"border-image: url(imgs/home.png);")
        self.lightButton.setStyleSheet(common_style+"border-image: url(imgs/light-bulb.png);")
        self.stoveButton.setStyleSheet(common_style+"border-image: url(imgs/oven.png);")
        self.washerButton.setStyleSheet(common_style+"border-image: url(imgs/washing-machine.png);")
        self.chimneyButton.setStyleSheet(common_style+"border-image: url(imgs/food.png);")

        #self.homeButton.clicked.connect(self.closeKitchen)

        self.kitchen_thr = QThread()
        self.kitchen_worker = m.EEG_Worker()
        self.kitchen_worker.moveToThread(self.kitchen_thr)
        self.kitchen_thr.started.connect(lambda: self.kitchen_worker.navigate(4))
        # self.kitchen_worker.start_sig.connect(self.openKitchen)
        self.kitchen_worker.eye_state.connect(self.show_state)                                                                     #self.kitchen_worker.eye_state.connect(self.kitchen.show_state)
        self.kitchen_worker.cnt_sig.connect(self.cnt_feedback)                                                                       #self.kitchen_worker.cnt_sig.connect(self.kitchen.cnt_feedback)
        self.kitchen_worker.fin.connect(self.close)                                                                    #self.kitchen_worker.fin.connect(self.kitchen.close)
        #self.kitchen_worker.cnt_return.connect(self.cnt_thr.start)
        self.kitchen_worker.fin.connect(self.kitchen_thr.quit)

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
    kitchen.show()
    sys.exit(app.exec_())