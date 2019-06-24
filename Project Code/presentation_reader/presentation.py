import pyttsx3
# import speech_recognition as sr
import win32com.client
import time

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# def my_command():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         r.pause_threshold = 1
#         r.adjust_for_ambient_noise(source, duration=1)
#         audio = r.listen(source)
#     try:
#         command = r.recognize_google(audio)
#
#     except sr.UnknownValueError:
#         assistant(my_command())


def assistant():
    with open("Intro.txt", "r") as inputFile:
        lines = inputFile.readlines()

    app = win32com.client.Dispatch("PowerPoint.Application")
    presentation = app.Presentations.Open(FileName=u'E:\\Android Process Management.pptm', ReadOnly=1)

    presentation.SlideShowSettings.Run()

    time.sleep(1)
    for line in lines:
        print(line)
        engine.say(line)
        engine.runAndWait()


n = 1
while n < 2:
    assistant()
    n += 1
