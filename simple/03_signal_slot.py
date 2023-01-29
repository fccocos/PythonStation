import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Slot, Signal, Qt, QObject


# class Button(QWidget):
#     clicked = Signal(Qt.MouseButton)
#
#     def mousePressEvent(self, event):
#         self.clicked.emit(event.button())

class Communicate(QObject):
    speak = Signal((int,), (str,))
    people = Signal(int, str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.speak[int].connect(self.say_something)
        self.speak[str].connect(self.say_something)
        self.people.connect(self.people_info)

    @Slot(int)
    @Slot(str)
    def say_something(self, arg):
        if isinstance(arg, int):
            print('This is a number: ', arg)
        elif isinstance(arg, str):
            print('This is a string: ', arg)

    @Slot(int, str)
    def people_info(self, age, name):
        print('It is', name,',', age, 'years old')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    someone = Communicate()
    someone.speak.emit(10)
    someone.speak[str].emit("Hello everybody!")
    someone.people.emit(23, 'Jason')
    sys.exit(app.exec())


