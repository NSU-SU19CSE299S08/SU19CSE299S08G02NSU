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

