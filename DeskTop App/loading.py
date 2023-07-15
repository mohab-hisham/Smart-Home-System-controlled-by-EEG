from PyQt5 import QtWidgets as qtw
from PyQt5 import uic, QtCore
from PyQt5.QtGui import QPixmap
import sys
import main as m
from home import Smarthome
import time
from PyQt5.QtCore import *
from Utils.MQTTutils import startMQTTserver,MQTTns
from Utils.EEGutils import TFModelInit
from Utils.MUSEutils import startMUSEconnection,MUSEns
#import server
#import connection

class Loading(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #bath = "DeskTop App/"
        uic.loadUi("UIs/loading.ui", self)
        self.steps = 4
        self.info_label.setStyleSheet("color : white;")
        #self.progressBar.setvalue(1)
        #self.progressBar.setvalue(2)
        self.setStyleSheet("background-color: #122222; ")
        self.progressBar.setStyleSheet("border-radius: 1px; border-color: white;")
        self.welcome_label.setStyleSheet("background-color: #fffff0; border-radius: 50px;border: 10px solid orange; ")
        self.home = Smarthome()

        self.info_label.setText("Connecting to the Server.")

        self.server = QThread()
        self.server.started.connect(self.loop_server)
        #self.server_thr.server_sig.connect(self.update_progress)
        #self.cnt_thr.finished.connect(self.cnt_thr.start)

        self.device_thr = QThread()
        
        self.server.finished.connect(self.device_thr.start)

        self.device_thr.started.connect(self.loop_device)

        self.device_thr.finished.connect(self.home.cnt_thr.start)

        self.showFullScreen()


    # def update_progress(self, val):
    #     self.progressBar.setValue(val[0])
    #     self.info_label.setText(val[1])
    #     if val[0] == 3:
    #         time.sleep(1)
    #         self.server_worker.home_start_sig.emit()

    def loop_server(self):
        # startMUSEconnection()
        print("in server connect")
        time.sleep(3)
        self.info_label.setText("Connecting to Server.")
        startMQTTserver()
        while not MQTTns.didPrintSubscribeMessage:
            continue
        #progress setvalue
        self.progressBar.setValue(1)
        self.info_label.setText("Connected successfully!!")
        time.sleep(2)
        self.info_label.setText("Connecting to Device.")
        # finish thread
        self.server.quit()

    def loop_device(self):
        print("in device connect")
        # time.sleep(3)
        startMUSEconnection()
        TFModelInit()
        self.info_label.setText("Connected successfully!!")
        self.progressBar.setValue(2)
        while MUSEns.continueFlag == 0:
            continue
        time.sleep(2)
        self.info_label.setText("Checking signal Quality...")
        time.sleep(6)
        self.progressBar.setValue(3)
        self.info_label.setText("Good Signal Quality!!")
        time.sleep(2)
        self.info_label.setText("Opening My Smart Home.")
        print("progress 3")
        time.sleep(3)
        # time.sleep(1)
        self.progressBar.setValue(4)
        print("progress 4")
        # currentTime = time.time()
        # while (time.time() - currentTime) < 5:
        #     continue
        # currentTime = time.time()
        # while (time.time() - currentTime) < 5:
        #     continue
        time.sleep(3)
        self.close()
        # time.sleep(1)
        # while (time.time() - currentTime) < 3:
        #     continue
        self.home.showFullScreen()
        self.device_thr.quit()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    start= Loading()
    #start.showFullScreen()
    start.server.start()
    #start.device_thr.start()
    sys.exit(app.exec_())