import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QVBoxLayout


class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Qt样式实例大全-simple版')
        self.resize(800, 600)

        self.line_edit = QLineEdit()
        self.line_edit.setText('There is a input editor')
        self.line_edit.setObjectName('line_edit')

        self.pwd = QLineEdit()
        self.pwd.setText('Please input your passwd')
        self.pwd.setObjectName('pwd')

        self.name = QLineEdit()
        self.name.setText('Please input your name')
        self.name.setObjectName('name')

        self.label = QLabel('There is a placeholder text...')
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("""
            background-color: #000
            color: #FFFFFF
            font: 20px
        """)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.name)
        layout.addWidget(self.pwd)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("QLineEdit { background: yellow; color: gray }")
    window = Window()
    window.show()
    sys.exit(app.exec())
