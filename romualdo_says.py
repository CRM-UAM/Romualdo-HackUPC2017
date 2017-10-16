#!/usr/bin/python
# -*- coding: utf-8 -*-

from dialogflow import Dialogflow

import random
import subprocess
import re

random.seed()

def decir(texto):
  tones=[9.19, 20.21, 32.6, 39.38, 54.1, 70.62, 89.19]
  velocities=[110,120,130]
  # 'setsid -w' removes ALL output from the espeak program
  subprocess.check_output(['setsid', '-w', 'espeak', '-a', '200', '-v', 'mb-us1', '-s', str(random.choice(velocities)), '-p', str(random.choice(tones)), str(texto)])

def romualdo_says(texto):
  global inter_phrase_callback   
  tokens = re.split('(?<=[;,.:!?])\s*', texto)
  for t in tokens:
    #print t
    if inter_phrase_callback is not None: inter_phrase_callback()
    decir(t)

inter_phrase_callback = None
def set_inter_phrase_callback(function):
    global inter_phrase_callback
    inter_phrase_callback = function

#romualdo_says("Hello, how are you? I love chicken; Oh my gosh! look at that bunny! It's sooo pretty.")

#romualdo_says("We're no strangers to love. You know the rules, and so do I! A full commitment's what I'm thinking of. You wouldn't get this from any other guy! I, just wanna tell you how I'm feeling. Gotta make you understand! Never gonna give you up! Never gonna let you down! Never gonna run around and desert you! Never gonna make you cry! Never gonna say goodbye! Never gonna tell a lie, and hurt you!")

 
 
