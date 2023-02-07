'''
QCheckBox有三种状态
 未选中：0
 半选中：1
 选中： 2
'''

import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class CheckButtonDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QRadioButton Demo')
        self.resize(400, 360)

        layout = QHBoxLayout()

        self.checkBtn1 = QCheckBox('Check1')
        self.checkBtn1.setTristate(True)
        self.checkBtn1.stateChanged.connect(self.checkState)
        layout.addWidget(self.checkBtn1)
        self.setLayout(layout)

    def checkState(self):
        print(self.checkBtn1.text() + ' checkValue:' +
              str(self.checkBtn1.checkState()) + ' checkState:' +
              str(self.checkBtn1.isChecked()))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CheckButtonDemo()
    win.show()
    sys.exit(app.exec())