import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget, QPushButton
from PySide6.QtGui import QGuiApplication


class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle('Quit application')
        self.resize(800, 600)

        self.button1 = QPushButton('退出应用程序')
        self.button1.clicked.connect(self.onClick_Button)
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def onClick_Button(self):
        sender = self.sender()
        print(sender.text() + '按钮按下')
        app = QApplication.instance()
        app.quit()

    def setCenter(self):
        # 获取屏幕坐标系
        screen = QGuiApplication.primaryScreen()
        screenXY = screen.availableVirtualGeometry()
        print(screenXY)
        # 获取窗口坐标系
        windowXY = self.geometry()
        centerX = (screenXY.width()-windowXY.width())/2
        centerY = (screenXY.height()-windowXY.height())/2
        self.move(centerX, centerY)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainwin = Window()
    mainwin.setCenter()
    mainwin.show()
    sys.exit(app.exec())
