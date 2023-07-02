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
    fin = pyqtSignal()
    cnt_return = pyqtSignal()
    def navigate(self):
        time.sleep(5)
        self.eeg_sig.emit()
        time.sleep(5)
        self.cnt_return.emit()
        self.fin.emit()






