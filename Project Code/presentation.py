import pyttsx3
from selenium import webdriver
import win32com.client
import time
from pynput.keyboard import Key, Controller

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
