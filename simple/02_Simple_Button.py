from PySide6.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PySide6.QtCore import Slot
import sys


app = QApplication(sys.argv)
window = QWidget()
window.resize(800, 600)
# 自定槽函数
@Slot()
def say_hello():
    label = QLabel("Hello World!", parent=window)
    label.move(0,50)


btn = QPushButton("Click me", parent=window)
# 将自定义槽函数与按钮的点击信号链接
btn.clicked.connect(say_hello)
window.show()
app.exec()
