from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys
import main as m

class BathRoom(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #bath = "DeskTop App/"
        uic.loadUi("UIs/toi.ui", self)

        self.setStyleSheet("background-color: #122222; ")
        self.selected = 0
        self.on_off_background = {1: "background-color: #ffff30;", 0: "background-color: #666660;"}
        self.on_or_off = {1: 0, 2: 0, 3: 0, 4: 0}
        self.dic = {1: ["Light", self.lightButton, "الاضاءة"], 2: ["Bidet", self.bidetButton, "الشطافة"],
                    3: ["Cover", self.coverButton, "الغطاء"],
                    4: ["Flush", self.flushButton, "السيفون"], 5: ["Home", self.homeButton, "المنزل"]}

        self.img_styles = {1: "border-image: url(imgs/light-bulb.png);", 2: "border-image: url(imgs/toilet (1).png);",
                           3: "border-image: url(imgs/toilet cover.png);", 4: "border-image: url(imgs/flush.png);",
                           5: "border-image: url(imgs/home.png);"}
        self.howtocontrol = {0:"  Bath Room\n  Light: ..\n  bidet: .-\n  cover: -. \n  Flush: --\n Home: ...",1:"  Bath Room\n  select: ..",2:"  Bath Room\n  select: jaw clench",3:"  Bath Room\n  select: jaw clench"}
        self.common_style = "border-radius: 90px; border: 10px solid red; background-repeat: no-repeat; "
        self.message_label.setStyleSheet(self.common_style + "background-color: #fffff0;")
        self.info_label.setStyleSheet(self.common_style + "background-color: #fffff0;")

        self.lightButton.setStyleSheet(self.common_style + self.img_styles[1]+ self.on_off_background[self.on_or_off[1]])
        self.bidetButton.setStyleSheet(self.common_style + self.img_styles[2]+ self.on_off_background[self.on_or_off[2]])
        self.coverButton.setStyleSheet(self.common_style + self.img_styles[3]+ self.on_off_background[self.on_or_off[3]])
        self.flushButton.setStyleSheet(self.common_style + self.img_styles[4]+ self.on_off_background[self.on_or_off[4]])
        self.homeButton.setStyleSheet(self.common_style + self.img_styles[5])



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
    bath = BathRoom()
    bath.show()
    sys.exit(app.exec_())