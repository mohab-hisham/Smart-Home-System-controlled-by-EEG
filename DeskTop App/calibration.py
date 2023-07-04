from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
import sys
#from Utils import EEGns

class Calibration(qtw.QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("UIs/calib.ui", self)
        #self.maxt_SpinBox.setValue(EEGns.upperTH)
        #self.mint_SpinBox.setValue(EEGns.lowerTH)

        self.submitButton.clicked.connect(self.closeCalibration)
        self.maxt_SpinBox.valueChanged.connect(self.changeTH)
        self.mint_SpinBox.valueChanged.connect(self.changeTL)

    def closeCalibration(self):
        self.close()

    def changeTH(self):
        upper = self.maxt_SpinBox.value()
        #EEGns.upperTH = upper

    def changeTL(self):
        lower = self.mint_SpinBox.value()
        #EEGns.lowerTH = lower


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    calibration = Calibration()
    calibration.show()
    sys.exit(app.exec_())