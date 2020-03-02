#!/usr/bin/python3

import os, sys
from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtQuick import *
from PyQt5.Qt import *

# class Page(QWidget):
#     def __init__(self, parent=None):
#         super(Page, self).__init__(parent)
#
#         my_label = QLabel('This is my label')
#
#         layout = QVBoxLayout()
#         layout.addWidget(my_label)
#
#         main_layout = QGridLayout()
#         main_layout.addLayout(layout, 0, 1)
#
#         self.setLayout(main_layout)
#         self.setWindowTitle('My first Qt App')

if __name__ == '__main__':
    # import sys
    # app = QApplication(sys.argv)
    # window = Page()
    # window.show()
    # sys.exit(app.exec_())

    app =QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load(QUrl.fromLocalFile('main.qml'))

    window = engine.rootObjects()[0]
    window.show()
    sys.exit(app.exec_())
