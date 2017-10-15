
import time
import random

from servo_control import *
from recognize_speech import *
from romualdo_says import *

#dialogflow = Dialogflow(client_access_token="0a487393af224f75806710df607258ac")
from cleverwrap import CleverWrap

cw = CleverWrap('CC4yjEfbAKy_z5KzxphYI49GIHQ')

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
            say(["I couldn't hear you.","Can't hear a thing","It's too loud here","I cannot hear you."])
            if i > 1: return None
            say(["Please say again","Please talk louder","Please come closer, tell me","Tell me"])
            continue
        if text == "ERROR CANNOT CONNECT":
            say(["I'm afraid that WiFi is not working and I couldn't hear you.","Sorry, I've lost my internet connection and could not process your beautiful speech."])
            say(["The wonders of cloud computing! Ha ha.","We thought it was a good idea to use a cloud speech recognition software... what a fail!"])
            if i > 1: return None
            say(["So","Tell me again","Let's try again","Ok, so"])
            continue
        break
    if text == "ERROR NO SPEECH DETECTED" or text == "ERROR CANNOT CONNECT": return None
    print("Answer: "+str(text))
    say(["I see.","Ok.","Oh.","Cool.","Sweet."])
    return text




romualdo_says("Hello!")

wave_hand()

romualdo_says("My name is Romualdo, I'm a robot entertainer that lives on a pizza box!")



reply = ask_question("What is your name?")
if reply:
    reply = reply.split()
    name = reply[-1]
    name = name[:-1]
    say(["Nice to meet you "+name+"!","Cool name "+name+"!","That's a sweet name "+name+"!","Hey there "+name+"!",name+" Interesting name!",name+" is a breautiful name"])


reply = ask_question("How old are you?")
if reply:
    reply = reply.split()
    age = reply[-1]
    say(["I'm afraid you're too old for me.","Already? Happy late birthday then!","You look much younger than "+age,"Wow you still look pretty good to be "+age])


time.sleep(2)

say(["So.","Well.","Hmm","Are you single?","Actually, I woudn't mind a date with you"])





reply = ask_question("Would you go on a date with me?")
if reply:
    reply = reply.split()
    answer = reply[0]
    if answer[-1] == ".": answer = answer[:-1]
    answer = answer.lower()
    if answer == "no":
        say(["Oh","Ouch","Ok.","You've broken my heart","My heart is broken now"])
    else:
        say(["Oh my god.","Yes!","OMG","Sweet!"])
        say(["I knew you'd say yes.","Thank you.","Nobody ever dates me.","Nobody ever says yes."])
        say(["I'll make sure to bring pizza for our date.","Want a slice from my pizza box? Hahaha"])
    


say(["So.","Well.","Hmm","Are you single?","Actually, I woudn't mind a date with you","Would you go on a date with me? I'll bring pizza."])


while(True):
    say(["Say something.","What do you think of the weather?","So how are you?","You look beautiful today","Where are you from?","Do you believe in love after love?","I like chicken","I want to hear your beautiful voice again"])
    text = ask_question("",ignore_silence=True)
    if text is not None:
        #reply = dialogflow.text_request(text)
        reply = cw.say(text)
        print(reply)
        reply = str(reply)
        romualdo_says(reply)


