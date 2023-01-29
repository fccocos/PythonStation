import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QGuiApplication


class FirstWin(QMainWindow):
    def __init__(self, parent=None):
        super(FirstWin, self).__init__(parent)
        self.setWindowTitle('第一主窗口')
        self.resize(800, 600)

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

    mainwin = FirstWin()
    mainwin.setCenter()
    mainwin.show()
    sys.exit(app.exec())
