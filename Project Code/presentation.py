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
        # time.sleep(2)
        presentation.SlideShowSettings.Run()
        keyboard.press(Key.cmd)
        keyboard.press(Key.alt)
        keyboard.press('r')
        keyboard.release('r')
        keyboard.release(Key.alt)
        time.sleep(5)
        change_voice(1)
        for line in lines:
            serena.say(line)
            serena.runAndWait()
        presentation.SlideShowWindow.View.Next()
        serena.say('Now I am going to call Jarvis to assist me. Hello Jarvis ,  welcome.')
        change_voice(0)
        serena.say('Thanks Serena.')

    # else:
    #     change_voice('s')
    #     serena.say('You said: {}'.format(command))
    #     serena.runAndWait()


while True:
    try:
        assistant()
    except TypeError:
        continue
