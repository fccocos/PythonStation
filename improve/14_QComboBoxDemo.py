'''
下拉列表控件（QComboBox）
1。 如果将列表项添加到QComboBox控件中
2。 如何获取选中的列表项
'''

import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class ComboBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QComboBox Demo')
        self.resize(400, 360)

        layout = QVBoxLayout()

        self.lab = QLabel('Language:')
        self.comboBox1 = QComboBox()
        self.comboBox1.addItems(['c++', 'ruby', 'python',
                                 'java', 'javascript', 'c#'])
        self.comboBox1.currentIndexChanged.connect(self.comboBoxState)
        layout.addWidget(self.lab)
        layout.addWidget(self.comboBox1)
        self.setLayout(layout)

    def comboBoxState(self, i):
        self.lab.setText(self.comboBox1.itemText(
            self.comboBox1.currentIndex()
        ))
        self.lab.adjustSize()

        for count in range(self.comboBox1.count()):
            print('item' + str(count) + '=' +
                  self.comboBox1.itemText(count))
        print('current index', i, 'selection changed',
              self.comboBox1.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ComboBoxDemo()
    win.show()
    sys.exit(app.exec())