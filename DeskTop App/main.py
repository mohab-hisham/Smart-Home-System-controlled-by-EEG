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
home_seq= {'living':[1,1], 'room1': [1,3], 'room2': [1,5], 'kitchen': [1,7], 'lobby': [1,9], 'toilet': [4,2],
           'calibration': [4,4], 'control': [4,6], 'message': [4,8], 'fall': [6, 3]}

ns = SimpleNamespace()

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

    def readInputedSeq(self, EEGData, windowLength=10):
        inputSeqArr = []
        openTime = 0
        closeTime = 0
        firstClose = 1
        openCloseState = 0
        openCloseTime = 0
        closeOpenTime = 0
        #global SeqArray
        returnValue = 0

        while 1:
            rightData, leftData = EEGutils.filter_dataFreq(EEGData, wind_len=windowLength)
            if (min(rightData) < EEGns.lowerTH) and (min(leftData) < EEGns.lowerTH) and openCloseState == 0:  # close

                openCloseState = 1
                if firstClose == 1:
                    closeTime = time.time()
                    firstClose = 0
                else:
                    closeTime = time.time()
                    openCloseTime = closeTime - openTime
                    if openCloseTime < 0.3:
                        self.eye_state.emit("Short relaxation time!!")
                    elif openCloseTime < 0.62:
                        self.eye_state.emit("Medium relaxation time!!")
                    else:
                        self.eye_state.emit("long relaxation time!!")
                    # inputSeqArr.append(Blink(openCloseTime,BlinkType="eyeOpen"))
                    # print("added a Blink!")

                    inputSeqArr[-1].durationAfterBlink = [openCloseTime]
                    if len(inputSeqArr) == 2:
                        break
                    #EEGutils.Sequence(inputSeqArr).printSeq()
                    # print("eyeOpen: ", openCloseTime)
            elif (300 > max(rightData) > EEGns.upperTH) and (
                    300 > max(leftData) > EEGns.upperTH) and openCloseState == 1:  # open
                self.eye_state.emit("Eyes are opened!!")
                openCloseState = 0
                openTime = time.time()
                closeOpenTime = openTime - closeTime
                if closeOpenTime < 0.3:
                    self.eye_state.emit("Short blink time!!")
                elif closeOpenTime < 0.62:
                    self.eye_state.emit("Medium blink time!!")
                else:
                    self.eye_state.emit("long blink time!!")
                inputSeqArr.append(EEGutils.Blink(length=[closeOpenTime]))
                #EEGutils.Sequence(inputSeqArr).printSeq()

        return (inputSeqArr[0].classify(), inputSeqArr[1].classify())


    def getinput(self):
        
        
        while True:

            """ 3.1 ACQUIRE DATA """
            # Obtain EEG data from the LSL stream
            if self.intr_val[0]:
                return -1

            # Only keep the channel we're interested in
            # ch_data = np.array(eeg_data)[:, INDEX_CHANNEL]

        
            # print(fs)
            eeg_data, timestamp = MUSEns.EEGinlet.pull_chunk(
                timeout=0.5, max_samples=int(10))

            # print(eeg_data)
            outValue = readFullinputedSeq(eeg_data)
            

            if outValue != 0 and outValue:
                return outValue

    def choose(self):
        # time.sleep(5)
        print("started")
        code = self.getinput()

        if code != -1:
            # code = int(code)
            # print("In choose")
            # print(code)
            # time.sleep(5)
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
        BlinkMorseCode = ""
        paragraph = ""

        self.eeg_sig.emit()

        while True:
            # if end signal is sent break from this loop
            morseBlinkLength = EEGutils.getMorseData()
            # rdata, ldata = filter_dataFreq(eegData)

            if self.intr_val:
                self.intr_val = 0
                break

            if morseBlinkLength > 0.6:
                letter = EEGutils.decodeMorse(BlinkMorseCode)
                if letter == 'save':
                    self.str_sig.emit("")
                    self.m_letter.emit("")
                    break
                elif letter == 'clr':
                    paragraph = ""
                elif letter != None:
                    paragraph += letter

                self.str_sig.emit(paragraph)
                BlinkMorseCode = ""
                self.m_letter.emit(BlinkMorseCode)
            else:
                    if 0.2 > morseBlinkLength >= 0:
                        BlinkMorseCode = BlinkMorseCode + '.'
                        self.m_letter.emit(BlinkMorseCode)

                    elif 0.6 > morseBlinkLength > 0.2:
                        BlinkMorseCode = BlinkMorseCode + '-'
                        self.m_letter.emit(BlinkMorseCode)

        self.fin.emit()
        self.cnt_return.emit()

    def setIntr(self, val):
        self.intr_val = val


