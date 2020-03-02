import sys
import os
import json

from PyQt5.QtWidgets import (QApplication, QWidget,
                             QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QLineEdit,
                             QTabBar, QFrame, QStackedLayout, QTabWidget,
                             QShortcut, QKeySequenceEdit, QSplitter)

from PyQt5.QtGui import (QIcon, QWindow, QImage, QKeySequence)
from PyQt5.QtCore import *
from PySide2.QtWebEngineWidgets import *

class AddressBar(QLineEdit):
    def __init__(self):
        super().__init__()

    def mousePressEvent(self, e):
        self.selectAll()

class WebBrowser(QFrame):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Web Browser')
        self.setBaseSize(1366, 768)
        self.setMinimumSize(1366, 768)
        self.createApp()
        self.setWindowIcon(QIcon('logo.png'))

    def createApp(self):
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        #  TabBar
        self.tabBar = QTabBar(movable=True, tabsClosable=True)
        self.tabBar.tabCloseRequested.connect(self.closeTab)
        self.tabBar.tabBarClicked.connect(self.switchTab)

        # self.tabBar.addTab('Tab 1')
        # self.tabBar.addTab('Tab 2')
        # self.tabBar = QTabWidget()
        # self.tabBar.addTab(QPushButton('Tab 1'), 'First Tab')
        # self.tabBar.addTab(QPushButton('Tab 2'), 'Second Tab')

        self.tabBar.setCurrentIndex(0)  # Which Tab in the row of tabs is active
        self.tabBar.setDrawBase(False)
        self.tabBar.setLayoutDirection(Qt.LeftToRight)
        self.tabBar.setElideMode(Qt.ElideLeft)

        # Create Key shortcuts
        self.shortcutNewTab = QShortcut(QKeySequence('Ctrl+T'), self)
        self.shortcutNewTab.activated.connect(self.addTab)

        self.shortcutReload = QShortcut(QKeySequence('Ctrl+R'), self)
        self.shortcutReload.activated.connect(self.reload)

        # Keep track of tabs
        self.tabCount = 0
        self.tabs = []

        # Create address bar
        self.toolBar = QWidget()
        self.toolBar.setObjectName('toolBar')
        self.toolBarLayout = QHBoxLayout()
        self.addressBar = AddressBar()
        self.addressBar.returnPressed.connect(self.browseToFromAddressBar)

        # New Tab Button
        self.addTabButton = QPushButton('+')
        self.addTabButton.clicked.connect(self.addTab)

        # Set Toolbar Buttons like Back button, Reload etc.
        self.bwdButton = QPushButton('<')
        self.bwdButton.clicked.connect(self.navigateBwd)

        self.fwdButton = QPushButton('>')
        self.fwdButton.clicked.connect(self.navigateFwd)

        self.rldButton = QPushButton('R')
        self.rldButton.clicked.connect(self.reload)

        # Build Toolbar
        self.toolBar.setLayout(self.toolBarLayout)
        self.toolBarLayout.addWidget(self.bwdButton)
        self.toolBarLayout.addWidget(self.fwdButton)
        self.toolBarLayout.addWidget(self.rldButton)
        self.toolBarLayout.addWidget(self.addressBar)
        self.toolBarLayout.addWidget(self.addTabButton)

        #  Set Main View
        self.container = QWidget()
        self.container.layout = QStackedLayout()
        self.container.setLayout(self.container.layout)

        self.layout.addWidget(self.tabBar)
        self.layout.addWidget(self.toolBar)
        self.layout.addWidget(self.container)

        self.setLayout(self.layout)
        self.show()

    def closeTab(self, i):
        self.tabBar.removeTab(i)

    def addTab(self):
        i = self.tabCount

        self.tabs.append(QWidget())
        self.tabs[i].layout = QVBoxLayout()
        self.tabs[i].layout.setContentMargins(0, 0, 0, 0)

        self.tabs[i].setObjectName('tab' + str(i))

        self.tabs[i].content = QWebEngineView()
        self.tabs[i].content.load(QUrl.fromUserInput('http://google.com'))

        #  Update the title of the Tab when the URL changes
        self.tabs[i].content.titleChanged.connect(lambda : self.setTabContent(i, 'Title'))
        self.tabs[i].content.iconChanged.connect(lambda : self.setTabContent(i, 'Icon'))
        self.tabs[i].content.urlChanged.connect(lambda: self.setTabContent(i, 'Url'))

        #  Add webview to tabs layout
        self.tabs[i].splitview = QSplitter()
        self.tabs[i].splitview.setOrientation(Qt.Vertical)
        self.tabs[i].layout.addWidget(self.tabs[i].splitview)

        self.tabs[i].splitview.addWidget(self.tabs[i].content)

        #  Set top level tab in list to Layout
        self.tabs.setLayout(self.tabs[i].layout)

        # Add tab to top level stacked widget
        self.container.layout.addWidget(self.tabs[i])
        self.container.layout.setCurrentWidget(self.tabs[i])

        # Set the tab at the top of the screen
        self.tabBar.addTab('New Tab')
        self.tabBar.setTabData(i, {'object': 'tab' + str(i), 'initial': i})
        self.tabBar.setCurrentIndex(i)

        self.tabCount += 1

    def switchTab(self, i):
        if self.tabBar.tabData(i):
            tabData = self.tabBar.tabData(i)
            tab_widget = self.findChild(QWidget, tabData)
            self.container.layout.setCurrentWidget(tab_widget)

            new_url = tab_widget.url().toString()
            self.addressBar.setText(new_url)

    def browseToFromAddressBar(self):
        txtLine = self.addressBar.text()

        i = self.tabBar.currentIndex()
        tabData = self.tabBar.tabData(i)
        tab_content = self.findChild(QWidget, tabData).content

        if 'http' not in txtLine:
            if '.' not in txtLine:
                url = 'https://www.google.com/search?q=' + str(txtLine)
            else:
                url = 'http://' + str(txtLine)
        else:
            url = txtLine
        tab_content.load(QUrl.fromUserInput(url))

    def setTabContent(self, i, type):
        tab_name = self.tabs[i].objectName()
        count = 0
        running = True
        current_tab = self.tabBar.tabData(self.tabBar.currentIndex())['object']

        if current_tab == tab_name and type == 'Url':
            new_url = self.findChild(QWidget, tab_name).content.url().toString()
            self.addressBar.setText(new_url)
            return False

        while running:
            tab_data_name = self.tabBar.tabData(count)

            if count > 99:
                running = False

            if tab_name == tab_data_name['object']:
                if type == 'Title':
                    newTitle = self.findChild(QWidget, tab_name).content.title()
                    self.tabBar.setTabText(count, newTitle)
                elif type == 'Icon':
                    newIcon = self.findChild(QWidget, tab_name).content.icon()
                    self.tabBar.setTabIcon(count, newIcon)

                running = False
            else:
                count += 1

    def navigateBwd(self):
        activeIndex = self.tabBar.currentIndex()
        tab_name = self.tabBar.tabData(activeIndex)['object']
        tab_content = self.findChild(QWidget, tab_name).content

        tab_content.back()

    def navigateFwd(self):
        activeIndex = self.tabBar.currentIndex()
        tab_name = self.tabBar.tabData(activeIndex)['object']
        tab_content = self.findChild(QWidget, tab_name).content

        tab_content.forward()

    def reload(self):
        activeIndex = self.tabBar.currentIndex()
        tab_name = self.tabBar.tabData(activeIndex)['object']
        tab_content = self.findChild(QWidget, tab_name).content

        tab_content.reload()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WebBrowser()

    with open('styles.css', 'r') as style:
        app.setStyleSheet(style.read())

    # Opening Developer Tools as part of Browser
    os.environ['QTWEBENGINE_REMOTE_DEBUGGING'] = '667'

    sys.exit(app.exec())
