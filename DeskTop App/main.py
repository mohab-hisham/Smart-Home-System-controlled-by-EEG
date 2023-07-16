import time
from PyQt5.QtCore import *

import numpy as np  # Module that simplifies computations on matrices
import matplotlib.pyplot as plt  # Module used for plotting

from PyQt5 import QtWidgets as qtw
import sys

import time
#from Utils.EEGutils import getMorseData, decodeMorse
import threading
import asyncio
# import variables
from types import SimpleNamespace
from Utils.EEGutils import readMorseCode, readInputedSeq,EEGns


#from Utils import collectEEGsignal,readFullinputedSeq,MUSEns,EEGns, EEGutils
global home_seq, calib_seq, all_cnt_sig, rooms

# Mapping between sequence and its corresponding room number in home tab.
home_seq = {"11": 1, "13": 2, "15": 3, "17": 4, "19": 5, "42": 6, "44": 7, "46": 8, "48": 9, "63": 10}

# Three different sequences for calibration submit button.
calib_seq = {"12": 1, "21": 1, "32": 1}

# Mapping between room number concatenated with item number and corresponding control code
all_cnt_sig = {"11": 1, "12": 2, "13": 3, "14": 4, "21": 5, "22": 6, "23": 7, "24": 8, "31": 9, "32": 10, "33": 11,
               "34": 12, "41": 13, "42": 14, "43": 15, "44": 16, "51": 17, "52": 18, "53": 19, "54": 20, "61": 21,
               "62": 22, "63": 23, "64": 24}

# Mapping between each room item and its corresponding sequence.
rooms ={1: {"91": 1, "93": 2, "15": 3, "17": 4, "29": 5}, 2: {"41": 1, "43": 2, "45": 3, "47": 4, "49": 5},
        3: {"81": 1, "83": 2, "85": 3, "87": 4, "89": 5}, 4: {"82": 1, "84": 2, "86": 3, "17": 4, "88": 5},
        5: {"71": 1, "73": 2, "55": 3, "57": 4, "59": 5}, 6: {"51": 1, "53": 2, "75": 3, "67": 4, "69": 5}}

ns = SimpleNamespace()

# Handy little enum to make code more readable

class CntWorker(QObject):
    morse_falg =0
    control_mode = 0
    isArabic = 1

    selected_item_code_msg = pyqtSignal(int)
    #fin = pyqtSignal()

    mouse_interrupt_msg =  pyqtSignal(int)

    left_right_msg = pyqtSignal(int)

    gyro_msg = pyqtSignal(int)

    type_of_blink_msg = pyqtSignal(str)

    system_action_msg = pyqtSignal(str)

    morse_statment_msg = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.intr_val = [0,0]
        self.mouse_interrupt_msg.connect(self.setIntr)




    def choose(self):
        
        print("in choose!!!!!!!")

        if CntWorker.morse_falg:
            readMorseCode(self)
        else:
            code = readInputedSeq(self,windowLength=10,controlMethod=CntWorker.control_mode)

            # while code == 0:
            #     # loop for taking input
            #     code = self.readInputedSeq()
            self.type_of_blink_msg.emit("")
            if code != -1:

                # self.left_right_msg.emit(code-2)
                # self.left_right_msg.emit(-2)
                # self.selected_item_code_msg.emit(code)
                if CntWorker.control_mode == 1 or CntWorker.control_mode == 3:
                    self.left_right_msg.emit(code-2)
                else:
                # if no button is clicked:
                    self.selected_item_code_msg.emit(code)
                print("sig is emitted")
                # time.sleep(2)

            else:
                # if button is clicked:
                print("button clicked")
                self.selected_item_code_msg.emit(self.intr_val[1])
                self.intr_val = [0, 0]

        # self.type_of_blink_msg.emit("")

        #self.fin.emit()


    def setIntr(self, val):
        self.intr_val = [1, val]


