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


def open_idm():
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
            self.pushButton_13.clicked.connect(self.save_browser_playlist)

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
                best_quality = video.getbest()
                download = best_quality.download(filepath=save_location, callback=self.video_progress)
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
            QApplication.processEvents()

            for video in playlist_videos:
                video = video['pafy']
                best_quality = video.getbest()
                self.lcdNumber.display(current_video_in_download)
                download = best_quality.download(callback=self.playlist_progress)
                QApplication.processEvents()
                current_video_in_download += 1

        def playlist_progress(self, total, received, ratio, rate, time):
            read_data = received
            if total > 0:
                download_percentage = read_data * 100 / total
                self.progressBar_4.setValue(download_percentage)
                remaining_time = round(time / 60, 2)
                self.label_2.setText(str('{} minutes remaining'.format(remaining_time)))
                QApplication.processEvents()

        def save_browser_playlist(self):
            playlist_save_location = QFileDialog.getExistingDirectory(self, 'Select Download Directory')
            self.lineEdit_14.setText(playlist_save_location)

    def main():
        app = QApplication(sys.argv)
        window = MainApp()
        window.show()
        app.exec_()

    if __name__ == '__main__':
        main()


def run_presentation():
    keyboard = Controller()

    def change_voice(a):
        if a == 1:
            serena.setProperty('voice', voices[1].id)
        else:
            serena.setProperty('voice', voices[0].id)

    def screen_recording_start():
        keyboard.press(Key.cmd)
        keyboard.press('g')
        keyboard.release(Key.cmd)
        keyboard.release('g')
        keyboard.press(Key.cmd)
        keyboard.press('g')
        keyboard.release(Key.cmd)
        keyboard.release('g')
        time.sleep(3)

        keyboard.press(Key.cmd)
        keyboard.press(Key.alt)
        keyboard.press('r')
        screen_recording_stop()
        time.sleep(3)

    def screen_recording_stop():
        keyboard.release('r')
        keyboard.release(Key.alt)
        keyboard.release(Key.cmd)

    serena = pyttsx3.init()
    voices = serena.getProperty('voices')
    serena.setProperty('voice', voices[0].id)
    serena.setProperty('rate', 170)

    def my_command():
        return str(input()).lower()

    def assistant():
        n = 2
        with open('txt files/intro.txt', 'r') as inputFile:
            lines = inputFile.readlines()

        app = win32com.client.Dispatch("PowerPoint.Application")
        presentation = app.Presentations.Open(FileName=u'E:\\Android-OS-Memory-Management.pptx', ReadOnly=1)
        presentation.SlideShowSettings.Run()
        screen_recording_start()
        change_voice(1)
        for line in lines:
            serena.say(line)
            serena.runAndWait()
        presentation.SlideShowWindow.View.Next()
        serena.say('Now I am going to call Jarvis to assist me. Hello Jarvis ,  welcome.')
        change_voice(0)
        serena.say('Thanks Serena.')
        with open('txt files/introMM.txt', 'r') as inputFile:
            lines = inputFile.readlines()
        for line in lines:
            serena.say(line)
            serena.runAndWait()
            change_voice(0 if n % 2 == 0 else 1)
            n += 1
        presentation.SlideShowWindow.View.Next()
        change_voice(1)
        with open('txt files/paging.txt', 'r') as inputFile:
            lines = inputFile.readlines()
        n = 2
        for line in lines:
            serena.say(line)
            serena.runAndWait()
            change_voice(0 if n % 2 == 0 else 1)
            n += 1
        presentation.SlideShowWindow.View.Next()
        change_voice(0)
        with open('txt files/garbage.txt', 'r') as inputFile:
            lines = inputFile.readlines()
        n = 1
        for line in lines:
            serena.say(line)
            serena.runAndWait()
            change_voice(0 if n % 2 == 0 else 1)
            n += 1
        presentation.SlideShowWindow.View.Next()
        change_voice(0)
        with open('txt files/shared_memory.txt', 'r') as inputFile:
            lines = inputFile.readlines()
        n = 1
        for line in lines:
            serena.say(line)
            serena.runAndWait()
            change_voice(0 if n % 2 == 0 else 1)
            n += 1
        serena.runAndWait()
        presentation.SlideShowWindow.View.Next()
        change_voice(1)
        with open('txt files/last_page.txt', 'r') as inputFile:
            lines = inputFile.readlines()
        n = 1
        for line in lines:
            serena.say(line)
            serena.runAndWait()
            change_voice(0 if n % 2 == 0 else 1)
            n += 1
        change_voice(1)
        screen_recording_start()
        presentation.Close()

    while True:
        try:
            assistant()
        except TypeError:
            continue


