# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rgbEkSDlR.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QSlider, QSpinBox, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(553, 304)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 551, 301))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.spinBox = QSpinBox(self.gridLayoutWidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox, 2, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.spinBox_3 = QSpinBox(self.gridLayoutWidget)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_3, 2, 2, 1, 1)

        self.spinBox_2 = QSpinBox(self.gridLayoutWidget)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_2, 2, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)

        self.verticalSlider = QSlider(self.gridLayoutWidget)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMaximum(255)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout.addWidget(self.verticalSlider, 3, 0, 1, 1)

        self.verticalSlider_2 = QSlider(self.gridLayoutWidget)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        self.verticalSlider_2.setMaximum(255)
        self.verticalSlider_2.setOrientation(Qt.Vertical)

        self.gridLayout.addWidget(self.verticalSlider_2, 3, 1, 1, 1)

        self.verticalSlider_3 = QSlider(self.gridLayoutWidget)
        self.verticalSlider_3.setObjectName(u"verticalSlider_3")
        self.verticalSlider_3.setMaximum(255)
        self.verticalSlider_3.setOrientation(Qt.Vertical)

        self.gridLayout.addWidget(self.verticalSlider_3, 3, 2, 1, 1)


        self.retranslateUi(Form)
        self.spinBox.valueChanged.connect(self.verticalSlider.setValue)
        self.spinBox_2.valueChanged.connect(self.verticalSlider_2.setValue)
        self.spinBox_3.valueChanged.connect(self.verticalSlider_3.setValue)
        self.verticalSlider.sliderMoved.connect(self.spinBox.setValue)
        self.verticalSlider_2.sliderMoved.connect(self.spinBox_2.setValue)
        self.verticalSlider_3.sliderMoved.connect(self.spinBox_3.setValue)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Red", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Green", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Blue", None))
    # retranslateUi

