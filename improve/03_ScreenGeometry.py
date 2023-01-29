import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget, QPushButton
from PySide6.QtGui import QGuiApplication


def onClick_Button():
    print('method 1')
    print('widget (x, y)=(%d, %d)' % (widget.x(), widget.y()))
    print('widget (w, h)=(%d, %d)' % (widget.width(), widget.height()))
    print('method 2')
    print('geometry (x, y)=(%d, %d)' % (widget.geometry().x(), widget.geometry().y()))
    print('geometry (w, h)=(%d, %d)' % (widget.geometry().width(), widget.geometry().height()))
    print('method 3')
    print('frame (x, y)=(%d, %d)' % (widget.frameGeometry().x(), widget.frameGeometry().y()))
    print('frame (w, h)=(%d, %d)' % (widget.frameGeometry().width(), widget.frameGeometry().height()))


app = QApplication(sys.argv)
widget = QWidget()
btn = QPushButton('btn', widget)
btn.clicked.connect(onClick_Button)
widget.resize(300, 240)
widget.move(250, 200)
widget.setWindowTitle('屏幕坐标系')
widget.show()

sys.exit(app.exec())
