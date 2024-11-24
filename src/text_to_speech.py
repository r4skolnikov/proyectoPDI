## aqui va la parte de las funciones tts

import pyttsx3

tts_engine = pyttsx3.init()
tts_engine.setProperty("rate", 150)

def speak_text(text):
    """
    Convierte texto a voz en tiempo real utilizando pyttsx3.
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
