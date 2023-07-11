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
    selected_item_code_msg = pyqtSignal(int)
    #fin = pyqtSignal()

    mouse_interrupt_msg =  pyqtSignal(int)

    type_of_blink_msg = pyqtSignal(str)

    morse_statment_msg = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.intr_val = [0,0]
        self.mouse_interrupt_msg.connect(self.setIntr)

# github try
    def readInputedSeq(self, windowLength=10):
        global home_seq
        seq = ""
        for i in range(25):

            if self.intr_val[0]:
                return -1

            time.sleep(1)

            if i == 10:
                seq += "4"
                self.type_of_blink_msg.emit("type 4")

            elif i == 20:
                seq += "4"
                self.type_of_blink_msg.emit("type 4")

        try:
            return home_seq[seq]

        except:
            self.type_of_blink_msg.emit("Error: Unknown sequence is entered, Try again!!!! ")
            return 0

    def morse(self):
        BlinkMorseCode = ""


        for i in range(3):
            # time.sleep(3)
            if i == 0:
                morseBlinkLength = 0.1
            elif i == 1:
                morseBlinkLength = 0.4
            else:
                morseBlinkLength = 0.7

            self.type_of_blink_msg.emit("")


            # if end signal is sent break from this loop
            #morseBlinkLength = getMorseData()
            # rdata, ldata = filter_dataFreq(eegData)

            if self.intr_val[0]:
                self.selected_item_code_msg.emit(self.intr_val[1])
                #self.type_of_blink_msg.emit("")
                self.intr_val = [0, 0]
                break

            if morseBlinkLength > 0.6:
                #letter = decodeMorse(BlinkMorseCode)
                letter = None
                if letter == 'save':
                    self.selected_item_code_msg.emit(5)
                    #self.type_of_blink_msg.emit("")
                elif letter == 'clr':
                    self.selected_item_code_msg.emit(1)
                elif letter != None:
                    self.morse_statment_msg.emit(letter)
                    self.selected_item_code_msg.emit(2)
                    #self.type_of_blink_msg.emit("")
                    print("after emitting letter")
                else:
                    #self.type_of_blink_msg.emit("Error: Unknown sequence is entered, Try again!!!! ")
                    self.selected_item_code_msg.emit(3)

                break

            else:
                if 0.2 > morseBlinkLength >= 0:
                    BlinkMorseCode = BlinkMorseCode + '.'
                    self.type_of_blink_msg.emit(BlinkMorseCode)

                elif 0.6 > morseBlinkLength > 0.2:
                    BlinkMorseCode = BlinkMorseCode + '-'
                    self.type_of_blink_msg.emit(BlinkMorseCode)




    def choose(self):
        print("in choose!!!!!!!")

        if CntWorker.morse_falg:
            self.morse()
        else:
            code = self.readInputedSeq()

            while code == 0:
                # loop for taking input
                code = self.readInputedSeq()

            self.type_of_blink_msg.emit("")

            if code != -1:
                # if no button is clicked:
                self.selected_item_code_msg.emit(code)
                print("sig is emitted")
                time.sleep(2)

            else:
                # if button is clicked:
                print("button clicked")
                self.selected_item_code_msg.emit(self.intr_val[1])
                self.intr_val = [0, 0]



        #self.fin.emit()


    def setIntr(self, val):
        self.intr_val = [1, val]


