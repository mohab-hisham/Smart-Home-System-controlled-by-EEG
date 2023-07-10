from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import room, bathroom, kitchen, corridor, calibration, controls, message, fall
import sys
import main as m
from PyQt5.QtCore import *
#from Utils import startMUSEconnection, calibrate, CheckSignalQuality,MUSEns


class Smarthome(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        #self.interrupt = [0, 0]
        self.cnt_thr = QThread()
        self.cnt_worker = m.CntWorker()
        self.cnt_worker.moveToThread(self.cnt_thr)
        self.cnt_thr.started.connect(self.show)
        self.cnt_thr.started.connect(self.cnt_worker.choose)
        self.cnt_worker.selected_item_code_msg.connect(self.control)
        self.cnt_worker.type_of_blink_msg.connect(self.show_state)
        self.cnt_worker.fin.connect(self.cnt_thr.quit)
        bath = ""
        uic.loadUi(bath + "UIs/h1.ui", self)

        self.setStyleSheet("background-color: #122222; ")
        self.showFullScreen()

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

        self.exitButton.clicked.connect(self.exit)


        self.room1 = room.Room()
        self.room2 = room.Room()
        self.living = room.Room()
        self.bath = bathroom.BathRoom()
        self.kitchen = kitchen.Kitchen()
        self.corridor = corridor.Corridor()

        self.room1.homeButton.clicked.connect(self.returnHome)
        self.room2.homeButton.clicked.connect(self.returnHome)
        self.living.homeButton.clicked.connect(self.returnHome)
        #self.room1_Button.clicked.connect(lambda: self.room1.open("Room 1"))
        #self.room1_Button.clicked.connect(self.close)
        #self.room2_Button.clicked.connect(lambda: self.room2.open("Room 2"))
        #self.room2_Button.clicked.connect(self.close)
        #self.livingButton.clicked.connect(lambda: self.living.open("Living Room"))
        #self.livingButton.clicked.connect(self.close)
        #self.bathButton.clicked.connect(self.openBath)
        self.bath.homeButton.clicked.connect(self.returnHome)
        self.kitchen.homeButton.clicked.connect(self.returnHome)
        #self.kitchenButton.clicked.connect(self.openKitchen)
        self.corridor.homeButton.clicked.connect(self.returnHome)
        #self.lobbyButton.clicked.connect(self.openCorridor)

        self.living_thr = QThread()
        self.living_worker = m.EEG_Worker()
        self.living_worker.moveToThread(self.living_thr)
        self.living_thr.started.connect(lambda :self.living_worker.navigate(1))
        self.living_worker.start_sig.connect(lambda: self.living.open("Living Room"))
        self.living_worker.start_sig.connect(self.close)
        self.living_worker.eye_state.connect(self.living.show_state)
        self.living_worker.cnt_sig.connect(self.living.cnt_feedback)
        self.living_worker.fin.connect(self.living.close)
        self.living_worker.cnt_return.connect(self.cnt_thr.start)
        self.living_worker.fin.connect(self.living_thr.quit)

        self.room1_thr = QThread()
        self.room1_worker = m.EEG_Worker()
        self.room1_worker.moveToThread(self.room1_thr)
        self.room1_thr.started.connect(lambda :self.room1_worker.navigate(2))
        self.room1_worker.start_sig.connect(lambda: self.room1.open("Room 1"))
        self.room1_worker.start_sig.connect(self.close)
        self.room1_worker.eye_state.connect(self.room1.show_state)
        self.room1_worker.cnt_sig.connect(self.room1.cnt_feedback)
        self.room1_worker.fin.connect(self.room1.close)
        self.room1_worker.cnt_return.connect(self.cnt_thr.start)
        self.room1_worker.fin.connect(self.room1_thr.quit)

        self.room2_thr = QThread()
        self.room2_worker = m.EEG_Worker()
        self.room2_worker.moveToThread(self.room2_thr)
        self.room2_thr.started.connect(lambda: self.room2_worker.navigate(3))
        self.room2_worker.start_sig.connect(lambda: self.room2.open("Room 2"))
        self.room2_worker.start_sig.connect(self.close)
        self.room2_worker.eye_state.connect(self.room2.show_state)
        self.room2_worker.cnt_sig.connect(self.room2.cnt_feedback)
        self.room2_worker.fin.connect(self.room2.close)
        self.room2_worker.cnt_return.connect(self.cnt_thr.start)
        self.room2_worker.fin.connect(self.room2_thr.quit)

        self.corridor_thr = QThread()
        self.corridor_worker = m.EEG_Worker()
        self.corridor_worker.moveToThread(self.corridor_thr)
        self.corridor_thr.started.connect(lambda: self.corridor_worker.navigate(5))
        self.corridor_worker.start_sig.connect(self.openCorridor)
        self.corridor_worker.eye_state.connect(self.corridor.show_state)
        self.corridor_worker.cnt_sig.connect(self.corridor.cnt_feedback)
        self.corridor_worker.fin.connect(self.corridor.close)
        self.corridor_worker.cnt_return.connect(self.cnt_thr.start)
        self.corridor_worker.fin.connect(self.corridor_thr.quit)

        self.kitchen.kitchen_worker.cnt_return.connect(self.cnt_thr.start)

        self.bath_thr = QThread()
        self.bath_worker = m.EEG_Worker()
        self.bath_worker.moveToThread(self.bath_thr)
        self.bath_thr.started.connect(lambda: self.bath_worker.navigate(6))
        self.bath_worker.start_sig.connect(self.openBath)
        self.bath_worker.eye_state.connect(self.bath.show_state)
        self.bath_worker.cnt_sig.connect(self.bath.cnt_feedback)
        self.bath_worker.fin.connect(self.bath.close)
        self.bath_worker.cnt_return.connect(self.cnt_thr.start)
        self.bath_worker.fin.connect(self.bath_thr.quit)



        #############################################################################################
        self.calib = calibration.Calibration()
        self.control = controls.Controls()
        self.msg = message.Message()
        self.fall = fall.Fall()
        #self.actionCalibration_2.triggered.connect(self.openCalibration)
        #self.actionControls.triggered.connect(self.openControls)
        #self.actionMessage.triggered.connect(self.openMessage)


        #self.actionFall_Detection.triggered.connect(self.openFall)

        self.calib.submitButton.clicked.connect(self.returnHome)
        self.control.doneButton.clicked.connect(self.returnHome)
        self.msg.saveButton.clicked.connect(self.returnHome)
        self.fall.backButton.clicked.connect(self.returnHome)

        self.calib_thr = QThread()
        self.calib_worker = m.EEG_Worker()
        self.calib_worker.moveToThread(self.calib_thr)
        self.calib_thr.started.connect(self.calib_worker.calibrate)
        self.calib_worker.start_sig.connect(self.openCalibration)
        self.calib_worker.fin.connect(self.calib.close)
        self.calib_worker.cnt_return.connect(self.cnt_thr.start)
        self.calib_worker.fin.connect(self.calib_thr.quit)

        self.control_thr = QThread()
        self.control_worker = m.EEG_Worker()
        self.control_worker.moveToThread(self.control_thr)
        self.control_thr.started.connect(self.control_worker.navigate)
        self.control_worker.start_sig.connect(self.openControls)
        self.control_worker.fin.connect(self.control.close)
        self.control_worker.cnt_return.connect(self.cnt_thr.start)
        self.control_worker.fin.connect(self.control_thr.quit)

        self.msg_thr = QThread()
        self.msg_worker = m.EEG_Worker()
        self.msg_worker.moveToThread(self.msg_thr)
        self.msg_thr.started.connect(self.msg_worker.morse)
        self.msg_worker.start_sig.connect(self.openMessage)
        self.msg_worker.str_sig.connect(self.msg.write_pragraph)
        self.msg_worker.m_letter.connect(self.msg.show_code)
        self.msg_worker.fin.connect(self.msg.close)
        self.msg_worker.cnt_return.connect(self.cnt_thr.start)
        self.msg_worker.fin.connect(self.msg_thr.quit)

        self.fall_thr = QThread()
        self.fall_worker = m.EEG_Worker()
        self.fall_worker.moveToThread(self.fall_thr)
        self.fall_thr.started.connect(self.fall_worker.navigate)
        self.fall_worker.start_sig.connect(self.openFall)
        self.fall_worker.fin.connect(self.fall.close)
        self.fall_worker.cnt_return.connect(self.cnt_thr.start)
        self.fall_worker.fin.connect(self.fall_thr.quit)

        self.actionFall_Detection.triggered.connect(lambda:self.cnt_worker.mouse_interrupt_msg.emit(10))

        self.actionMessage.triggered.connect(lambda:self.cnt_worker.mouse_interrupt_msg.emit(9))
        self.msg.saveButton.clicked.connect(self.msg_worker.intr.emit)

        self.actionControls.triggered.connect(lambda:self.cnt_worker.mouse_interrupt_msg.emit(8))

        self.actionCalibration_2.triggered.connect(lambda:self.cnt_worker.mouse_interrupt_msg.emit(7))
        self.calib.submitButton.clicked.connect(self.calib_worker.intr.emit)

        self.bathButton.clicked.connect(lambda:self.cnt_worker.mouse_interrupt_msg.emit(6))

        self.lobbyButton.clicked.connect(lambda:self.cnt_worker.mouse_interrupt_msg.emit(5))

        self.kitchenButton.clicked.connect(lambda:self.cnt_worker.mouse_interrupt_msg.emit(4))

        self.room2_Button.clicked.connect(lambda:self.cnt_worker.mouse_interrupt_msg.emit(3))

        self.room1_Button.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(2))

        self.livingButton.clicked.connect(lambda: self.cnt_worker.mouse_interrupt_msg.emit(1))


        self.living.lightButton.clicked.connect(lambda: self.living_worker.mouse_intr.emit(1))
        self.living.cartensButton.clicked.connect(lambda: self.living_worker.mouse_intr.emit(2))
        self.living.tvButton.clicked.connect(lambda: self.living_worker.mouse_intr.emit(3))
        self.living.fanButton.clicked.connect(lambda: self.living_worker.mouse_intr.emit(4))
        self.living.homeButton.clicked.connect(lambda: self.living_worker.mouse_intr.emit(5))

        self.room1.lightButton.clicked.connect(lambda: self.living_worker.mouse_intr.emit(1))
        self.room1.cartensButton.clicked.connect(lambda: self.living_worker.mouse_intr.emit(2))
        self.room1.tvButton.clicked.connect(lambda: self.living_worker.mouse_intr.emit(3))
        self.room1.fanButton.clicked.connect(lambda: self.living_worker.mouse_intr.emit(4))
        self.room1.homeButton.clicked.connect(lambda: self.living_worker.mouse_intr.emit(5))

        self.room2.lightButton.clicked.connect(lambda: self.living_worker.mouse_intr.emit(1))
        self.room2.cartensButton.clicked.connect(lambda: self.living_worker.mouse_intr.emit(2))
        self.room2.tvButton.clicked.connect(lambda: self.living_worker.mouse_intr.emit(3))
        self.room2.fanButton.clicked.connect(lambda: self.living_worker.mouse_intr.emit(4))
        self.room2.homeButton.clicked.connect(lambda: self.living_worker.mouse_intr.emit(5))



        self.corridor.lightButton.clicked.connect(lambda: self.corridor_worker.mouse_intr.emit(1))
        self.corridor.door1Button.clicked.connect(lambda: self.corridor_worker.mouse_intr.emit(2))
        self.corridor.door2Button.clicked.connect(lambda: self.corridor_worker.mouse_intr.emit(3))
        self.corridor.toiletButton.clicked.connect(lambda: self.corridor_worker.mouse_intr.emit(4))
        self.corridor.homeButton.clicked.connect(lambda: self.corridor_worker.mouse_intr.emit(5))
        #self.corridor.homeButton.clicked.connect(lambda :print("home corridor is clicked!!!!!!"))

        self.bath.lightButton.clicked.connect(lambda: self.bath_worker.mouse_intr.emit(1))
        self.bath.bidetButton.clicked.connect(lambda: self.bath_worker.mouse_intr.emit(2))
        self.bath.coverButton.clicked.connect(lambda: self.bath_worker.mouse_intr.emit(3))
        self.bath.flushButton.clicked.connect(lambda: self.bath_worker.mouse_intr.emit(4))
        self.bath.homeButton.clicked.connect(lambda: self.bath_worker.mouse_intr.emit(5))

        ############################################################################################

        # styles #

        #self.room2.homeButton.clicked.connect(lambda: self.room2_Button.setStyleSheet("background-color: #ffffff; "))
        #self.room2_Button.clicked.connect(lambda: self.room2.message_label.setText("Hiiiiii"))
        #self.room2_Button.clicked.connect(lambda: self.room2.homeButton.setStyleSheet("background-color: #ff91ff; "))
        #self.room2_worker.start_sig.connect(lambda: self.room2.message_label.setText("Hiiiiii"))
        #self.room2_worker.cnt_return.connect(lambda: self.room2_Button.setStyleSheet("background-color: #ffffff; "))

    def control(self, code):
        print("in control")
        dic = {1: self.living_thr, 2: self.room1_thr, 3: self.room2_thr,
               4: self.kitchen.kitchen_thr, 5: self.corridor_thr, 6: self.bath_thr, 7: self.calib_thr,
               8: self.control_thr, 9: self.msg_thr, 10: self.fall_thr}

        display_dic = {1: self.living, 2: self.room1, 3: self.room2,
               4: self.kitchen, 5: self.corridor, 6: self.bath, 7: self.calib,
               8: self.control, 9: self.msg, 10: self.fall}

        self.close()
        display_dic[code].open()
        self.cnt_thr.quit()

        dic[code].start()
        #dic[code].exec()
        print("control started")

    def returnHome(self):
        self.show()

    def openBath(self):
        self.bath.open()
        self.bath.showFullScreen()
        self.close()

    def openKitchen(self):
        print("in open kitchen")
        self.kitchen.open()
        self.close()

    def openCorridor(self):
        self.corridor.open()
        self.close()

    def openCalibration(self):
        self.calib.show()
        self.close()

    def openControls(self):
        self.control.show()
        self.close()

    def openMessage(self):
        self.msg.show()
        self.close()

    def openFall(self):
        self.fall.show()
        self.close()

    def show_state(self, msg):
        self.message_label.setText(msg)

    def exit(self):
        self.close()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    #startMUSEconnection()
    home = Smarthome()
    home.cnt_thr.start()
    sys.exit(app.exec_())


