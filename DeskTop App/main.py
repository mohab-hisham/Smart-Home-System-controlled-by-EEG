import time
from PyQt5.QtCore import *

import numpy as np  # Module that simplifies computations on matrices
import matplotlib.pyplot as plt  # Module used for plotting


import time

import threading
import asyncio
# import variables
from types import SimpleNamespace

from Utils import collectEEGsignal,readFullinputedSeq,MUSEns,EEGns, EEGutils
global home_seq
# home_seq= {[1, 1]: 1, [1, 3]: 2, [1, 5]: 3, [1, 7]: 4, [1, 9]: 5, [4, 2]: 6,
#            [4, 4]: 7, [4, 6]: 8, [4, 8]: 9, [6, 3]: 10}

home_seq = {"11":1,"13":2,"15":3,"17":4,"19":5,"42":6,"44":7,"46":8,"48":9,"63":10}
# ns = SimpleNamespace()

# Handy little enum to make code more readable

class CntWorker(QObject):
    eeg_cnt = pyqtSignal(int)
    fin = pyqtSignal()

    mouse_int =  pyqtSignal(int)

    eye_state = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.intr_val = [0,0]
        self.mouse_int.connect(self.setIntr)

    def readInputedSeq(self, windowLength=10):
        # global home_seq
        # inputSeqArr = []
        # openTime = 0
        # closeTime = 0
        # firstClose = 1
        # openCloseState = 0
        # openCloseTime = 0
        # closeOpenTime = 0

        while True:

            if self.intr_val[0]:
                return -1

            eeg_data, timestamp = MUSEns.EEGinlet.pull_chunk(
                timeout=0.5, max_samples=int(10))
            
            outSeqValue = EEGutils.readFullinputedSeq(ns = self,EEGData=eeg_data)

            if outSeqValue != 0:
                return outSeqValue
            # rightData, leftData = EEGutils.filter_dataFreq(eeg_data, wind_len=windowLength)

            # if (min(rightData) < EEGns.lowerTH) and (min(leftData) < EEGns.lowerTH) and openCloseState == 0:  # close

            #     openCloseState = 1
            #     if firstClose == 1:
            #         closeTime = time.time()
            #         firstClose = 0
            #     else:
            #         closeTime = time.time()
            #         openCloseTime = closeTime - openTime
            #         if openCloseTime < 0.3:
            #             self.eye_state.emit("Short Relaxation Time")
            #         elif openCloseTime < 0.62:
            #             self.eye_state.emit("Medium Relaxation Time")
            #         else:
            #             self.eye_state.emit("Long Relaxation Time")

            #         inputSeqArr[-1].durationAfterBlink = [openCloseTime]
            #         if len(inputSeqArr) == 2:
            #             break

            # elif (300 > max(rightData) > EEGns.upperTH) and (
            #         300 > max(leftData) > EEGns.upperTH) and openCloseState == 1:  # open
            #     openCloseState = 0
            #     openTime = time.time()
            #     closeOpenTime = openTime - closeTime
            #     if closeOpenTime < 0.3:
            #         self.eye_state.emit("Short Blink Time")
            #     elif closeOpenTime < 0.62:
            #         self.eye_state.emit("Medium Blink Time")
            #     else:
            #         self.eye_state.emit("Long Blink Time")
            #     inputSeqArr.append(EEGutils.Blink(length=[closeOpenTime]))

        # try:
            
        #     seq = str(inputSeqArr[0].classify())+ str(inputSeqArr[1].classify())
        #     print(seq)
        #     return home_seq[seq]
        # except:
        #     self.eye_state.emit("Error: Unknown sequence is entered, Try again!!!! ")
        #     return 0




    def choose(self):
        # time.sleep(5)
        print("started")
        code = self.readInputedSeq()

        # while code == 0:
        #     code = self.readInputedSeq()

        if code != -1:
            self.eeg_cnt.emit(code)
            print("sig is emitted")
            time.sleep(2)

        else:
            self.eeg_cnt.emit(self.intr_val[1])
            self.intr_val = [0, 0]

        self.fin.emit()

        print("fin is emitted")

    def setIntr(self, val):
        self.intr_val = [1, val]


class EEG_Worker(QObject):
    eeg_sig = pyqtSignal()
    str_sig = pyqtSignal(str)
    m_letter = pyqtSignal(str)
    fin = pyqtSignal()
    cnt_return = pyqtSignal()

    intr = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.intr_val = 0
        self.intr.connect(lambda: self.setIntr(1))

    def navigate(self):
        # time.sleep(5)
        self.eeg_sig.emit()
        time.sleep(5)
        self.cnt_return.emit()
        self.fin.emit()

    def morse(self):
        # BlinkMorseCode = ""
        # paragraph = ""

        self.eeg_sig.emit()
        EEGutils.readMorseCode(self)
        # while True:
        #     # if end signal is sent break from this loop
        #     morseBlinkLength = EEGutils.getMorseData()
        #     # rdata, ldata = filter_dataFreq(eegData)

        #     if self.intr_val:
        #         self.intr_val = 0
        #         break

        #     if morseBlinkLength > 0.6:
        #         letter = EEGutils.decodeMorse(BlinkMorseCode)
        #         if letter == 'save':
        #             self.str_sig.emit("")
        #             self.m_letter.emit("")
        #             break
        #         elif letter == 'clr':
        #             paragraph = ""
        #         elif letter != None:
        #             paragraph += letter

        #         self.str_sig.emit(paragraph)
        #         BlinkMorseCode = ""
        #         self.m_letter.emit(BlinkMorseCode)
        #     else:
        #             if 0.2 > morseBlinkLength >= 0:
        #                 BlinkMorseCode = BlinkMorseCode + '.'
        #                 self.m_letter.emit(BlinkMorseCode)

        #             elif 0.6 > morseBlinkLength > 0.2:
        #                 BlinkMorseCode = BlinkMorseCode + '-'
        #                 self.m_letter.emit(BlinkMorseCode)

        self.fin.emit()
        self.cnt_return.emit()

    def setIntr(self, val):
        self.intr_val = val


