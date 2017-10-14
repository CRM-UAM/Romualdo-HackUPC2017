#!/usr/bin/python
# -*- coding: utf-8 -*-

import speech_recognition as sr
from api_key import API_KEY

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Calibrando... Silencio!")
    r.adjust_for_ambient_noise(source)

def recognize_speech():
    print("Listening...")
    r.pause_threshold = 0.8
    with sr.Microphone() as source:
        audio = r.listen(source, phrase_time_limit=4)
    
    print("Processing speech...")
    # recognize speech using Bing Voice Recognition
    try:
        text = r.recognize_bing(audio, key=API_KEY)
        return text
    except sr.UnknownValueError:
        return "ERROR NO SPEECH DETECTED"
    except sr.RequestError as e:
        return "ERROR CANNOT CONNECT"

#print(recognize_speech())

