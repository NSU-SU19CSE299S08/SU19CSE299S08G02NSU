from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import os
import os.path
from PyQt5.uic import loadUiType
import urllib.request
import pafy
import humanize

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
        self.pushButton_7.clicked.connect(self.get_video_data)
        self.pushButton_12.clicked.connect(self.download_video)
        self.pushButton_6.clicked.connect(self.save_browse_yt)
        self.pushButton_14.clicked.connect(self.playlist_downloader)

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

        if download_url == '' or save_location == '':
            QMessageBox.warning(self, "Data Error", "Provide a Valid URL or save Location")
        else:
            try:
                urllib.request.urlretrieve(download_url, save_location, self.handle_progress)
            except Exception:
                QMessageBox.warning(self, "Data Error", "Provide a Valid URL or save Location")
        QMessageBox.information(self, "Download Completed", "The Download Completed Successfully")
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.progressBar.setValue(0)

    def save_browse(self):
        pass

    #####################YT downloader##############################

    def save_browse_yt(self):
        save_location = QFileDialog.getSaveFileName(caption='Save as', directory='.', filter="All Files(*.*)")
        self.lineEdit_8.setText(str(save_location[0]))

    def get_video_data(self):
        video_url = self.lineEdit_7.text()
        if video_url == '':
            QMessageBox.warning(self, "Data Error", "Provide a Valid Video URL")
        else:
            video = pafy.new(video_url)
            print(video.title)
            print(video.duration)

            video_streams = video.videostreams
            for stream in video_streams:
                size = humanize.naturalsize(stream.get_filesize())
                if stream.extension == 'mp4':
                    data = "{} {} {} {}".format(stream.mediatype, stream.extension, stream.quality, size)
                    self.comboBox.addItem(data)

    def download_video(self):
        video_url = self.lineEdit_7.text()
        save_location = self.lineEdit_8.text()
        if video_url == '' or save_location == '':
            QMessageBox.warning(self, "Data Error", "Provide a Valid URL or save Location")
        else:
            video = pafy.new(video_url)
            video_stream = video.videostreams
            video_quality = self.comboBox.currentIndex()
            download = video_stream[video_quality].download(filepath=save_location, callback=self.video_progress)
            QMessageBox.information(self, "Download Completed", "The Download Completed Successfully")
            QApplication.processEvents()

    def video_progress(self, total, received, ratio, rate, time):
        read_data = received
        if total > 0:
            download_percentage = read_data * 100 / total
            self.progressBar_3.setValue(download_percentage)
            remaining_time = round(time / 60, 2)
            self.label_8.setText(str('{} minutes remaining'.format(remaining_time)))
            QApplication.processEvents()

    def playlist_downloader(self):
        playlist_url = self.lineEdit_13.text()
        save_location = self.lineEdit_14.text()
        if playlist_url == '' or save_location == '':
            QMessageBox.warning(self, "Data Error", "Provide a Valid URL or save Location")
        else:
            playlist = pafy.get_playlist(playlist_url)
            playlist_videos = playlist['items']
            self.lcdNumber_2.display(len(playlist_videos))

        os.chdir(save_location)
        if os.path.exists(str(playlist['title'])):
            os.chdir(str(playlist['title']))
        else:
            os.mkdir(str(playlist['title']))
            os.chdir(str(playlist['title']))
        current_video_in_download = 1
        quality = self.comboBox_2.currentIndex()
        self.lcdNumber.display(current_video_in_download)
        for video in playlist_videos:
            current_video = video['pafy']
            current_video_stream = current_video.videostreams
            downnload = current_video_stream[quality].download(callback=self.playlist_progress)
            current_video_in_download += 1

    def playlist_progress(self, total, received, ratio, rate, time):
        pass


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
