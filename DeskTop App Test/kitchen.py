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

        self.selected = 0
        self.on_or_off = {1: 0, 2: 0, 3: 0, 4: 0}
        self.on_off_background = {1: "background-color: #ffff30;", 0: "background-color: #666660;"}
        self.dic = {1: ["Light", self.lightButton], 2: ["Stove", self.stoveButton], 3: ["Washing Machine", self.washerButton],
                    4: ["Chimney", self.chimneyButton], 5: ["Home", self.homeButton]}

        self.img_styles = {1: "border-image: url(imgs/light-bulb.png);", 2: "border-image: url(imgs/oven.png);",
                           3: "border-image: url(imgs/washing-machine.png);", 4: "border-image: url(imgs/food.png);",
                           5: "border-image: url(imgs/home.png);"}

        self.common_style = "border-radius: 90px; border: 10px solid red; background-repeat: no-repeat; "
        self.message_label.setStyleSheet(self.common_style + "background-color: #fffff0;")
        self.info_label.setStyleSheet(self.common_style + "background-color: #fffff0;")

        self.lightButton.setStyleSheet(
            self.common_style + self.img_styles[1] + self.on_off_background[self.on_or_off[1]])
        self.stoveButton.setStyleSheet(
            self.common_style + self.img_styles[2] + self.on_off_background[self.on_or_off[2]])
        self.washerButton.setStyleSheet(
            self.common_style + self.img_styles[3] + self.on_off_background[self.on_or_off[3]])
        self.chimneyButton.setStyleSheet(
            self.common_style + self.img_styles[4] + self.on_off_background[self.on_or_off[4]])
        self.homeButton.setStyleSheet(self.common_style + self.img_styles[5])





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

    def select(self, item_no):
        print("in rooom select")
        new_style = "background-color: #fffff0; border-radius: 90px; border: 10px solid green; background-repeat: no-repeat; "
        if self.selected != 0:
            self.reset_selection()

        if item_no != 5 or m.CntWorker.control_mode:
            self.dic[item_no][1].setStyleSheet(new_style)
            if m.CntWorker.isArabic:
                self.dic[item_no][1].setText(self.dic[item_no][2])
            else:
                self.dic[item_no][1].setText(self.dic[item_no][0])
            self.selected = item_no

        else:
            self.selected = 0

    def reset_selection(self):
        if self.selected != 5:
            self.dic[self.selected][1].setStyleSheet(self.common_style + self.img_styles[self.selected]
                                                     + self.on_off_background[self.on_or_off[self.selected]])
        else:
            self.dic[self.selected][1].setStyleSheet(self.common_style + self.img_styles[self.selected])
        self.dic[self.selected][1].setText("")

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    kitchen = Kitchen()
    kitchen.showFullScreen()
    sys.exit(app.exec_())