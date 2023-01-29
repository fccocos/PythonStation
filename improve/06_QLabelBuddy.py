from PySide6.QtWidgets import *
import sys


class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel与伙伴控件')

        nameLabel = QLabel('&Name', self)
        nameLineEdit = QLineEdit(self)
        nameLabel.setBuddy(nameLineEdit)

        passwdLabel = QLabel('&Passwd', self)
        passwdLineEdit = QLineEdit(self)
        passwdLabel.setBuddy(passwdLineEdit)

        btnOK = QPushButton('&OK')
        btnCancel = QPushButton('&Cencel')

        mainFrame = QGridLayout()
        mainFrame.addWidget(nameLabel, 0, 0)
        mainFrame.addWidget(nameLineEdit, 0, 1, 1, 2)
        mainFrame.addWidget(passwdLabel, 1, 0)
        mainFrame.addWidget(passwdLineEdit, 1, 1, 1, 2)
        mainFrame.addWidget(btnOK, 2, 1)
        mainFrame.addWidget(btnCancel, 2, 2)

        self.setLayout(mainFrame)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QLabelBuddy()
    window.show()
    sys.exit(app.exec())
