from PyQt5 import QtWidgets as qtw
from PyQt5 import uic, QtCore
from PyQt5.QtGui import QPixmap
import sys
import main as m
class Loading(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #bath = "DeskTop App/"
        uic.loadUi("UIs/loading.ui", self)
        #self.steps = 4
        #self.progressBar.se
        self.setStyleSheet("background-color: #122222; ")
        self.progressBar.setStyleSheet("border-radius: 1px; border-color: white;")
        self.welcome_label.setStyleSheet("background-color: #fffff0; border-radius: 50px;border: 10px solid orange; ")

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    b = Loading()
    b.showFullScreen()
    sys.exit(app.exec_())