from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
import sys
from Utils.EEGutils import EEGns, calibrate

class Calibration(qtw.QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("UIs/cali.ui", self)
        self.setStyleSheet("background-color: #122222; ")
        btn_style = "background-color: #ff0000; border-radius: 30px; border-color: white; background-repeat: no-repeat; "
        label_style = "background-color: #00a000; border-radius: 30px; border-color: white; background-repeat: no-repeat; "
        spin_style = "background-color: #f5f5dc; border-radius: 20px; border-color: white; background-repeat: no-repeat; "
        self.submitButton.setStyleSheet(btn_style)
        self.autoButton.setStyleSheet(btn_style)
        self.min_label.setStyleSheet(label_style)
        self.mint_SpinBox.setStyleSheet(spin_style)
        self.maxt_label.setStyleSheet(label_style)
        self.maxt_SpinBox.setStyleSheet(spin_style)
        self.autoButton.clicked.connect(calibrate)

        self.maxt_SpinBox.setValue(EEGns.upperTH)
        self.mint_SpinBox.setValue(EEGns.lowerTH)

        #self.submitButton.clicked.connect(self.closeCalibration)
        self.maxt_SpinBox.valueChanged.connect(self.changeTH)
        self.mint_SpinBox.valueChanged.connect(self.changeTL)

    def closeCalibration(self):
        self.close()

    def changeTH(self):
        upper = self.maxt_SpinBox.value()
        EEGns.upperTH = upper

    def changeTL(self):
        lower = self.mint_SpinBox.value()
        EEGns.lowerTH = lower


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    calibration = Calibration()
    calibration.showFullScreen()
    sys.exit(app.exec_())