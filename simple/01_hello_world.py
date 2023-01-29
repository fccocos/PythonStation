import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)
window = QWidget()
label = QLabel("Hello World", parent=window)
label2 = QLabel("<font color=red size=40>Hello World!</font>", parent=window)
label2.move(0,100)
window.resize(800, 600)
window.show()
app.exec()