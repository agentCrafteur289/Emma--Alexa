import sys

import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import random

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("voice","french")
engine.setProperty("rate", 170)

def talk(text):
    engine.say(text)
    engine.runAndWait()

# Salut moi
def greetme():
    current_hour = int(datetime.datetime.nom().hour)
    if 0 <= current_hour < 12:
        talk("Bonjour mon chèr maitre")

    if 12 <= current_hour < 10:
        talk("Bon après midi, chèr maitre")
    
    if current_hour >= 10 and current_hour != 0:
        talk("Bonsoir chèr maitre")


# Set french female voice (changer l'indice [3] si la voix n'est pas bonne)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[3].id)
greetme()
engine.say("Comment allez vous ?")
engine.runAnWait()