import time
from PyQt5.QtCore import *

import numpy as np  # Module that simplifies computations on matrices
import matplotlib.pyplot as plt  # Module used for plotting
from pylsl import StreamInlet, resolve_byprop  # Module to receive EEG data

import time

import threading
import asyncio
# import variables
from types import SimpleNamespace

from Utils import collectEEGsignal,readFullinputedSeq,MUSEns,EEGns, EEGutils


ns = SimpleNamespace()

# Handy little enum to make code more readable

class CntWorker(QObject):
    eeg_cnt = pyqtSignal(int)
    fin = pyqtSignal()
    

    def getinput(self):
        
        
        while True:

            """ 3.1 ACQUIRE DATA """
            # Obtain EEG data from the LSL stream
           

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
        # code = int(code)
        # print("In choose")
        # print(code)
        # time.sleep(5)
        self.eeg_cnt.emit(code)
        print("sig is emitted")
        time.sleep(2)
        self.fin.emit()
        print("fin is emitted")


class EEG_Worker(QObject):
    eeg_sig = pyqtSignal()
    str_sig = pyqtSignal(str)
    m_letter = pyqtSignal(str)
    fin = pyqtSignal()
    cnt_return = pyqtSignal()
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

            if morseBlinkLength > 0.9:
                letter = EEGutils.decodeMorse(BlinkMorseCode)
                if letter == 'save':
                    self.fin.emit()
                    self.cnt_return.emit()
                    break
                elif letter == 'clr':
                    paragraph = ""
                else:
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

                    elif 0.9 > morseBlinkLength > 0.6:
                        BlinkMorseCode = BlinkMorseCode + '*'
                        self.m_letter.emit(BlinkMorseCode)