def log_to_facebook():
    driver = webdriver.Firefox(executable_path='C:\geckodriver.exe')
    driver.get('https://www.facebook.com/')
    email_element = driver.find_element(By.XPATH, './/*[@id="email"]')
    email_element.send_keys('maheen@northsouth.edu')
    pass_element = driver.find_element(By.XPATH, './/*[@id="pass"]')
    pass_element.send_keys('abecoeasd')
    elem = driver.find_element(By.XPATH, '//*[@id="u_0_2"]')
    elem.click()


def log_to_github():
    driver = webdriver.Firefox(executable_path='C:\geckodriver.exe')

    driver.get('https://github.com/')
    sign_in_element = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
    sign_in_element.click()
    username_element = driver.find_element_by_xpath('//*[@id="login_field"]')
    username_element.send_keys('mustavi.maheen@northsouth.edu')
    password_element = driver.find_element_by_xpath('//*[@id="password"]')
    password_element.send_keys('Porosh11')
    log_in_element = driver.find_element_by_xpath('/html/body/div[3]/main/div/form/div[3]/input[7]')
    log_in_element.click()


def log_to_slack():
    driver = webdriver.Firefox(executable_path='C:\geckodriver.exe')

    driver.execute_script("window.open('')")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("http://slack.com/")

    sign_in = driver.find_element_by_xpath('/html/body/header/nav[1]/div/ul/li[6]/a')
    sign_in.click()
    sign_in_to_workspace = driver.find_element_by_xpath('//*[@id="domain"]')
    sign_in_to_workspace.send_keys('su19cse299nsusas3')
    log_in_element = driver.find_element_by_xpath('//*[@id="submit_team_domain"]')
    log_in_element.click()
    username_element = driver.find_element_by_xpath('//*[@id="email"]')
    username_element.send_keys('mustavi.maheen@northsouth.edu')
    password_element = driver.find_element_by_xpath('//*[@id="password"]')
    password_element.send_keys('Porosh111')
    remember_me = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/form/div[1]/label')
    remember_me.click()
    log_in_element = driver.find_element_by_xpath('//*[@id="signin_btn"]')
    log_in_element.click()


def log_in_mail():
    driver = webdriver.Firefox(executable_path='C:\geckodriver.exe')

    driver.execute_script("window.open('')")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("http://mail.google.com/")
    enter_email = driver.find_element_by_xpath('//*[@id="identifierId"]')
    enter_email.send_keys('mustavi.maheen@northsouth.edu')
    enter_email.send_keys(Keys.ENTER)
    time.sleep(5)
    enter_pass = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
    enter_pass.send_keys('Mustavi23.27!@!@')
    enter_pass.send_keys(Keys.ENTER)
    time.sleep(10)


host = "192.168.43.115"
port_android = 7890

while True:
    socket_android = socket(AF_INET, SOCK_STREAM)
    socket_android.bind((host, port_android))
    socket_android.listen(5)
    c_android, addr_android = socket_android.accept()
    receivedData = (c_android.recv(1024).decode('utf-8'))
    print('Client:', receivedData)
    if 'login to slack' in receivedData:
        log_to_slack()
    if 'login to facebook' in receivedData.lower():
        log_to_facebook()
    if 'login to github' in receivedData.lower():
        log_to_github()
    if 'login to mail' in receivedData.lower():
        log_in_mail()
    if 'open idm' in receivedData.lower():
        open_idm()
    if 'give a presentation' in receivedData.lower():
        run_presentation()
