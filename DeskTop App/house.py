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
        self.img_styles = {1: "border-image: url(imgs/living.jpeg);", 2: "border-image: url(imgs/room1.jpeg);",
                           3: "border-image: url(imgs/room.jpeg);", 4: "border-image: url(imgs/kit.jpeg);",
                           5: "border-image: url(imgs/lobby.jpeg);", 6: "border-image: url(imgs/to.jpg);"}

        self.selected = 0
        self.setStyleSheet("background-color: #122222; ")
        self.dic = {1: ["Living", self.livingButton, "غرفة المعيشة"], 2: ["Room 1", self.room1_Button, "الغرفة الأولى"],
                    3: ["Room 2", self.room2_Button,"الغرفة الثانية"], 4: ["Kitchen", self.kitchenButton, "المطبخ"],
                    5: ["Corridor", self.lobbyButton, "الممر"], 6: ["Toilet", self.bathButton, "دوره المياه"],
                    7: ["Message", None, "الرسالة"]}

        self.common_style = "background-color: #fffff0; border-radius: 90px; border-color: white; background-repeat: no-repeat; "
        self.message_label.setStyleSheet(
            "background-color: #fffff0; border-radius: 30px; border-color: white; background-repeat: no-repeat; ")
        self.info_label.setStyleSheet(
            "background-color: #fffff0; border-radius: 30px; border-color: white; background-repeat: no-repeat;")
        self.exitButton.setStyleSheet("background-color: #ff0000; border-radius: 30px; border-color: white;")
        self.livingButton.setStyleSheet(self.common_style + "border-image: url(imgs/living.jpeg);")
        self.room1_Button.setStyleSheet(self.common_style + "border-image: url(imgs/room1.jpeg);")
        self.room2_Button.setStyleSheet(self.common_style + "border-image: url(imgs/room.jpeg);")
        self.kitchenButton.setStyleSheet(self.common_style + "border-image: url(imgs/kit.jpeg);")
        self.lobbyButton.setStyleSheet(self.common_style + "border-image: url(imgs/lobby.jpeg);")
        self.bathButton.setStyleSheet(self.common_style + "border-image: url(imgs/to.jpg);")



    def select(self, item_no):
        print("in rooom select")

        new_style = "background-color: #fffff0; border-radius: 90px; border: 10px solid green; background-repeat: no-repeat; "
        if self.selected != 0:
            self.reset_selection()

        self.dic[item_no][1].setStyleSheet(new_style)
        if m.CntWorker.isArabic:
            self.dic[item_no][1].setText(self.dic[item_no][2])
        else:
            self.dic[item_no][1].setText(self.dic[item_no][0])
        self.selected = item_no

    def reset_selection(self):
        if self.selected < 7:
            self.dic[self.selected][1].setStyleSheet(self.common_style + self.img_styles[self.selected])
            self.dic[self.selected][1].setText("")


    def closeHome(self):
        self.close()

    def show_state(self, msg):
        self.message_label.setText(msg)
    
    def show_control_state(self, msg):
        self.info_label.setText(msg)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    home = Home()
    home.show()
    sys.exit(app.exec_())
