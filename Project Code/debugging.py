from PyQt5.QtWidgets import *
import sys
import os
import os.path
from PyQt5.uic import loadUiType
import urllib.request
import pafy
import humanize
import pyttsx3
import win32com.client
from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from socket import *


def open_main():
    try:
        ui, = loadUiType('GUI/start.ui')
    except Exception:
        pass

        class StartApp(QMainWindow, ui):
            def __init__(self, parent=None):
                super(StartApp, self).__init__(parent)
                QMainWindow.__init__(self)
                self.setupUi(self)
                self.inint_ui()
                self.handle_buttons()

            def inint_ui(self):
                pass

            def handle_buttons(self):
                self.pushButton_1.clicked.connect(self.open_github)
                self.pushButton_2.clicked.connect(self.open_facebook)
                self.pushButton_3.clicked.connect(self.open_slack)
                self.pushButton_4.clicked.connect(self.open_gmail)

            def open_github(self):
                os.startfile(
                    'C:/Users/smahe/OneDrive/Documents/GitHub/SU19CSE299S08G02NSU/Project Code/all_files/github.txt')

            def open_slack(self):
                os.startfile(
                    'C:/Users/smahe/OneDrive/Documents/GitHub/SU19CSE299S08G02NSU/Project Code/all_files/slack.txt')

            def open_gmail(self):
                os.startfile(
                    'C:/Users/smahe/OneDrive/Documents/GitHub/SU19CSE299S08G02NSU/Project Code/all_files/gmail.txt')

            def open_facebook(self):
                os.startfile(
                    'C:/Users/smahe/OneDrive/Documents/GitHub/SU19CSE299S08G02NSU/Project Code/all_files/facebook.txt')

    def main():
        app = QApplication(sys.argv)
        window = StartApp()
        window.show()
        app.exec_()

    if __name__ == '__main__':
        main()


open_main()
