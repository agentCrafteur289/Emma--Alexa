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
engine.setProperty("voice", voices[1].id)
greetme()
engine.say("Comment allez vous ?")
engine.runAnWait()

def emma_command():
    with sr.Microphone() as source:
        print("listenning...")
        listener.pause_threshold = 5
        voice = listener.listen(source)
        command = listener.recognize_google(voice, language="fr-FR")
        command = command.lower()
        print (command)
        if "emma" in command:
            command = command.replace("emma", "")
            print(command)

    return command


def run_emma():
    command = emma_command()
    if "musique" in command:
        song = command.replace("musique", "")
        talk("musique en cours...")
        pywhatkit.playonyt(song)
    elif "Heure" in command:
        time = datetime.datetime.now().strtime("%H:%M")
        print ()
        talk("il est actuelement :" + time)
    elif "qui est" in command:
        person = command.replace("Qui est", "")
        wikipedia.set_lang("fr")
        info = wikipedia.summary(person, 1)
    elif "sortir" in command:
        talk("Désolé, j'ai trop la flemme")
    elif "es-tu en couple" in command:
        talk("T'iquiete, je suis sur un coup")
    elif "Blague" in command:
# Mettre des blagues dans joke
        jokes = ["Le developer est un flemmard",
        "Il ne pas encore adresse cette fonction"]
        talk(random.choice(jokes))
    elif "et toi" in command:
        msgs = ["Je fais juste mon truc !",
        "Je vais bien !",
        "Bien !",
        "Je suis bien et plein d'énergie."]
        talk(random.choice(msgs))
    elif "désactive toi" in command:
        talk("Merci de m'avoir utilisé")
        sys.exit()
    else:
        talk("Pourrais tu repété ? je n'ai pas bien compris")

if __name__ == '__main__':
    while True:
        run_emma()