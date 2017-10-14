#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import subprocess
import re

random.seed()

def decir(texto):
  tones=[9.19, 32.6, 54.1, 89.19]
  subprocess.check_output(['espeak', '-v', 'mb-us1', '-s', '110', '-p', str(random.choice(tones)), str(texto)])


def romualdo_says(texto):
  tokens = re.split(';|,|\.|:', texto)
  for t in tokens:
    #print t
    decir(t)
  
romualdo_says("Hello, how are you? I love chicken; Oh my gosh!. look at that bunny!")



 
 