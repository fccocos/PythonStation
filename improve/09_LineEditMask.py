import sys
from PySide6.QtWidgets import *

"""
掩码字符
A ascii字母      必须输入          （a-z、A-Z）
a ascii字母      允许输入但不是必要的
N ascii字母      必须输入          （a-z、A-Z、0-9）
n ascii字母      允许输入但不是必要的
X 任何字符        必须输入
x 任何字符        允许输入但不是必要的
9 ascii数字      必须              （0-9）
0 ascii数字      允许输入但不是必要的
D ascii数字      必须              （1-9）
d ascii数字      允许输入但不是必要的
# ascii数字或加减 允许输入但不是必要的
H 十六进制        必须
h 十六进制        允许
B 二进制          必须
b 二进制          允许
元字符
>                输入的字母都会转换成大写
<                输入的字母都会转换成小写
!                关闭大小写转换
;c               终止输入掩码并将空白字符转换为c
[ ] { }          保留
\                用于转移上面的特殊字符，将其用作分隔符
"""

class QLineEditMask(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('用掩码限制QLineEdit控件的输入')
        formLayout = QFormLayout()

        ipLineEdit = QLineEdit()
        macLineEdit = QLineEdit()
        dateLineEdit = QLineEdit()
        licenseLineEdit = QLineEdit()

        ipLineEdit.setInputMask("000.000.000.000;_")
        macLineEdit.setInputMask("HH:HH:HH:HH:HH:HH;_")
        dateLineEdit.setInputMask("0000-00-00")
        licenseLineEdit.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#")

        formLayout.addRow('数字掩码', ipLineEdit)
        formLayout.addRow('Mac掩码', macLineEdit)
        formLayout.addRow('日期掩码', dateLineEdit)
        formLayout.addRow('许可证掩码', licenseLineEdit)

        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QLineEditMask()
    window.show()

    sys.exit(app.exec())