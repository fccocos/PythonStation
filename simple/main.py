import ui_rgb
from PySide6.QtWidgets import QApplication, QWidget
import sys

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.form = ui_rgb.Ui_Form()
        self.form.setupUi(self)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())