"""
QLineEdit的校验器(Validator)

限制输入框只能输入整数、浮点数、字符串等
"""

import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import QIntValidator, QDoubleValidator, QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression

class QLineEidtValidator(QWidget):
    def __init__(self):
        super(QLineEidtValidator, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('校验器')

        # 创建表单布局
        formLayout = QFormLayout()

        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()

        formLayout.addRow('整数类型：', intLineEdit)
        formLayout.addRow('浮点类型：', doubleLineEdit)
        formLayout.addRow('数字和字母：', validatorLineEdit)

        # 设置文本提示
        intLineEdit.setPlaceholderText('integer')
        doubleLineEdit.setPlaceholderText('double')
        validatorLineEdit.setPlaceholderText('Number and letter')

        # 整数校验器
        intValidator = QIntValidator(self)
        intValidator.setRange(1, 99)

        # 浮点数校验器
        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-360, 360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        # 设置精度，小数点后两位
        doubleValidator.setDecimals(2)

        # 数字和字母
        reg = QRegularExpression('[a-zA-Z0-9]+$')
        validator = QRegularExpressionValidator(self)
        validator.setRegularExpression(reg)

        # 设置校验器
        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(validator)

        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QLineEidtValidator()
    window.show()

    sys.exit(app.exec())