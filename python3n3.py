#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 12:57:31 2020

@author: macbookair
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.browser = QWebEngineView()
        self.browser.setUrl( QUrl("https://google.com")) 
        
        self.setCentralWidget(self.browser)
        
        self.show()
        
        self.setWindowTitle("Page Browser")
        self.setWindowIcon( QIcon("icon1.png") )
        
        self.browser = QWebEngineView()
        self.browser.setUrl( QUrl("https://google.com")) 
        
        
app = QApplication(sys.argv)
app.setApplicationName("Page Browser")
window = MainWindow()
window.show()

app.exec_()