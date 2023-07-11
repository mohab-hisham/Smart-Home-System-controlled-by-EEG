from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class Message(qtw.QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("UIs/message.ui", self)
        self.paragraph = ""
        self.setStyleSheet("background-color: #122222; ")
        btn_style = "background-color: #ff0000; border-radius: 70px; border-color: white; background-repeat: no-repeat; "
        label_style = "background-color: #c4c4aa; border-radius: 50px; border-color: white; background-repeat: no-repeat; "
        #self.saveButton.clicked.connect(self.closeMessage)
        self.clearButton.setStyleSheet(btn_style)
        self.saveButton.setStyleSheet(btn_style)
        self.code_label.setStyleSheet(label_style)
        self.message_label.setStyleSheet(label_style)
        self.info_label.setStyleSheet(label_style)



    def closeMessage(self):
        self.close()

    def write_pragraph(self, paragraph):
        print("in write paragraph")
        self.paragraph =  self.paragraph + paragraph
        self.message_label.setText(self.paragraph)

    def show_code(self, code):
        self.code_label.setText(code)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    msg = Message()
    msg.showFullScreen()
    sys.exit(app.exec_())