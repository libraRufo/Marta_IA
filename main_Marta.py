from email.mime import audio
from telnetlib import STATUS
import speech_recognition as sr
import pyttsx3
import pywhatkit
import urllib.request
import json
import datetime
import wikipedia

# Nombre del asistente
name = 'marta'

# Key de mi api
key = 'AIzaSyBQ0RwvuGJ4mnSIEEK-LAg-AY-i2V8p2WQ'

# El flag nos ayuda a apagar el programa
flag = 1

listener = sr.Recognizer()

engine = pyttsx3.init()

# seleccion de voz
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Edicion de la configuracion basica
engine.setProperty('rate', 178)
engine.setProperty('volume', 0.7)


# Funcion para hablar
def talk(text):
    engine.say(text)
    engine.runAndWait()


# Reconocimiento de voz
def listen():
    flag = 1
    try:
        with sr.Microphone() as source:
            # voice = listener.listen(source,timeout=5, phrase_time_limit=5)
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()

            if name in rec:
                rec = rec.replace('', name)
                flag = run(rec)
            # else:
            # talk("Vuelve a intentarlo, no reconozco: " + rec)
    except:
        pass
    return flag

# Inicio interaccion
    talk("Hola en que puedo ayudatre")
def run(rec):
    '''
        Acciones que puede hacer marta
    '''


    # Reproduce la musica que le digas
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk('Reproduciendo ' + music)
        pywhatkit.playonyt(music)
    # Hola
    elif 'hola' in rec:
        talk("Hola señor, muy buenas")
    # Buenos días
    elif 'buenos días' in rec:
        talk("Buenos días señor, que quiere hacer")
    # Buenas tardes
    elif 'buenas tardes' in rec:
        talk("Buenas tardes señor, que quiere hacer")
    # Buenas noches
    elif 'buenas noches' in rec:
        talk("Buenas noches señor, que quiere hacer")
        # Descansa
    elif 'descansa' in rec:
        flag = 0
        talk("Buenas noches señor, descanse")
    # Pone lista para despertarse
    elif 'despierta' in rec:
        desp = rec.replace('despierta', '')
        talk('Reproduciendo ' + desp)
        pywhatkit.playonyt()
    # Te dice la hora
    elif 'hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las " + hora)
    # Te da informacion de la Wikipedia
    elif 'información sobre' in rec:
        order = rec.replace('información sobre', '')
        wikipedia.set_lang("es")
        info = wikipedia.summary(order, 1)
        talk(info)
    # Da gracias
    elif 'gracias' in rec:
        talk("De nada señor, quiere algo mas ?")
    # Se despide
    elif 'adiós' in rec:
        flag = 0
        talk("Adiós señor")
    elif 'hasta luego' in rec:
        flag = 0
        talk("Nos vemos señor")
        # Mensaje de error
    else:
        talk("Ha havido un problema señor")
    return flag

'''
while flag:
    flag = listen()
'''

