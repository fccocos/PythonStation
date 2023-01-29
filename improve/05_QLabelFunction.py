import  sys
from PySide6.QtWidgets import (QLabel, QWidget, QPushButton, QVBoxLayout,
                               QApplication, QMainWindow)
from PySide6.QtGui import QPalette, QPixmap
from PySide6.QtCore import Qt

"""
QLabel控件的基本用法

setAlignment 设置文本对齐方式
setIndent 设置文本缩进
text 获取文本
setBuddy 设置伙伴关系
selectedText 返回所选字符
setwordWrap 设置是否允许换行

QLabel常用信号（事件）

鼠标划过QLabel控件时触发：linkHovered
鼠标点击QLabel控件时触发：linkActivated
"""


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label1 = QLabel('label1')
        self.label2 = QLabel('label2')
        self.label3 = QLabel('label3')
        self.label4 = QLabel('label4')
        self.initGUI()

    def initGUI(self):
        self.label1.setText('<font color=yellow>这是一个标签</font>')
        self.label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)
        self.label1.setPalette(palette)
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")

        self.label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label3.setToolTip('这是一个图片标签')
        self.label3.setPixmap(QPixmap("./image/姜饼.png"))

        self.label4.setOpenExternalLinks(True)
        self.label4.setText("<a href='https://item.dj.com/12317265.html'>🙏关注《Python从菜鸟到高手》</a>")
        self.label4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label4.setToolTip('这是一个超级链接')

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.label3)
        vbox.addWidget(self.label4)

        mainFrame = QWidget()
        mainFrame.setLayout(vbox)
        self.setCentralWidget(mainFrame)
        self.label2.linkHovered.connect(self.linkHovered)
        self.label4.linkActivated.connect(self.linkClicked)

    def linkHovered(self):
        print('当鼠标滑过label2标签时，触发事件')

    def linkClicked(self):
        print('当鼠标点击label4标签时，触发事件')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    app.setWindowIcon(QPixmap("./image/姜饼.png"))
    sys.exit(app.exec())

