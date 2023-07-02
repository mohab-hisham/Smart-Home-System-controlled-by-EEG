from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class Message(qtw.QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("UIs/message.ui", self)
        self.saveButton.clicked.connect(self.closeMessage)

    def closeMessage(self):
        self.close()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    msg = Message()
    msg.show()
    sys.exit(app.exec_())