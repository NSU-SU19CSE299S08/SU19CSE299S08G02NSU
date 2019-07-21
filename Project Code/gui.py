from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import os
import os.path
from PyQt5.uic import loadUiType
import urllib.request

ui, _ = loadUiType('GUI/main.ui')


class MainApp(QMainWindow, ui):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.inint_ui()
        self.handle_buttons()

    def inint_ui(self):
        pass

    def handle_buttons(self):
        self.pushButton.clicked.connect(self.download_file)
        self.pushButton_3.clicked.connect(self.handle_browse)

    def handle_progress(self, block_num, block_size, total_size):
        read_data = block_num * block_size
        if total_size > 0:
            download_percentage = read_data * 100 / total_size
            self.progressBar.setValue(download_percentage)
            QApplication.processEvents()

    def handle_browse(self):
        save_location = QFileDialog.getSaveFileName(caption='Save as', directory='.', filter="All Files(*.*)")
        print(save_location)
        self.lineEdit_2.setText(str(save_location[0]))

    def download_file(self):
        print('Stating Download')
        download_url = self.lineEdit.text()
        save_location = self.lineEdit_2.text()

        urllib.request.urlretrieve(download_url, save_location, self.handle_progress)

    def save_browse(self):
        pass


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
