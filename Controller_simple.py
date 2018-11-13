# -*- coding: utf-8 -*-

import time
import random

from servo_control import *
from recognize_speech import *
from romualdo_says import *
from api_key import API_KEY_CHATBOT
import webbrowser


#from dialogflow import Dialogflow
#dialogflow = Dialogflow(client_access_token=API_KEY_CHATBOT)
from cleverwrap import CleverWrap
cw = CleverWrap(API_KEY_CHATBOT)

set_inter_phrase_callback(hand_random)

def say(phrase_list):
    romualdo_says(random.choice(phrase_list))
#say(["","","",""])

def ask_question(question, ignore_silence=False):
    i = 0
    while True:
        i += 1
        if len(question) > 0: romualdo_says(question)
        text = recognize_speech()
        if not ignore_silence and text == "ERROR NO SPEECH DETECTED":
            say(["No te oigo.","No oigo nada!","Hay mucho ruido","No puedo oirte."])
            if i > 1: return None
            say(["Repite, por favor","Por favor acercate al micrófono","Habla mas alto, por favor. Dime","Dime"])
            continue
        if text == "ERROR CANNOT CONNECT":
            say(["No tengo internet y no puedo reconocer voz. Carita triste.","Lo siento, no funciona internet y no puedo reconocer tu preciosa voz."])
            say(["La magia de la nube! Ja ja ja","Es tremendo cuando falla la nube. jejeje"])
            if i > 1: return None
            say(["Entonces","Repitemelo","Volvamos a intentarlo","Okey, entonces"])
            continue
        break
    if text == "ERROR NO SPEECH DETECTED" or text == "ERROR CANNOT CONNECT": return None
    print("RESPUESTA RECONOCIDA: "+str(text))
    if not ignore_silence: say(["Ya veo.","Okey.","Oh.","Bien.","Interesante."])
    return text



romualdo_says("Hola hola!")

#wave_hand()

romualdo_says("Me llamo Oshwaldo, soy un bot que adora el software libre y los sapoconchos")



reply = ask_question("Como te llamas?")
if reply:
    reply = reply.split()
    name = reply[-1]
    #name = name[:-1]
    say(["Encantado de conocerte "+name+"!","Es un nombre muy bonito "+name+"!","Que nombre tan chulo "+name+"!","Hola "+name+"!","Oh! "+name+" que nombre tan interesante!",name+" es un nombre precioso"])

age_aux=0
reply = ask_question("Cuantos anios tienes?")
if reply:
    reply = reply.split()
    age = reply[0]
    age_aux = int(age)
    if age_aux > 18:
        say(["Oh vaya, no esta mal. Pero conozco sapoconchos mas viejos"])
        #say(["Me temo que eres muy mayor para mi.","Tan pronto? Feliz cumpleaños, con retraso!","Pareces mucho mas joven que "+age+" anios","Guau! Todavia tienes buen aspecto para tener "+age])
    else:
        say(["Oh vaya! Quieres ser mi amigo?", "El otro dia conoci a alguien de tu edad, me robó las tuercas"])

#time.sleep(2)

if age_aux >= 18:
    say(["Hum.","Bueno.","Hum hum hum.","Eres soltero?","De hecho, no me importaria tener una cita contigo"])
    reply = ask_question("Tendrias una cita conmigo? Puedes venir con pareja soy de mente abierta")
    if reply:
        reply = reply.split()
        answer = reply[0]
        if answer[-1] == ".": answer = answer[:-1]
        answer = answer.lower()
        if answer == "no":
            say(["Oh","Ouch","Okey.","Me rompes el corazon","Me has roto el corazon"])
        else:
            say(["Guau.","Si!","OMaiGod!","Que guay!"])
            say(["Sabia que dirias si.","Gracias.","Nunca nadie quiere tener una cita conmigo.","Nadie me habia dicho que si."])
            say(["Me asegurare de llevar pixsa a nuestra cita.","Voy encargando el menu de fiesta."])
    


#say(["Hum.","Bueno.","Hum, hum, hum.","Eres soltero o soltera?","De hecho, no me importaria tener una cita contigo"])

#say(["UN momento! Me estan jackeando, me estan jackeando! Ah no, solo eran gases. Continuemos"])

n = 0
while(True):
    say(["Dime algo.","Que opinas del tiempo?","Y que tal estas?","Hoy estas estupenda","Hoy estas especialmente guapa","De que ciudad eres?","Crees en el amor?","Me gusta el pollo frito", "Quien vive en la pinia debajo del mar?","Dime algo, estoy aburrido!","Me he quedado sin palabras","Perdona que no te hable, es que eres tan guapa"])
    text = ask_question("",ignore_silence=True)
    if text is not None:
        #reply = dialogflow.text_request(text)
        #reply = cw.say(text)
	reply = text ########### respondemos lo mismo que nos han dicho
        print(reply)
        reply = str(reply)
        romualdo_says(reply)
    n += 1
    if n > 2: break


say(["Has llegado al final de la demo! Gracias por participar! Aqui tienes un poco de música!"])
#webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")


