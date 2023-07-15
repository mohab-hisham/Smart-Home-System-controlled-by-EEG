from PyQt5 import QtWidgets as qtw
from PyQt5 import uic, QtCore
from PyQt5.QtGui import QPixmap
import sys
import main as m
class Room(qtw.QWidget):
    def __init__(self, name):
        super().__init__()
        #bath = "DeskTop App/"
        uic.loadUi("UIs/l2.ui", self)
        self.selected = 0
        self.on_or_off = {1: 0, 2: 0, 3: 0, 4: 0}
        self.on_off_background = {1: "background-color: #ffff30;", 0: "background-color: #666660;"}
        self.dic = {1: ["Light", self.lightButton, "الاضاءة"], 2: ["Curtains", self.cartensButton,"الستائر"], 3: ["TV", self.tvButton,"التلفزيون"],
                    4: ["Fan", self.fanButton,"البوتجاز"], 5: ["Home", self.homeButton,"المنزل"]}

        self.img_styles = {1:"border-image: url(imgs/light-bulb.png);", 2: "border-image: url(imgs/curtains.png);",
                           3: "border-image: url(imgs/smart-tv.png);", 4:"border-image: url(imgs/fan.png);",
                           5:"border-image: url(imgs/home.png);"}
        self.howtocontrol = {0:f"  {name}\n  Light: ..\n  curtains: .-\n  TV: -. \n  Fan: --\n  Home: ...",1:f"  {name}\n  select: ..",2:f"  {name}\n  select: jaw clench",3:f"  {name}\n  select: jaw clench"}
        self.message_label.setText(name)
        self.setStyleSheet("background-color: #122222; ")

    #border-color: white;
        self.common_style = "border-radius: 90px; border: 10px solid red; background-repeat: no-repeat; "
        self.message_label.setStyleSheet(self.common_style+"background-color: #fffff0;")
        self.info_label.setStyleSheet(self.common_style+"background-color: #fffff0;")

        self.homeButton.setStyleSheet(self.common_style + self.img_styles[5])
        self.fanButton.setStyleSheet(self.common_style + self.img_styles[4]+ self.on_off_background[self.on_or_off[4]])
        self.tvButton.setStyleSheet(self.common_style + self.img_styles[3]+ self.on_off_background[self.on_or_off[3]])
        self.cartensButton.setStyleSheet(self.common_style + self.img_styles[2]+ self.on_off_background[self.on_or_off[2]])
        self.lightButton.setStyleSheet(self.common_style + self.img_styles[1]+ self.on_off_background[self.on_or_off[1]])
        


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
            print("in reset_selection")
            self.dic[self.selected][1].setStyleSheet(self.common_style + self.img_styles[self.selected]
                                                     + self.on_off_background[self.on_or_off[self.selected]])
        else:
            self.dic[self.selected][1].setStyleSheet(self.common_style + self.img_styles[self.selected])
        self.dic[self.selected][1].setText("")






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