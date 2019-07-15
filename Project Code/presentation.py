import pyttsx3
from selenium import webdriver
import win32com.client
import time
from pynput.keyboard import Key, Controller
import speech_recognition as sr

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
    keyboard.press(Key.cmd)
    keyboard.press(Key.alt)
    keyboard.press('r')
    screen_recording_stop()


def screen_recording_stop():
    keyboard.release('r')
    keyboard.release(Key.alt)
    keyboard.release(Key.cmd)


serena = pyttsx3.init()
voices = serena.getProperty('voices')
serena.setProperty('voice', voices[0].id)
serena.setProperty('rate', 170)


#
# def my_command():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         r.pause_threshold = 2
#         r.adjust_for_ambient_noise(source, duration=1)
#         audio = r.listen(source)
#     try:
#         command = r.recognize_google(audio)
#         print(command)
#         return command
#
#     except sr.UnknownValueError or TypeError:
#         assistant()
def my_command():
    return str(input()).lower()


def assistant():
    command = my_command()
    if 'open facebook' in command:
        serena.say('Opening Facebook')
        serena.runAndWait()
        driver = webdriver.Firefox(executable_path='C:\geckodriver.exe')
        driver.get('https://www.facebook.com/')
    if 'hello serena' in command:
        change_voice(1)
        serena.say('Welcome Back Sir, How are you.')
        serena.runAndWait()
    if 'hello jarvis' in command:
        change_voice(0)
        serena.say('Welcome back sir, I am jarvis.')
        serena.runAndWait()
    if 'run' in command:
        n = 2
        with open('txt files/intro.txt', 'r') as inputFile:
            lines = inputFile.readlines()

        app = win32com.client.Dispatch("PowerPoint.Application")
        presentation = app.Presentations.Open(FileName=u'E:\\Android-OS-Memory-Management.pptx', ReadOnly=1)
        screen_recording_start()
        presentation.SlideShowSettings.Run()
        time.sleep(5)
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

    # else:
    #     change_voice('s')
    #     serena.say('You said: {}'.format(command))
    #     serena.runAndWait()


while True:
    try:
        assistant()
    except TypeError:
        continue
