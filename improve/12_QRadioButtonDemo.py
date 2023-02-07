import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class RadioButtonDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QRadioButton Demo')
        self.resize(400, 360)

        layout = QHBoxLayout()

        self.radio1 = QRadioButton('Radio1')
        self.radio1.setChecked(True)
        self.radio1.toggled.connect(self.radioState)
        layout.addWidget(self.radio1)

        self.radio2 = QRadioButton('Radio2')
        self.radio2.toggled.connect(self.radioState)
        layout.addWidget(self.radio2)

        self.setLayout(layout)

    def radioState(self):
        radioBtn = self.sender()

        if radioBtn.isChecked() == True:
            print('<' + radioBtn.text() + '> is checked')
        else:
            print('<' + radioBtn.text() + '> is uncheckable')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = RadioButtonDemo()
    win.show()
    sys.exit(app.exec())
