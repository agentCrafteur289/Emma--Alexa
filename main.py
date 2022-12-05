import sys

import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import random

# import subprocess
# import time
# from sys import *

# Pour installer les module/Librairies
# requirements = ["PyAudio","pyttsx3","pywhatkit","SpeechRecognition","wikipedia","datetime","random"]
# for modul in requirements:
#     try: __import__(modul[0])
#     except:
#         subprocess.Popen(f"{executable} -m pip install {modul[1]}", shell=True)
#         time.sleep(3)


listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("voice","french")
engine.setProperty("rate", 170)
voices = engine.getProperty("voices")

def talk(text):
    engine.say(text)
    engine.runAndWait()

# Salut moi
def greetme():
    current_hour = int(datetime.datetime.now().hour)
    if 0 <= current_hour < 12:
        talk("Bonjour !")

    if 12 <= current_hour < 18:
        talk("Bonne après midi !")
    
    if current_hour >= 18 and current_hour != 0:
        talk("Bonsoir !")


# Set french female voice (changer l'indice [3] si la voix n'est pas bonne)

engine.setProperty("voice", voices[0].id)
greetme()
engine.say("Que puige faire pour vous ?")
engine.runAndWait()

def emma_command():
    with sr.Microphone() as source:
        print("listenning...")
        listener.pause_threshold = 5
        voice = listener.listen(source)
        command = listener.recognize_google(voice, language="fr-FR")
        command = command.lower()
        print(command)
        if "emma" in command:
            command = command.replace("emma", "")
            print(command)

    return command


def run_emma():
    command = emma_command()
    if "musique" in command:
        song = command.replace("musique", "")
        talk("musique en cours...")
        print(song)
        pywhatkit.playonyt(song)
    elif "heure" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        talk("il est actuelement :" + time)
    elif "qui est" in command:
        person = command.replace("Qui est", "")
        wikipedia.set_lang("fr")
        info = wikipedia.summary(person, 1)
    elif "sortir" in command:
        talk("Désolé, j'ai trop la flemme")
    elif "es-tu en couple" in command:
        talk("T'iquiete, je suis sur un coup")
    elif "blague" in command:
        jokes = ["Le developer est un flemmard",
        "Il n'a pas encore eu le temps pour cette fonction"]
        talk(random.choice(jokes))
    elif "et toi" in command:
        msgs = ["Je fais juste mon truc !",
        "Je vais bien !",
        "Bien !",
        "Je suis bien et plein d'énergie."]
        talk(random.choice(msgs))
    elif "stop toi" in command:
        talk("Merci de m'avoir utilisé")
        sys.exit()
    elif "jenna" in command:
        talk("jenna elle est thaah adopter")
    elif "chahid" in command:
        talk("L'homosexualite de cette personne ne devrait pas etre un blem")
    elif "entend" in command:
        talk("OUI, parfaitement")
    else:
        talk("Pourrais tu repété ? je n'ai pas bien compris") 


if __name__ == '__main__':
    while True:
        run_emma()