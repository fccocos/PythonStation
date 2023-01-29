import sys
from PySide6.QtWidgets import (QMainWindow, QApplication, QHBoxLayout, QWidget,
                               QPushButton, QToolTip)
from PySide6.QtGui import QGuiApplication, QIcon, QPixmap, QFont

"""
setAlignment 设置对齐方式

setToolTip 设置控件提示信息
selectedText() 返回所有

window.setWindowIcon(QIcon('img path')) 在window中可以显示图标，但是在Macos中无法显示
app.setWindowIcon(QIcon('img path')) 在window和Macos中都可以显示图标
"""


class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.button1 = QPushButton('我的按钮')
        self.initGUI()

    def initGUI(self):
        self.resize(300, 240)
        self.setWindowTitle('设置窗口图标')
        self.setWindowIcon(QIcon('./image/姜饼.png'))

        QToolTip.setFont(QFont('Apple', 12))
        self.setToolTip('今天是<b>星期五</b>')
        self.setGeometry(300, 200, 200, 300)

        self.button1.setToolTip('There is a button. Are you OK?')

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QPixmap('./image/姜饼.png'))

    window = Window()
    window.show()

    sys.exit(app.exec())
