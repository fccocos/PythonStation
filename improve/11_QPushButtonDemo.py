"""

QAbstractButton

QPushButton
QToolButton
QRadioButton
QCheckBox
"""

import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QPushButton Demo')

        layout = QVBoxLayout()

        self.button1 = QPushButton('第一个按钮')
        self.button1.setText('Firt Button')
        self.button1.setCheckable(True)  # 设置按钮可复选
        self.button1.toggle() # 设置按钮为开关

        self.button1.clicked.connect(lambda: self.whichButton(self.button1))
        self.button1.clicked.connect(self.buttonState)
        layout.addWidget(self.button1)

        # 在文本前面显示图像
        self.button2 = QPushButton('图像按钮')
        self.button2.setIcon(QIcon(QPixmap('./image/姜饼.png')))
        self.button2.clicked.connect(lambda: self.whichButton(self.button2))
        layout.addWidget(self.button2)

        self.button3 = QPushButton('不可用按钮')
        self.button3.setEnabled(False)
        self.button3.clicked.connect(lambda: self.whichButton(self.button3))
        layout.addWidget(self.button3)

        self.button4 = QPushButton('默认按钮')
        self.button4.setDefault(True)
        self.button4.setText('&MyDefaultButton')
        self.button4.clicked.connect(lambda: self.whichButton(self.button4))
        layout.addWidget(self.button4)

        self.setLayout(layout)

    def whichButton(self, btn):
        print('被点击的按钮时<' + btn.text() + '>')

    def buttonState(self):
        if self.button1.isChecked():
            print('button1被选中')
        else:
            print('button1没有被选中')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QPushButtonDemo()
    win.show()
    sys.exit(app.exec())