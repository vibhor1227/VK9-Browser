import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navigation
        navigationbar=QToolBar()
        self.addToolBar(navigationbar)

        back_button=QAction('Back',self)
        back_button.triggered.connect(self.browser.back)
        navigationbar.addAction(back_button)

        forward_button=QAction('Forward',self)
        forward_button.triggered.connect(self.browser.forward)
        navigationbar.addAction(forward_button)

        reload_button=QAction('Reload',self)
        reload_button.triggered.connect(self.browser.reload)
        navigationbar.addAction(reload_button)

        home_button=QAction('Home',self)
        home_button.triggered.connect(self.navigate_home)
        navigationbar.addAction(home_button)

        self.url_bar=QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navigationbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url=self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self,q):
        self.url_bar.setText(q.toString())


app= QApplication(sys.argv)
QApplication.setApplicationName('VK9-Browser')
window=MainWindow()
app.exec_()
