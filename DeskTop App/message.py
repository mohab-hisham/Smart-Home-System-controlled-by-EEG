from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class Message(qtw.QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("UIs/message.ui", self)
        self.saveButton.clicked.connect(self.closeMessage)
        self.saveButton.clicked.connect(lambda:self.write_pragraph(""))
        self.saveButton.clicked.connect(lambda: self.show_code(""))
        self.clearButton.clicked.connect(lambda: self.write_pragraph(""))

    def closeMessage(self):
        self.close()

    def write_pragraph(self, paragraph):
        self.message_label.setText(paragraph)

    def show_code(self, code):
        self.code_label.setText(code)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    msg = Message()
    msg.show()
    sys.exit(app.exec_())