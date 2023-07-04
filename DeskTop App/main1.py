import time
from PyQt5.QtCore import *


class CntWorker(QObject):
    eeg_cnt = pyqtSignal(int)
    fin = pyqtSignal()

    def choose(self):
        code = input("choose")

        code = int(code)
        print("In choose")
        #time.sleep(5)
        self.eeg_cnt.emit(code)
        print("sig is emitted")
        #time.sleep(2)
        self.fin.emit()
        print("fin is emitted")


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
        time.sleep(5)
        self.eeg_sig.emit()
        time.sleep(5)
        self.cnt_return.emit()
        self.fin.emit()

    def morse(self):
        self.eeg_sig.emit()
        while 1:
            code = input("select")
            code = int(code)
            if code == 0 or self.intr_val:
                self.intr_val = 0
                break
            print("In select")
            #time.sleep(5)
            self.str_sig.emit(str(code))
            self.m_letter.emit(str(code+1))
            print("sig is emitted")
            #time.sleep(2)
        self.cnt_return.emit()
        self.fin.emit()
        print("morse fin is emitted")

    def setIntr(self, val):
        self.intr_val = val






