import pyttsx3
import speech_recognition as sr
from selenium import webdriver
import sys


def change_voice(a):
    if a == 's':
        serena.setProperty('voice', voices[1].id)
    else:
        serena.setProperty('voice', voices[0].id)


serena = pyttsx3.init()
voices = serena.getProperty('voices')
serena.setProperty('voice', voices[0].id)
serena.setProperty('rate', 170)


# serena.say("Hello, I am Jarvis")
# change_voice()
# serena.say("Welcome back,Sir.")
# change_voice()
# serena.say('who is this?')
# change_voice()
# serena.say('I am Serena')
# serena.runAndWait()

def my_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 2
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(command)
        return command

    except sr.UnknownValueError or TypeError:
        assistant()


def assistant():
    temp = my_command()
    command = str(temp).lower()
    if 'open facebook' in command:
        driver = webdriver.Firefox(executable_path='C:\geckodriver.exe')
        driver.get('https://www.facebook.com/')
    if 'hello serena' in command:
        change_voice('s')
        serena.say('Welcome Back Sir, How are you.')
        serena.runAndWait()
    if 'hello jarvis' in command:
        change_voice('j')
        serena.say('Welcome back sir, I am jarvis.')
        serena.runAndWait()
    if 'close app' in command:
        serena.say('Good Bye Sir, get some sleep')
        serena.runAndWait()
        sys.exit()
    else:
        change_voice('s')
        serena.say('You said: {}'.format(command))
        serena.runAndWait()


while True:
    try:
        assistant()
    except TypeError:
        continue
