## aqui va la parte de las funciones tts

import pyttsx3

def text_to_speech(text):
    """
    Convierte texto a voz en tiempo real utilizando pyttsx3.
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
