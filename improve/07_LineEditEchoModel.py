import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

"""
QLineEdit控件与回显模式

基本功能：输入单行的文本

EchoMode(回显模式）

1. Normal
2. NoEcho
3. PassWord
4. PasswordEchoOnEdit
"""

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')

        formLayout = QFormLayout()

        normaLineEidt = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEdit = QLineEdit()

        formLayout.addRow("Normal", normaLineEidt)
        formLayout.addRow("NoEcho", noEchoLineEdit)
        formLayout.addRow("Password", passwordLineEdit)
        formLayout.addRow("PasswordEchoOnEdit", passwordEchoOnEdit)

        # 设置文本提示
        normaLineEidt.setPlaceholderText('Normal')
        noEchoLineEdit.setPlaceholderText('NoEcho')
        passwordLineEdit.setPlaceholderText('Password')
        passwordEchoOnEdit.setPlaceholderText('PasswordEchoOnEdit')

        # 设置回显模式
        normaLineEidt.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec())
