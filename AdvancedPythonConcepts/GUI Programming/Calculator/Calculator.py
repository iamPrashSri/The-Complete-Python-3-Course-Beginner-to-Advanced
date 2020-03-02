import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Button:
    def __init__(self, text, results):
        self.b = QPushButton(str(text))
        self.text = text
        self.results = results
        self.b.clicked.connect(lambda : self.handleInput(self.text))

    def handleInput(self, val):
        if val == '=':
            self.results.setText(str(eval(self.results.text())))
        elif val == 'AC':
            self.results.setText("")
        elif val == '√':
            self.results.setText(str(math.sqrt(int(self.results.text()))))
        elif val == 'DEL':
            self.results.setText(self.results.text()[:-1])
        else:
            self.results.setText(self.results.text() + str(val))

class CalcApplication(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.createApp()

    def createApp(self):
        # Create the GridLayout
        gL = QGridLayout()
        results = QLineEdit()

        gL.addWidget(results, 0, 0, 1, 4)

        buttons = ['AC', '√', 'DEL', '/',
                   7, 8, 9, '*',
                   4, 5, 6, '-',
                   1, 2, 3, '+',
                   0, '.', '=']

        row = 1
        col = 0
        for button in buttons:
            if col > 3:
                col = 0
                row += 1

            btnObj = Button(button, results)

            if button == 0:
                gL.addWidget(btnObj.b, row, col, 1, 2)
                col += 1
            else:
                gL.addWidget(btnObj.b, row, col, 1, 1)
            col += 1

        self.setLayout(gL)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalcApplication()
    sys.exit(app.exec())
