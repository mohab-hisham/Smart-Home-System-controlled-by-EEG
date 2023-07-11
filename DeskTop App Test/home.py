import time

from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import room, bathroom, kitchen, corridor, calibration, controls, message, fall, house
import sys
import main as m
from PyQt5.QtCore import *


class Smarthome(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("UIs/test.ui", self)
        self.menubar.setStyleSheet("background-color: #fffff0; border-radius: 10px; border-color: white; ")

        self.setStyleSheet("background-color: #122222; ")


        self.house = house.Home()
        self.room1 = room.Room("Room 1")
        self.room2 = room.Room("Room 2")
        self.living = room.Room("Living Room")
        self.bath = bathroom.BathRoom()
        self.kitchen = kitchen.Kitchen()
        self.corridor = corridor.Corridor()

        self.calib = calibration.Calibration()
        self.control = controls.Controls()
        self.msg = message.Message()
        self.fall = fall.Fall()

        #self.morse_flag = 0
        self.room_dic = {0: self.house, 1: self.living, 2: self.room1, 3: self.room2,
               4: self.kitchen, 5: self.corridor, 6: self.bath, 7: self.calib,
               8: self.control, 9: self.msg, 10: self.fall}

        self.testLayout.addWidget(self.house)
        self.current_widget = 0

        self.kitchen.lightButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(1))
        self.kitchen.stoveButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(2))
        self.kitchen.washerButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(3))
        self.kitchen.chimneyButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(4))
        self.kitchen.homeButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(5))

        self.living.lightButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(1))
        self.living.cartensButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(2))
        self.living.tvButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(3))
        #self.living.fanButton.clicked.connect(lambda: self.living.select(4))
        self.living.fanButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(4))
        self.living.homeButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(5))

        self.room1.lightButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(1))
        self.room1.cartensButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(2))
        self.room1.tvButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(3))
        self.room1.fanButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(4))
        self.room1.homeButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(5))

        self.room2.lightButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(1))
        self.room2.cartensButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(2))
        self.room2.tvButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(3))
        self.room2.fanButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(4))
        self.room2.homeButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(5))

        self.corridor.lightButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(1))
        self.corridor.door1Button.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(2))
        self.corridor.door2Button.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(3))
        self.corridor.toiletButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(4))
        self.corridor.homeButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(5))

        self.bath.lightButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(1))
        self.bath.bidetButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(2))
        self.bath.coverButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(3))
        self.bath.flushButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(4))
        self.bath.homeButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(5))

        self.calib.submitButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(5))

        self.control.doneButton.clicked.connect(self.get_control_mode)
        self.control.doneButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(5))

        self.msg.saveButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(5))
        self.msg.clearButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(1))

        self.fall.backButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(5))

        self.house.exitButton.clicked.connect(self.close)


        self.cnt_thr = QThread()
        self.cnt_worker = m.CntWorker()
        self.cnt_worker.moveToThread(self.cnt_thr)
        self.cnt_thr.started.connect(self.cnt_worker.choose)
        self.cnt_worker.selected_item_code_msg.connect(self.change)
        self.cnt_worker.left_right_msg.connect(self.left_right)
        self.cnt_thr.finished.connect(self.cnt_thr.start)

        self.house.livingButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(1))
        self.house.room1_Button.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(2))
        self.house.room2_Button.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(3))
        self.house.kitchenButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(4))
        self.house.lobbyButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(5))
        self.house.bathButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(6))
        self.actionCalibration.triggered.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(7))
        self.actionControls.triggered.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(8))
        self.actionMessage.triggered.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(9))
        self.actionFall_Detection.triggered.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(10))

        self.cnt_worker.type_of_blink_msg.connect(self.kitchen.show_state)
        self.cnt_worker.type_of_blink_msg.connect(self.house.show_state)
        self.cnt_worker.type_of_blink_msg.connect(self.corridor.show_state)
        self.cnt_worker.type_of_blink_msg.connect(self.bath.show_state)
        self.cnt_worker.type_of_blink_msg.connect(self.room1.show_state)
        self.cnt_worker.type_of_blink_msg.connect(self.room2.show_state)
        self.cnt_worker.type_of_blink_msg.connect(self.living.show_state)

        self.cnt_worker.morse_statment_msg.connect(self.msg.write_pragraph)
        self.cnt_worker.type_of_blink_msg.connect(self.msg.show_code)

        self.showFullScreen()

    def get_control_mode(self):
        m.CntWorker.control_mode = self.control.get_control_option()
        if m.CntWorker.control_mode:
            self.house.select(1)
            #self.house.message_label.setText("Living is selected.")
            print("new done!!")
        elif self.house.selected != 0:
            self.house.reset_selection()
            self.house.selected = 0


    def change(self, widget_no):
        print("in sequence")
        # if I am in main menue to select rooms:
        if self.current_widget == 0:
            print("in first if")
            self.house.close()
            self.testLayout.addWidget(self.room_dic[widget_no])
            self.current_widget = widget_no
            self.room_dic[self.current_widget].show()

            # if morse is selected:
            if widget_no == 9:
                m.CntWorker.morse_falg = 1

            # select first item if in left right mode
            if m.CntWorker.control_mode:
                try: # because widgets in menue bar has no selection.
                    self.room_dic[self.current_widget].select(1)
                except:
                    pass


        # if any button other than 'return to home' button is selected:
        elif widget_no != 5:
            if m.CntWorker.morse_falg:
                if widget_no == 1 :
                    self.msg.paragraph = ""
                    self.msg.write_pragraph("")
                elif widget_no == 3:
                    self.msg.show_code("Error: Unknown sequence is entered, Try again!!!! ")
                else:
                    pass
            else:
                self.room_dic[self.current_widget].message_label.setText(f"{widget_no} is turned on !!" )
                self.room_dic[self.current_widget].select(widget_no)
                print("in second if")
                print("any button is clicked")

        # if 'return to home button' is selected:
        else:
            if m.CntWorker.morse_falg:
                self.msg.paragraph = ""
                self.msg.write_pragraph("")
                #self.msg.show_code("")
                m.CntWorker.morse_falg = 0

            print("in third if")
            try:
                self.room_dic[self.current_widget].select(widget_no)
            except:
                print("in pass")
                pass
            self.room_dic[self.current_widget].close()
            self.house.show()
            if m.CntWorker.control_mode:
                try:
                    self.room_dic[self.current_widget].reset_selection()
                    self.room_dic[self.current_widget].selected = 0
                except:
                    pass
                self.house.message_label.setText("Living is selected.")
            self.current_widget = 0


        self.cnt_thr.quit()

    def left_right(self, left_right_state):

        print("in left right")
        print(f"{left_right_state} is needed")
        if self.current_widget != 0 or left_right_state != 0:
            selected_item = self.room_dic[self.current_widget].selected + left_right_state

            if selected_item > list(self.room_dic[self.current_widget].dic)[-1]:
                selected_item = list(self.room_dic[self.current_widget].dic)[0]
            elif selected_item < list(self.room_dic[self.current_widget].dic)[0]:
                selected_item = list(self.room_dic[self.current_widget].dic)[-1]

            self.room_dic[self.current_widget].select(selected_item)
            self.room_dic[self.current_widget].message_label.setText(f"{selected_item} is selected.")

            if left_right_state == 0:
                if selected_item == 5:
                    # if user wants to go home:
                    self.cnt_worker.mouse_interrupt_msg.emit(5)
                else:
                    # if user wants to turn a devices without returning to home menue:
                    self.room_dic[self.current_widget].message_label.setText(f"{selected_item} is turned on !!")


        else:
            print("in elseeeeeee")
            self.house.close()
            self.testLayout.addWidget(self.room_dic[self.house.selected])
            self.current_widget = self.house.selected
            self.house.selected = 0
            self.room_dic[self.current_widget].show()
            self.room_dic[self.current_widget].select(1)



        self.cnt_thr.quit()







if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    #startMUSEconnection()
    home = Smarthome()
    home.cnt_thr.start()
    #home.open()

    sys.exit(app.exec_())



