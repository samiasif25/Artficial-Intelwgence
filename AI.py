from pyttsx3 import voice


def speak(audio):
    pass  # For now, we will write the conditions later.
import pyttsx3

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voice[0].id)
def speak(audio):

engine.say(audio)

engine.runAndWait() #Without this command, speech will not be audible to us.
if __name__ == "__main__":

speak("Code With Harry")

import datetime


def wishme():


hour = int(datetime.datetime.now().hour)

import speechRecognition as sr




